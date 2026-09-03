#!/usr/bin/env bash
# Checks do projeto AuctaPay Concilia (tier 3) — adaptado pelo init-repo (item 8).
# O harness compara o motor legado com a referência EXTERNA baseline_expected.json;
# o resultado esperado nunca é recalculado pelo código sob teste.
set -euo pipefail

echo "== ACC-001: baseline de caracterização do legado =="
python3 tests/regression/baseline_check.py
