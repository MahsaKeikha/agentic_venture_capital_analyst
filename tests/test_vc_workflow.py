import json
from pathlib import Path

from agents import RiskAnalyst, TractionAnalyst
from orchestrator import VCOrchestrator


ROOT = Path(__file__).resolve().parents[1]


def load_case():
    return json.loads((ROOT / "examples" / "VC-1001.json").read_text(encoding="utf-8"))


def test_orchestrator_produces_all_core_analyses():
    memory = VCOrchestrator(load_case()).run()
    assert set(memory.analyses) == {
        "intake", "market", "product", "team", "traction", "business_model"
    }
    assert memory.risks
    assert memory.diligence_questions
    assert "Investment Memo Draft" in memory.memo


def test_missing_retention_is_not_invented():
    case = load_case()
    case["traction"]["retention"] = ""
    traction = TractionAnalyst().run(case)
    assert traction["retention"] == "Unknown / evidence required"

    risks = RiskAnalyst().run(case, {"traction": traction})
    assert any("Retention evidence is missing" in item["risk"] for item in risks)


def test_memo_contains_verification_language():
    memory = VCOrchestrator(load_case()).run()
    assert "Verify material claims" in memory.memo
    assert "capital commitment" in memory.memo
