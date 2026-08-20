from agents import (
    IntakeAnalyst, MarketAnalyst, ProductAnalyst, TeamAnalyst,
    TractionAnalyst, BusinessModelAnalyst, RiskAnalyst,
    DiligenceLead, InvestmentMemoWriter,
)
from memory import SharedMemory


class VCOrchestrator:
    def __init__(self, case):
        self.memory = SharedMemory(case=case)

    def run(self):
        case = self.memory.case
        self.memory.write("intake", IntakeAnalyst().run(case))
        self.memory.write("market", MarketAnalyst().run(case))
        self.memory.write("product", ProductAnalyst().run(case))
        self.memory.write("team", TeamAnalyst().run(case))
        self.memory.write("traction", TractionAnalyst().run(case))
        self.memory.write("business_model", BusinessModelAnalyst().run(case))

        self.memory.risks = RiskAnalyst().run(case, self.memory.analyses)
        self.memory.diligence_questions = DiligenceLead().run(case, self.memory.risks)
        self.memory.memo = InvestmentMemoWriter().run(
            case,
            self.memory.analyses,
            self.memory.risks,
            self.memory.diligence_questions,
        )
        return self.memory
