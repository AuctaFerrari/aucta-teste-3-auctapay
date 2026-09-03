#!/usr/bin/env python3
"""Harness de caracterização da baseline do legado (ACC-001).

Executa o motor legado (legacy/reconcile.py) sobre a massa sintética e compara
com a referência EXTERNA legacy/baseline/baseline_expected.json — o resultado
esperado nunca é recalculado pelo código sob teste (blueprint 2.5).

A baseline preserva o comportamento OBSERVADO, inclusive o defeito candidato
T002 (known_concern). Reproduzir a baseline NÃO aprova regra de negócio.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEGACY = ROOT / "legacy"

sys.path.insert(0, str(LEGACY))
from reconcile import reconcile_records  # noqa: E402  (código legado sob caracterização)

def main() -> int:
    titles = json.loads((LEGACY / "synthetic" / "titles.json").read_text(encoding="utf-8"))
    payments = json.loads((LEGACY / "synthetic" / "payments.json").read_text(encoding="utf-8"))
    reference = json.loads((LEGACY / "baseline" / "baseline_expected.json").read_text(encoding="utf-8"))

    expected = reference["expected_legacy_output"]
    observed = [
        {k: row[k] for k in ("title_id", "payment_id", "status")}
        for row in reconcile_records(titles, payments)
    ]

    ok = observed == expected
    print(f"Baseline legado ({reference['version']}): {'OK — 3/3 casos reproduzidos' if ok else 'FALHA'}")
    if not ok:
        print("Esperado:", json.dumps(expected, ensure_ascii=False))
        print("Observado:", json.dumps(observed, ensure_ascii=False))
        return 1
    if reference.get("evidence_status") != "observed_not_approved":
        print("AVISO: evidence_status da baseline mudou — revisar TRUTHS antes de prosseguir.")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
