#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

API_BASE = "https://api.github.com"
ORGS = ["AGENslab", "digenoma-lab"]
README_PATH = Path(__file__).resolve().parents[1] / "README.md"

TOOL_PATTERNS: list[tuple[str, str]] = [
    ("Nextflow", r"(?i)\bnextflow\b"),
    ("Dorado", r"(?i)\bdorado\b"),
    ("Pod5 Tools", r"(?i)\bpod5 tools\b|\bpod5\b"),
    ("SeqKit", r"(?i)\bseqkit\b"),
    ("fastp", r"(?i)\bfastp\b"),
    ("cutadapt", r"(?i)\bcutadapt\b"),
    ("BrumiR", r"(?i)\bbrumir\b"),
    ("Random Forest", r"(?i)\brandom forest\b"),
    ("Python", r"(?i)\bpython\b"),
    ("RStudio", r"(?i)\brstudio\b"),
    ("R", r"(?i)\bedger\b|\bmultimir\b|\brmarkdown\b|\bggplot2\b|\bbioconductor\b"),
    ("edgeR", r"(?i)\bedger\b"),
    ("multiMiR", r"(?i)\bmultimir\b"),
    ("windowmasker", r"(?i)\bwindowmasker\b"),
    ("BRAKER3", r"(?i)\bbraker3\b|\bbraker\b"),
    ("BUSCO", r"(?i)\bbusco\b"),
    ("UniProt", r"(?i)\buniprot\b"),
    ("Slurm", r"(?i)\bslurm\b"),
    ("Hifiasm", r"(?i)\bhifiasm\b"),
    ("RagTag", r"(?i)\bragtag\b"),
    ("GFAtools", r"(?i)\bgfatools\b"),
    ("Liftoff", r"(?i)\bliftoff\b"),
    ("BWA", r"(?i)\bbwa\b"),
    ("FastQC", r"(?i)\bfastqc\b"),
    ("STAR", r"(?i)\bstar\b"),
    ("DESeq2", r"(?i)\bdeseq2\b"),
    ("miRDeep2", r"(?i)\bmirdeep2\b"),
    ("GATK", r"(?i)\bgatk\b"),
    ("FreeBayes", r"(?i)\bfreebayes\b"),
    ("Manta", r"(?i)\bmanta\b"),
    ("Delly", r"(?i)\bdelly\b"),
    ("Pilon", r"(?i)\bpilon\b"),
    ("Racon", r"(?i)\bracon\b"),
    ("Kraken2", r"(?i)\bkraken2\b"),
    ("Bracken", r"(?i)\bbracken\b"),
    ("MetaBAT", r"(?i)\bmetabat\b"),
    ("CheckM", r"(?i)\bcheckm\b"),
    ("MetaPhlAn", r"(?i)\bmetaphlan\b"),
    ("Jellyfish", r"(?i)\bjellyfish\b"),
    ("LIGER", r"(?i)\bliger\b"),
    ("Mutect2", r"(?i)\bmutect2\b"),
    ("Strelka2", r"(?i)\bstrelka2\b"),
    ("STAR-Fusion", r"(?i)\bstar-fusion\b"),
    ("OptiType", r"(?i)\bopti[type]?\b"),
    ("NGSCheckMate", r"(?i)\bngscheckmate\b"),
    ("PURPLE", r"(?i)\bpurple\b"),
    ("Wengan", r"(?i)\bwengan\b"),
    ("HiC-Pro", r"(?i)\bhic-pro\b"),
    ("OpenCV", r"(?i)\bopencv\b"),
    ("PyTorch", r"(?i)\bpytorch\b|\btorch\b"),
    ("scikit-learn", r"(?i)\bscikit-learn\b|\bsklearn\b"),
    ("AmpliconArchitect", r"(?i)\bampliconarchitect\b"),
    ("minimap2", r"(?i)\bminimap2\b"),
    ("Samtools", r"(?i)\bsamtools\b"),
    ("Bakta", r"(?i)\bbakta\b"),
    ("Prokka", r"(?i)\bprokka\b"),
    ("Qualimap", r"(?i)\bqualimap\b"),
    ("somalier", r"(?i)\bsomalier\b"),
    ("bcftools", r"(?i)\bbcftools\b"),
    ("bedtools", r"(?i)\bbedtools\b"),
    ("Nanopore", r"(?i)\bnanopore\b"),
    ("Snakemake", r"(?i)\bsnakemake\b"),
    ("TensorFlow", r"(?i)\btensorflow\b"),
    ("Keras", r"(?i)\bkeras\b"),
    ("Transformer", r"(?i)\btransformer\b"),
]

