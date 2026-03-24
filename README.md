# ALL_PIPELINES

This repository gathers pipeline-like repositories published under the `AGENslab` and `digenoma-lab` GitHub organizations.

## Automatic Update

This file is generated automatically by `scripts/update_readme.py` using the GitHub API.
The GitHub Actions workflow `.github/workflows/update-readme.yml` refreshes it on a schedule and can also be triggered manually.

## Criteria Used In This Table

- **Version**: extracted from GitHub releases, tags, `nextflow.config`, `pyproject.toml`, `setup.py`, or the `README` when available.
- **Status**: inferred from repository structure and explicit notes in the `README`. `Active` indicates an executable pipeline with workflow and documentation; `In development`, a pipeline under construction; `Documented`, a repository with documentation or associated analysis; `Experimental`, auxiliary material, a demo, or a template.
- **Tools**: summarized from the `README`, manifests, and the main project files detected at the repository root.

## AGENslab Pipelines

| Pipeline Name | Latest Version | Status | Description | Tools Used |
|---|---|---|---|---|
| [**nf_rna_align**](https://github.com/AGENslab/nf_rna_align) | 1.0.0 | Active | Este pipeline automatiza las etapas de preprocesamiento, alineamiento y cuantificación de lecturas largas de RNA-seq. Está desarrollado en... | Nextflow, fastp, Slurm, BWA, FastQC |

## digenoma-lab Pipelines

| Pipeline Name | Latest Version | Status | Description | Tools Used |
|---|---|---|---|---|
| [**alndv**](https://github.com/digenoma-lab/alndv) | v1.0 | Active | A nextflow (DSL 2) Whole‑Genome Short‑Read Pipeline (BWA‑MEM2 → DeepVariant → GLnexus) for small‑variant discovery from paired‑end FASTQ files. | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**alnsl**](https://github.com/digenoma-lab/alnsl) | V0.1 | Active | A nextflow pipeline for alignment of short WGS reads. | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**biomining_metagenomes**](https://github.com/digenoma-lab/biomining_metagenomes) | No declared version | Documented | Repository that holds data, scripts and figures regarding to the mining MAGs (Cauquenes tailing) article: "Genome-resolved metagenomics and... | Nextflow, BWA, CheckM, Samtools |
| [**BRCA**](https://github.com/digenoma-lab/BRCA) | v1.0 | Active | A Nextflow pipeline for processing target NGS BRCA data | Nextflow, BWA, FastQC, Samtools, Qualimap |
| [**BRCA12_ms**](https://github.com/digenoma-lab/BRCA12_ms) | v1.0 | Documented | Code for figure and analysis of BRCA12 ms | Nextflow |
| [**call_snv**](https://github.com/digenoma-lab/call_snv) | 1.0 | Active | Nextflow pipeline for the identification of Single Nucleotide Variants (SNVs) from short-read sequences. | Nextflow, Python, Slurm, Manta, Samtools |
| [**Eval-RF-hap**](https://github.com/digenoma-lab/Eval-RF-hap) | v1.0.0 | Active | Eval-RF-hap is a Nextflow pipeline designed to evaluate the haplotyping performance of RFhap (or whatever other model to separate haplotypes),... | Nextflow, Slurm, Hifiasm, Nanopore |
| [**HBW**](https://github.com/digenoma-lab/HBW) | No declared version | Documented | HBW is a repository hold code for implementing trio-based binning and bubble graph approaches to diploid assembly but for hybrid genomic datasets... | Wengan |
| [**HistologyFeatureExtraction**](https://github.com/digenoma-lab/HistologyFeatureExtraction) | 1.1 | Active | A Nextflow pipeline for extracting features from histology whole slide images (WSI) using multiple patch and slide encoders via TRIDENT. | Nextflow, Python, Slurm, OpenCV, PyTorch |
| [**HistologyLinearProbing**](https://github.com/digenoma-lab/HistologyLinearProbing) | 1.4 | Active | Linear probing pipeline for histopathology to evaluate different feature extractors (foundation models) using Elastic Net classification on genes... | Nextflow, Python, R, Slurm, scikit-learn |
| [**HistologyMultiInstanceLearning**](https://github.com/digenoma-lab/HistologyMultiInstanceLearning) | 1.1 | Experimental | Multi-Instance Learning (MIL) pipeline for histopathology to evaluate different MIL architectures (ABMIL, CLAM, DSMIL, etc.) using pre-extracted... | Nextflow, Python, Slurm, Transformer |
| [**HistoMILTrainer**](https://github.com/digenoma-lab/HistoMILTrainer) | 1.2 | Experimental | A library for training Multi-Instance Learning (MIL) architectures from MIL-Lab on histology datasets. HistoMILTrainer provides a unified... | Python, Slurm, PyTorch, scikit-learn, Transformer |
| [**k-count-nf**](https://github.com/digenoma-lab/k-count-nf) | 1.0 | Active | A nextflow pipeline to count k-mers and estimate genome size from WGS data | Nextflow, STAR |
| [**longreadstats**](https://github.com/digenoma-lab/longreadstats) | v1.1 | Active | digenoma-lab/longreadstats is a bioinformatics best-practice analysis pipeline for computing long-read statistics with Nanoplot. | Nextflow, Python, Slurm |
| [**minibusco-nf**](https://github.com/digenoma-lab/minibusco-nf) | V0.1 | Active | A simple and scalable Nextflow pipeline to compute genome or transcriptome quality metrics using minibusco. This pipeline is designed for... | Nextflow, BUSCO, Slurm |
| [**nf-bakta**](https://github.com/digenoma-lab/nf-bakta) | v1.1 | Active | A Nextflow pipeline for the annotation of bacterial genomes or MAGs running Bakta. | Nextflow, Python, UniProt, Slurm, Bakta |
| [**nf-groot**](https://github.com/digenoma-lab/nf-groot) | No declared version | Active | A Nextflow pipeline for running Groot, which is a tool to type Antibiotic Resistance Genes (ARGs) in metagenomic samples. | Nextflow, Slurm |
| [**nf-mag-depths**](https://github.com/digenoma-lab/nf-mag-depths) | No declared version | Active | A nextflow pipeline to calculate depth of coverage from a metagenomic set of bins. | Nextflow, BWA, MetaBAT, Samtools |
| [**rfhap**](https://github.com/digenoma-lab/rfhap) | V2.0 | Active | A Nextflow pipeline for long-read phasing in trio datasets, leveraging multiple k-mers and a random forest classifier. | Nextflow, Random Forest, Slurm, Hifiasm |
| [**snps_mags**](https://github.com/digenoma-lab/snps_mags) | V1.0 | Active | snps_mags is a Nextflow pipeline designed for calling point mutations in Metagenome-Assembled Genomes (MAGs) using InStrain. The pipeline... | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**somatic_point_mutations**](https://github.com/digenoma-lab/somatic_point_mutations) | v1.1 | Active | This repository provides a Nextflow pipeline for calling somatic point mutations from tumor/normal pairs using Whole Genome Sequencing (WGS) or... | Nextflow, Python, Slurm, Manta, bcftools |
| [**spg**](https://github.com/digenoma-lab/spg) | 1.0 | Active | Simple Pan-Genome workflow for MAGs. | Nextflow, Python, Slurm, MetaBAT, Prokka |

> Note: this table is heuristic. Some repositories do not declare versions or toolchains explicitly, so the best possible inference is shown from the metadata available on GitHub.
