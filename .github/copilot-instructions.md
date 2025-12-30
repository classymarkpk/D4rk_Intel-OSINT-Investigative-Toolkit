<!-- AI onboarding for D4rk_Intel-OSINT-Investigative-Toolkit -->
# AI Onboarding — repository-specific guidance

Purpose: concise, actionable guidance to help an AI coding agent make safe, accurate edits in this repo.

**Big picture**
- The repo is a lightweight OSINT toolkit scaffold: small Python CLI stubs, tiny reusable helpers, and a couple of standalone scripts.
- Dataflow pattern: `cli/` CLIs call functions in `lib/`; `tools/` holds standalone utilities (Node, etc.); tests validate helpers.

**Key files to read first**
- [README.md](README.md) — high-level intent and resources.
- [cli/osint_scan.py](cli/osint_scan.py#L1) — example CLI stub that imports `lib.utils` and prints JSON-stub output.
- [lib/utils.py](lib/utils.py#L1) — minimal helpers (e.g., `log(msg)` prints `[osint-utils] ` prefix).
- [tools/harvester.js](tools/harvester.js#L1) — Node template for small harvesters.
- [tests/test_utils.py](tests/test_utils.py#L1) — unit test pattern (uses `unittest` to capture stdout).

**Developer workflows (concrete commands)**
- Run the CLI (from repo root):

  python cli/osint_scan.py --target example.com

- Run the unit test(s):

  python -m unittest tests/test_utils.py

  (`pytest -q` will also work if you add pytest to the environment, but the current tests use `unittest`.)

- Run the Node tool (from repo root):

  node tools/harvester.js


**Project-specific conventions & patterns**
- Keep utilities tiny and importable. Example: `lib/utils.py` provides `log(msg)` intended for reuse by CLI stubs.
- CLI stubs should be runnable with a single command and emit simple JSON or human-readable output (see `cli/osint_scan.py`).
- Tests are small, deterministic, and focus on helper behavior (capture stdout in `tests/test_utils.py`).
- Prefer minimal dependencies; if you add packages, include `requirements.txt` or `pyproject.toml` and update docs.

**Integration points & secrets**
- External APIs or OSINT services should be invoked from `cli/` or `tools/` and documented in `README.md` or `docs/README.md`.
- Never add secrets to the repo. If a change needs credentials, add a `.env.example` and document env var names and minimal setup.

**When changing or adding code**
- Preserve small boundary rules: put reusable helpers in `lib/`, CLI entrypoints in `cli/`, and language-specific quick tools in `tools/`.
- Add a one-line run example at the top of any new script and update the repo `README.md` or the relevant folder `README`.
- Avoid absolute paths (there may be a `.vscode/main.js` used for editor automation). If you modify it, keep its paths relative.
- Add focused unit tests (follow `tests/test_utils.py` style). Run tests locally before proposing changes.

**If you add CI/build or Docker**
- Include exact run commands and a short `README` snippet. Keep the initial CI minimal and focused on running the unit tests.

If anything in these guidance notes is unclear or you want more detail (CI examples, package layouts, or a starter `requirements.txt`), tell me which area to expand.
<!-- Copilot / AI agent instructions for D4rk_Intel-OSINT-Investigative-Toolkit -->
# Quick onboarding for AI coding agents

Purpose: give an AI practical, actionable context so it can make safe, focused changes in this repository.


  - [README.md](README.md): primary project summary, goals, and any usage notes. Use it as the authority for intended project purpose.
  - [.vscode/main.js](.vscode/main.js#L1-L11): contains editor automation/extension references (not app runtime). Note the explicit reference paths to a local VS Code extension in this file — avoid transforming these to absolute user paths when refactoring.

  - There is no existing app structure yet; if you add subsystems, follow a simple boundary pattern: `cli/` for command-line tools, `lib/` for reusable modules, `docs/` for design notes, and `tools/` for research scripts. Keep public-facing commands at repo root (e.g., `bin/` or `scripts/`).

  - No CI or build scripts are present. Before adding a toolchain, include a minimal `README` section with exact commands to run and test it.
  - For VS Code tasks, treat `.vscode/main.js` as editor automation only — do not assume it is executed by CI.

  - Keep filenames descriptive and language-appropriate (e.g., `osint-scan.py`, `harvester.js`).
  - Add a small README or header for each new top-level folder describing purpose and run steps.
  - Avoid hard-coded absolute user paths (the repo currently contains an absolute reference in `.vscode/main.js`); convert them to relative references or document why an absolute is necessary.

  - Document any external APIs, Docker images, or OSINT services you integrate. If you add credentials, insist on secrets/instructions to use environment variables and a `.env.example`.

  - If you add runnable code, include a one-line command to run it in the containing folder's README.
  - When creating or changing scripts referenced in `README.md`, update the `README.md` examples so a human can reproduce your steps.
  - Keep edits minimal and explicit: add files under clear folders, include a usage snippet, and add tests only if the change itself includes logic needing verification.

  - Editor helper: see [.vscode/main.js](.vscode/main.js#L1-L11) — it references a local extension path. If you modify or relocate this file, preserve or re-document those references.
  - High-level docs: see [README.md](README.md) for the repository's declared intent. Use it to infer naming and purpose for components you introduce.

If anything here is unclear or you want more detail in a specific area (tests, CI, packaging, or a suggested starter layout), tell me which area and I will expand the instructions and example files.
<!-- Copilot / AI agent instructions for D4rk_Intel-OSINT-Investigative-Toolkit -->
# Quick onboard for AI coding agents

Purpose: Give an AI the minimal, actionable context to make safe, focused changes.

- **Big picture**: This repo is a small OSINT/investigative-toolkit scaffold. Primary components are:
  - CLI utilities: [cli/osint_scan.py](cli/osint_scan.py#L1)
  - Reusable Python helpers: [lib/utils.py](lib/utils.py#L1)
  - Lightweight node helper: [tools/harvester.js](tools/harvester.js#L1)
  - Tests: [tests/test_utils.py](tests/test_utils.py#L1)
  Read these files to understand the intended dataflow: CLI calls helpers in `lib/`, tests validate helpers, JS tools are standalone scripts.

- **Files to inspect first**:
  - [README.md](README.md) — project intent and high-level notes.
  - [.vscode/main.js](.vscode/main.js#L1-L11) — editor automation only; do not hardcode absolute user paths.
  - [cli/osint_scan.py](cli/osint_scan.py#L1) and [lib/utils.py](lib/utils.py#L1) — core example of Python boundaries.

- **Project conventions**:
  - Folder roles: `cli/` for programs, `lib/` for reusable modules, `tools/` for one-off research scripts, `docs/` for design notes.
  - Add a README or one-line header for any new top-level folder explaining purpose and run command.
  - Avoid absolute paths (see `.vscode/main.js`) — prefer project-relative paths or environment variables.

- **Workflows & quick commands** (examples discovered in repo):
  - Run the main CLI script:

    python cli/osint_scan.py

  - Run tests (pytest is used in `tests/`):

    pytest -q

  - Run node scripts in `tools/` (add `package.json` if you add JS deps):

    node tools/harvester.js

  If you add Python dependencies, include a `requirements.txt` or `pyproject.toml` with exact install commands in the folder README.

- **Integration points**:
  - External OSINT services/APIs are expected to be documented and invoked from `cli/` or `tools/`. Place credentials in environment variables and provide a `.env.example` when introducing secrets.
  - If you add Docker, CI, or external tooling, include the exact commands and a minimal `README.md` describing how to run them locally.

- **Code-change guidance (practical rules)**:
  - If a referenced module is missing, create a minimal stub under `lib/` and call it out explicitly in the PR description.
  - Keep edits minimal and focused. When adding runnable code, include a single-line run example at the top of the file or in the folder README.
  - Add or update tests in `tests/` that target the changed behavior; keep test scope small and deterministic.

- **Repository-specific examples**:
  - Editor helper: see [.vscode/main.js](.vscode/main.js#L1-L11) — preserve relative paths if refactoring.
  - Python helper pattern: `cli/osint_scan.py` imports functions from `lib/` — follow the same separation for new commands.

If anything is unclear or you want a different level of detail (e.g., CI setup, packaging, starter layout), tell me which area and I will expand the instructions.