PIPELINE_MARKERS = {
    "nextflow.config",
    "main.nf",
    "pipeline.nf",
    "workflow.nf",
    "Snakefile",
    "environment.yml",
    "pyproject.toml",
    "setup.py",
}

EXPERIMENTAL_HINTS = ("template", "demo", "tutorial", "course", "learning")
EXCLUDE_REPO_HINTS = (".github",)


@dataclass
class RepoSummary:
    org: str
    name: str
    html_url: str
    version: str
    status: str
    description: str
    tools: str


class GitHubClient:
    def __init__(self, token: str | None = None) -> None:
        self.token = token

    def _request(self, url: str) -> tuple[Any, dict[str, str]]:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "all-pipelines-readme-updater",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode("utf-8")
            headers_out = {k.lower(): v for k, v in response.headers.items()}
        return json.loads(data), headers_out

    def get_json(self, url: str) -> Any:
        data, _ = self._request(url)
        return data

    def get_paginated(self, url: str) -> list[Any]:
        items: list[Any] = []
        next_url: str | None = url
        while next_url:
            data, headers = self._request(next_url)
            if isinstance(data, list):
                items.extend(data)
            else:
                items.append(data)
            next_url = None
            link = headers.get("link", "")
            for part in link.split(","):
                if 'rel="next"' in part:
                    next_url = part[part.find("<") + 1 : part.find(">")]
                    break
        return items


def clean_md(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]*)\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" -:")


def useless_line(line: str) -> bool:
    cleaned = clean_md(line)
    if not cleaned:
        return True
    if re.fullmatch(r"[\[\]()!:/._\- ]+", line):
        return True
    if cleaned.lower().startswith(("http", "doi.org")):
        return True
    return False


def first_paragraph(md: str, fallback: str) -> str:
    lines = md.splitlines()
    current: list[str] = []
    paragraphs: list[str] = []
    in_code = False
    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not s:
            if current:
                paragraph = clean_md(" ".join(current))
                if paragraph and not useless_line(paragraph):
                    paragraphs.append(paragraph)
                current = []
            continue
        if s.startswith("#") or s.startswith("![") or s.startswith("<img"):
            continue
        if s.startswith("- ") or re.match(r"^\d+[.)]", s):
            continue
        if useless_line(s):
            continue
        current.append(s)
        if len(" ".join(current)) > 280:
            paragraph = clean_md(" ".join(current))
            if paragraph and not useless_line(paragraph):
                paragraphs.append(paragraph)
            break
    if current and not paragraphs:
        paragraph = clean_md(" ".join(current))
        if paragraph and not useless_line(paragraph):
            paragraphs.append(paragraph)
    text = paragraphs[0] if paragraphs else fallback or "No clear description in README."
    if len(text) > 150:
        text = text[:147].rsplit(" ", 1)[0] + "..."
    return text


def decode_content(content_json: dict[str, Any]) -> str:
    content = content_json.get("content", "")
    encoding = content_json.get("encoding")
    if encoding == "base64":
        return base64.b64decode(content).decode("utf-8", errors="ignore")
    return content


def get_repo_contents(client: GitHubClient, org: str, repo: str, path: str = "") -> list[dict[str, Any]]:
    encoded_path = urllib.parse.quote(path)
    url = f"{API_BASE}/repos/{org}/{repo}/contents/{encoded_path}" if path else f"{API_BASE}/repos/{org}/{repo}/contents"
    try:
        data = client.get_json(url)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return []
        raise
    return data if isinstance(data, list) else [data]


