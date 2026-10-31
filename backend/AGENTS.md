# Backend agent instructions

Read `backend/README.md`, `reports/evaluation/research_gate.json`, `reports/evaluation/claim_boundaries.json`, and `reports/audit/model_manifest.csv` before changing inference or research claims.

- Never invent live data, metrics, estimates, feature definitions or model readiness.
- Maintain one-step-ahead, lag-based, past-only semantics. Never use test-set outcomes to choose champion or tune thresholds.
- Train-only peak threshold and chronological splits are core research invariants.
- Units differ among steel, electricity and appliances. Never conflate them.
- Do not deserialize untrusted joblib data.
- Maintain routes, tests, safe response schemas, and bilingual documentation parity with `docs/id`.
- Never make an endpoint pretend it can forecast from an arbitrary timestamp or an underspecified 21-value vector.
