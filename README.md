# Agentic Venture Capital Analyst (F26)

A multi-agent workflow for **venture capital screening and startup due diligence**. The system turns a structured startup case into an investment memo draft with market, team, product, traction, business model, risk, diligence, and recommendation sections, followed by a human approval gate.

This project is for research, education, and investment-process support. It is **not personalized financial advice**, does not replace professional due diligence, and does not make autonomous investment decisions.

## Quick start

```bash
python3 run_vc.py --case VC-1001 --offline
```

Use `--ship` only after a human reviewer has checked the memo and supporting evidence.

## Agents

| Agent | Role |
|---|---|
| Intake Analyst | Normalizes company, round, sector, geography, and evidence |
| Market Analyst | Reviews market size, growth drivers, category dynamics, and competition |
| Product Analyst | Reviews product differentiation, defensibility, roadmap, and technical risk |
| Team Analyst | Reviews founder-market fit, leadership gaps, and hiring risk |
| Traction Analyst | Reviews revenue, growth, retention, pilots, customers, and evidence quality |
| Business Model Analyst | Reviews pricing, unit economics, GTM, margins, and scalability |
| Risk Analyst | Produces a structured risk register and identifies missing evidence |
| Diligence Lead | Builds prioritized diligence questions and verification requests |
| Investment Memo Writer | Synthesizes the analysis into a concise IC-style memo |
| Gatekeeper | Prevents circulation until a human explicitly approves with `--ship` |

## Workflow

1. Load a startup case from `examples/<case>.json`.
2. Run specialized analyses against the same evidence package.
3. Store intermediate outputs in shared memory.
4. Build a diligence queue and risk register.
5. Produce an investment memo draft.
6. Apply the human circulation gate.

## Design principles

- Offline-first and deterministic demo mode
- Evidence-aware: missing facts are labeled as unknown rather than invented
- Human-in-the-loop before any investment recommendation is circulated
- No autonomous transaction, commitment, term-sheet issuance, or capital deployment
- Clear separation between facts, assumptions, risks, and recommendations

## Repository structure

```text
README.md
config.py
memory.py
orchestrator.py
run_vc.py
agents/
  __init__.py
  vc_agents.py
examples/
  VC-1001.json
```

## Human gate

Without `--ship`, the final status is `DRAFT - HUMAN REVIEW REQUIRED`.

With `--ship`, the status becomes `APPROVED FOR INTERNAL CIRCULATION`, but only after the user explicitly invokes the flag.

## Responsible use

Investment decisions involve uncertainty and material risk. Validate claims independently, use qualified legal, financial, tax, technical, and domain experts where appropriate, and never treat model output as sufficient evidence for deploying capital.