def get_text_file(client: GitHubClient, org: str, repo: str, path: str) -> str:
    encoded_path = urllib.parse.quote(path)
    url = f"{API_BASE}/repos/{org}/{repo}/contents/{encoded_path}"
    try:
        data = client.get_json(url)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return ""
        raise
    if not isinstance(data, dict):
        return ""
    return decode_content(data)


def repo_version(client: GitHubClient, org: str, repo: str, root_files: dict[str, str], readme_text: str) -> str:
    try:
        release = client.get_json(f"{API_BASE}/repos/{org}/{repo}/releases/latest")
        tag_name = release.get("tag_name")
        if tag_name:
            return tag_name
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise
    tags = client.get_paginated(f"{API_BASE}/repos/{org}/{repo}/tags?per_page=1")
    if tags:
        tag_name = tags[0].get("name")
        if tag_name:
            return tag_name
    for candidate in ("nextflow.config", "pyproject.toml", "setup.py", "environment.yml"):
        text = root_files.get(candidate, "")
        if not text:
            continue
        patterns = [
            r"\bversion\s*=\s*['\"]([^'\"]+)['\"]",
            r"\bversion\s*=\s*([0-9]+(?:\.[0-9A-Za-z_-]+)*)",
            r"manifest\.version\s*=\s*['\"]([^'\"]+)['\"]",
            r"\bversion:\s*['\"]?([^'\"\n]+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.I)
            if match:
                version = match.group(1).strip()
                if version and version.lower() not in {"false", "master", "null"} and not version.startswith("["):
                    return version
    match = re.search(r"Version\s*([0-9]+(?:\.[0-9]+){0,2})", readme_text, re.I)
    if match:
        return match.group(1)
    return "No declared version"


def repo_tools(root_files: dict[str, str], readme_text: str) -> str:
    haystack = readme_text + "\n" + "\n".join(root_files.values())
    found: list[str] = []
    for label, pattern in TOOL_PATTERNS:
        if re.search(pattern, haystack):
            found.append(label)
    deduped = list(dict.fromkeys(found))
    if not deduped:
        if any(name in root_files for name in ("nextflow.config", "main.nf", "pipeline.nf", "workflow.nf")):
            deduped.append("Nextflow")
        elif any(name in root_files for name in ("pyproject.toml", "setup.py")):
            deduped.append("Python")
    return ", ".join(deduped[:5]) if deduped else "Not specified"


def infer_status(repo_json: dict[str, Any], readme_text: str, root_names: set[str]) -> str:
    lower_name = repo_json["name"].lower()
    desc = (repo_json.get("description") or "").lower()
    readme_lower = readme_text.lower()
    topics = set(repo_json.get("topics") or [])
    has_workflow = any(name in root_names for name in ("nextflow.config", "main.nf", "pipeline.nf", "workflow.nf", "Snakefile"))
    has_docs = bool(readme_text.strip())
    if "under development" in readme_lower or "work in progress" in readme_lower or "wip" in topics:
        return "In development"
    if any(hint in lower_name for hint in EXPERIMENTAL_HINTS) or any(hint in desc for hint in EXPERIMENTAL_HINTS):
        return "Experimental"
    if has_workflow and has_docs:
        return "Active"
    if has_docs:
        return "Documented"
    return "Experimental"


def is_candidate_repo(repo_json: dict[str, Any], root_names: set[str], readme_text: str) -> bool:
    name = repo_json["name"]
    if repo_json.get("fork") or repo_json.get("archived"):
        return False
    if name.startswith(".") or name in EXCLUDE_REPO_HINTS:
        return False

    topics = set(repo_json.get("topics") or [])
    description = (repo_json.get("description") or "").lower()
    readme_lower = readme_text.lower()

    if root_names & PIPELINE_MARKERS:
        return True
    if {"nextflow", "pipeline", "bioinformatics", "workflow", "rnaseq", "genomics", "metagenomics"} & topics:
        return True
    if any(keyword in description for keyword in ("pipeline", "workflow", "analysis", "rnaseq", "genome", "genomics", "metagen")):
        return True
    if any(keyword in readme_lower for keyword in ("nextflow", "pipeline", "workflow", "analysis", "rnaseq", "genome", "genomics", "metagen")):
        return True

    # Fallback: include repositories that at least ship a README, then let status classify them.
    return bool(readme_text.strip())


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def build_repo_summary(client: GitHubClient, org: str, repo_json: dict[str, Any]) -> RepoSummary | None:
    repo = repo_json["name"]
    entries = get_repo_contents(client, org, repo)
    root_names = {entry["name"] for entry in entries if isinstance(entry, dict) and "name" in entry}

    readme_text = ""
    for candidate in ("README.md", "Readme.md", "README"):
        if candidate in root_names:
            readme_text = get_text_file(client, org, repo, candidate)
            break

    if not is_candidate_repo(repo_json, root_names, readme_text):
        return None

    root_files: dict[str, str] = {}
    for filename in PIPELINE_MARKERS:
        if filename in root_names:
            root_files[filename] = get_text_file(client, org, repo, filename)

    description = first_paragraph(readme_text, repo_json.get("description") or "No clear description in README.")
    version = repo_version(client, org, repo, root_files, readme_text)
    tools = repo_tools(root_files, readme_text)
    status = infer_status(repo_json, readme_text, root_names)

    return RepoSummary(
        org=org,
        name=repo,
        html_url=repo_json["html_url"],
        version=version,
        status=status,
        description=description,
        tools=tools,
    )


def build_readme(rows_by_org: dict[str, list[RepoSummary]]) -> str:
    lines: list[str] = []
    lines.append("# ALL_PIPELINES")
    lines.append("")
    lines.append("This repository gathers pipeline-like repositories published under the `AGENslab` and `digenoma-lab` GitHub organizations.")
    lines.append("")
    lines.append("## Automatic Update")
    lines.append("")
    lines.append("This file is generated automatically by `scripts/update_readme.py` using the GitHub API. If `GH_ORG_READ_TOKEN` is configured, private repositories from the tracked organizations are included as well.")
    lines.append("The GitHub Actions workflow `.github/workflows/update-readme.yml` refreshes it on a schedule and can also be triggered manually.")
    lines.append("")
    lines.append("## Criteria Used In This Table")
    lines.append("")
    lines.append("- **Version**: extracted from GitHub releases, tags, `nextflow.config`, `pyproject.toml`, `setup.py`, or the `README` when available.")
    lines.append("- **Status**: inferred from repository structure and explicit notes in the `README`. `Active` indicates an executable pipeline with workflow and documentation; `In development`, a pipeline under construction; `Documented`, a repository with documentation or associated analysis; `Experimental`, auxiliary material, a demo, or a template.")
    lines.append("- **Tools**: summarized from the `README`, manifests, and the main project files detected at the repository root.")
    lines.append("")
    for org in ORGS:
        lines.append(f"## {org} Pipelines")
        lines.append("")
        lines.append("| Pipeline Name | Latest Version | Status | Description | Tools Used |")
        lines.append("|---|---|---|---|---|")
        for row in rows_by_org[org]:
            lines.append(
                "| [**{name}**]({url}) | {version} | {status} | {description} | {tools} |".format(
                    name=escape_cell(row.name),
                    url=row.html_url,
                    version=escape_cell(row.version),
                    status=escape_cell(row.status),
                    description=escape_cell(row.description),
                    tools=escape_cell(row.tools),
                )
            )
        lines.append("")
    lines.append("> Note: this table is heuristic. Some repositories do not declare versions or toolchains explicitly, so the best possible inference is shown from the metadata available on GitHub.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    client = GitHubClient(token=token)
    rows_by_org: dict[str, list[RepoSummary]] = {}

    for org in ORGS:
        repos = client.get_paginated(f"{API_BASE}/orgs/{org}/repos?per_page=100&type=all")
        rows: list[RepoSummary] = []
        for repo_json in repos:
            summary = build_repo_summary(client, org, repo_json)
            if summary is not None:
                rows.append(summary)
        rows.sort(key=lambda item: item.name.lower())
        rows_by_org[org] = rows

    README_PATH.write_text(build_readme(rows_by_org), encoding="utf-8")
    for org, rows in rows_by_org.items():
        print(f"{org}: {len(rows)} repositories documented", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
