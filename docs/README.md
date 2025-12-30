# Docs for D4rk_Intel-OSINT-Investigative-Toolkit

This folder holds repository-level design notes, run steps, and short examples.

- `cli/` — place command-line utilities here. Example: `cli/osint_scan.py` is a tiny starter.
- `lib/` — reusable Python modules and helpers (keep them minimal and importable).
- `tools/` — small scripts in other languages (Node, PowerShell) used for quick data collection.

Quick run examples

Python CLI (from repo root):

```powershell
python ./cli/osint_scan.py --target example.com
```

Node tool (from repo root):

```powershell
node ./tools/harvester.js
```
