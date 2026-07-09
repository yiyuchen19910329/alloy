<!-- Replace <your-github-username> with your actual GitHub username, then this badge goes live. -->
![CI](https://github.com/<your-github-username>/insight-copilot/actions/workflows/ci.yml/badge.svg)

# ⚡ Insight Copilot

> A neuro-symbolic diagnostic layer for power-grid telemetry — turning noisy operational logs into auditable, root-cause insight.

**Insight Copilot** is the reference implementation of **ALLOY**, a neuro-symbolic framework that pairs the language ability of LLMs with deterministic, verifiable constraints. The target problem: in industrial grid operations, raw LLM output is not trustworthy enough for high-stakes decisions. ALLOY's thesis is that a probabilistic model becomes deployable only when a symbolic layer bounds and audits what it produces.

This repository is under **early, active development**. The section below states honestly what exists today versus what is planned — nothing here is claimed as finished unless it is.

---

## 📍 Status

| Area | State |
| --- | --- |
| Project infrastructure | ✅ **Built** |
| Data & modeling core | 🚧 **In progress** |
| ALLOY inference stack | 📋 **Planned** |
| EvoMerge research track | 📋 **Planned (separate repository)** |

**Built today**
- Reproducible environment: `uv`-managed dependencies, pinned Python 3.12, committed lockfile.
- Production-grade container: multi-stage `Dockerfile` (non-root, healthcheck), `docker-compose`.
- Quality gate: `ruff` (lint + format), `mypy` (strict), `pytest`, `pre-commit` hooks — all green locally.
- Continuous integration: GitHub Actions running lint, type-check, test, and a `docker build` gate.

**In progress**
- PyTorch modeling fundamentals and the deterministic data layer (synthetic telemetry → DuckDB → dbt).

**Planned** — see [Roadmap](#-roadmap). Everything below in *Design Goals* describes the intended architecture, not shipped features.

---

## 🎯 Design Goals (target architecture)

These are the design targets for ALLOY. They are **not yet implemented**; they define where the project is headed.

- **Neuro-symbolic constraints.** Fuse LLM reasoning with deterministic "hard" rules. Use classification heads and rule checks to bound outputs and suppress hallucination in a way that can be audited after the fact.
- **Domain adaptation.** Fine-tune on grid logs and engineering reports (e.g. ERCOT / IEEE datasets) so the model handles domain vocabulary — phasors, busbars, voltage surges — rather than generic text.
- **Inference engineering.** Target sub-second latency under event cascades via vLLM serving, 4-bit quantization, and KV-caching.
- **Semantic de-noising.** Aggregate large volumes of redundant alerts into a single root-cause diagnosis instead of forwarding raw noise ("alert fatigue").
- **Audit-ready output.** Every response is constrained by the symbolic layer, with the reasoning traceable — a prerequisite for regulated, high-stakes operations.

---

## 📂 Repository Structure

```text
insight-copilot/
├── src/
│   └── insight_copilot/     # application package
├── tests/                   # pytest suite
├── infra/
│   └── gcp/                 # Terraform (GCP, remote state) — scaffold
├── data/                    # datasets (gitignored)
├── notebooks/               # exploration
├── docs/                    # technical notes & specifications
├── Dockerfile               # multi-stage, non-root, healthcheck
├── docker-compose.yml
└── pyproject.toml           # single source of truth for deps & tooling
```

---

## 🚀 Getting Started

Requires [`uv`](https://docs.astral.sh/uv/) and Python 3.12 (uv can install it for you).

```bash
# 1. Clone
git clone https://github.com/<your-github-username>/insight-copilot.git
cd insight-copilot

# 2. Create the environment from the lockfile (bit-for-bit reproducible)
uv sync

# 3. Install the pre-commit quality hooks
uv run pre-commit install

# 4. Run the checks
uv run ruff check .
uv run mypy src
uv run pytest
```

The container image builds today (`docker build -t insight-copilot .`). The runnable service entrypoint (`src/main.py` + `/health`) is pending — see the roadmap.

---

## 🛠 Tech Stack

**Infrastructure (in use):** uv · Docker (multi-stage) · GitHub Actions · Terraform · GCP
**Quality (in use):** ruff · mypy · pytest · pre-commit
**Modeling (planned):** PyTorch · Hugging Face Transformers · vLLM · DuckDB · dbt

---

## 🗺 Roadmap

- [x] Reproducible infra, container, and CI/CD baseline
- [ ] Deterministic data layer: synthetic telemetry → DuckDB → dbt
- [ ] API entrypoint with `/health` and core inference route
- [ ] Domain fine-tuning on grid corpora
- [ ] Neuro-symbolic constraint layer (classification heads + rule checks)
- [ ] Inference optimization (quantization, KV-cache, vLLM serving)
- [ ] Terraform-provisioned deployment

*EvoMerge (evolutionary model merging) is a related research track developed in a separate repository; its integration with ALLOY is intentionally undecided pending experimental results.*

---

## 📄 License

TBD.