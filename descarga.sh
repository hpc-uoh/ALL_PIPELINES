#!/usr/bin/env bash

set -euo pipefail

ORG="AGENslab"
DESTINO="${1:-$ORG}"
API_URL="https://api.github.com"
VISIBILIDAD="all"
POR_PAGINA=100

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Error: falta el comando '$1'." >&2
    exit 1
  }
}

api_get() {
  local endpoint="$1"

  if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
    gh api "$endpoint"
  elif [ -n "${GITHUB_TOKEN:-}" ]; then
    curl -fsSL \
      -H "Accept: application/vnd.github+json" \
      -H "Authorization: Bearer $GITHUB_TOKEN" \
      "$API_URL$endpoint"
  else
    curl -fsSL \
      -H "Accept: application/vnd.github+json" \
      "$API_URL$endpoint"
  fi
}

clone_or_update_repo() {
  local repo_url="$1"
  local repo_name

  repo_name="$(basename "$repo_url" .git)"

  if [ -d "$repo_name/.git" ]; then
    echo "Actualizando $repo_name"
    git -C "$repo_name" pull --ff-only
  else
    echo "Clonando $repo_name"
    git clone "$repo_url"
  fi
}

require_cmd git
require_cmd curl
require_cmd jq

mkdir -p "$DESTINO"
cd "$DESTINO"

page=1
repos_en_pagina=0
repos_totales=0

while :; do
  respuesta="$(api_get "/orgs/$ORG/repos?type=$VISIBILIDAD&per_page=$POR_PAGINA&page=$page")"
  repos_en_pagina="$(jq 'length' <<<"$respuesta")"

  [ "$repos_en_pagina" -eq 0 ] && break

  while IFS= read -r repo_url; do
    [ -z "$repo_url" ] && continue
    clone_or_update_repo "$repo_url"
    repos_totales=$((repos_totales + 1))
  done < <(jq -r '.[].clone_url' <<<"$respuesta")

  [ "$repos_en_pagina" -lt "$POR_PAGINA" ] && break
  page=$((page + 1))
done

echo "Repos procesados: $repos_totales"

if ! command -v gh >/dev/null 2>&1 && [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "Nota: sin autenticacion solo se descargan repositorios publicos." >&2
  echo "Para incluir privados, usa 'gh auth login' o exporta GITHUB_TOKEN." >&2
fi
