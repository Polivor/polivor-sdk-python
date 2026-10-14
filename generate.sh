#!/usr/bin/env bash
# Regenerates polivor/generated from the OpenAPI file. The hand-written files in polivor/ are never touched.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
OPENAPI_FILE="${OPENAPI_FILE:-openapi/polivor.yaml}"
WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT
openapi-python-client generate --path "$OPENAPI_FILE" --config generator-config.yaml --output-path "$WORK_DIR/out" --overwrite
rm -rf polivor/generated
cp -R "$WORK_DIR/out/generated" polivor/generated
