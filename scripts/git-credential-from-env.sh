#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOKEN="${GITHUB_TOKEN:-}"

if [[ -z "$TOKEN" && -f "$ROOT_DIR/.env" ]]; then
  while IFS='=' read -r key value; do
    [[ -z "${key:-}" ]] && continue
    [[ "$key" =~ ^[[:space:]]*# ]] && continue
    if [[ "$key" == "GITHUB_TOKEN" ]]; then
      TOKEN="${value%$'\r'}"
      TOKEN="${TOKEN%\"}"
      TOKEN="${TOKEN#\"}"
      TOKEN="${TOKEN%\'}"
      TOKEN="${TOKEN#\'}"
      break
    fi
  done < "$ROOT_DIR/.env"
fi

if [[ -z "$TOKEN" ]]; then
  exit 0
fi

while IFS='=' read -r key value; do
  case "$key" in
    protocol) protocol="$value" ;;
    host) host="$value" ;;
  esac
done

if [[ "${protocol:-}" != "https" || "${host:-}" != "github.com" ]]; then
  exit 0
fi

printf 'username=x-access-token\n'
printf 'password=%s\n' "$TOKEN"

