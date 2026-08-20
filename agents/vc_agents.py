from typing import Any, Dict, List


def _unknown(value: Any) -> str:
    if value in (None, "", [], {}):
        return "Unknown / evidence required"
    return str(value)


class IntakeAnalyst:
    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "company": _unknown(case.get("company")),
            "sector": _unknown(case.get("sector")),
            "stage": _unknown(case.get("stage")),
            "round": _unknown(case.get("round")),
            "geography": _unknown(case.get("geography")),
            "source_count": len(case.get("evidence", [])),
        }


class MarketAnalyst:
    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        market = case.get("market", {})
        return {
            "target_customer": _unknown(market.get("target_customer")),
            "problem": _unknown(market.get("problem")),
            "market_size": _unknown(market.get("market_size")),
            "growth_drivers": market.get("growth_drivers", []) or ["Evidence required"],
            "competitors": market.get("competitors", []) or ["Evidence required"],
        }


class ProductAnalyst:
    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        product = case.get("product", {})
        return {
            "offering": _unknown(product.get("offering")),
            "differentiation": _unknown(product.get("differentiation")),
            "defensibility": _unknown(product.get("defensibility")),
            "technical_risks": product.get("technical_risks", []) or ["Technical diligence required"],
        }


class TeamAnalyst:
    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        team = case.get("team", {})
        return {
            "founders": team.get("founders", []) or ["Founder evidence required"],
            "strengths": team.get("strengths", []) or ["Evidence required"],
            "gaps": team.get("gaps", []) or ["Team gap analysis required"],
        }


class TractionAnalyst:
    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        traction = case.get("traction", {})
        return {
            "revenue": _unknown(traction.get("revenue")),
            "growth": _unknown(traction.get("growth")),
            "customers": _unknown(traction.get("customers")),
            "retention": _unknown(traction.get("retention")),
            "other_signals": traction.get("other_signals", []) or ["Evidence required"],
        }


class BusinessModelAnalyst:
    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        model = case.get("business_model", {})
        return {
            "pricing": _unknown(model.get("pricing")),
            "gtm": _unknown(model.get("gtm")),
            "gross_margin": _unknown(model.get("gross_margin")),
            "unit_economics": _unknown(model.get("unit_economics")),
        }


class RiskAnalyst:
    def run(self, case: Dict[str, Any], analyses: Dict[str, Any]) -> List[Dict[str, str]]:
        risks = []
        for item in case.get("known_risks", []):
            risks.append({"risk": str(item), "status": "Open", "owner": "Diligence"})
        traction = analyses.get("traction", {})
        if "Unknown" in str(traction.get("retention", "")):
            risks.append({"risk": "Retention evidence is missing", "status": "Open", "owner": "Traction"})
        if not risks:
            risks.append({"risk": "No validated risk register supplied", "status": "Open", "owner": "Diligence"})
        return risks


class DiligenceLead:
    def run(self, case: Dict[str, Any], risks: List[Dict[str, str]]) -> List[str]:
        questions = list(case.get("diligence_questions", []))
        for risk in risks:
            questions.append(f"What primary evidence resolves: {risk['risk']}?")
        return list(dict.fromkeys(questions))


class InvestmentMemoWriter:
    def run(self, case: Dict[str, Any], analyses: Dict[str, Any], risks, questions) -> str:
        company = case.get("company", "Unknown company")
        recommendation = case.get("preliminary_recommendation", "Continue diligence")
        lines = [
            f"# Investment Memo Draft: {company}",
            "",
            "## Preliminary recommendation",
            str(recommendation),
            "",
            "## Company and round",
            str(analyses.get("intake", {})),
            "",
            "## Market",
            str(analyses.get("market", {})),
            "",
            "## Product and defensibility",
            str(analyses.get("product", {})),
            "",
            "## Team",
            str(analyses.get("team", {})),
            "",
            "## Traction",
            str(analyses.get("traction", {})),
            "",
            "## Business model",
            str(analyses.get("business_model", {})),
            "",
            "## Key risks",
        ]
        lines.extend([f"- {r['risk']} [{r['status']}]" for r in risks])
        lines.extend(["", "## Priority diligence questions"])
        lines.extend([f"- {q}" for q in questions])
        lines.extend([
            "",
            "## Decision discipline",
            "This draft separates supplied evidence from unknowns. Verify material claims before an investment committee decision or capital commitment.",
        ])
        return "\n".join(lines)
