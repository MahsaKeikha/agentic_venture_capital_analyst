from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class SharedMemory:
    case: Dict[str, Any]
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: list = field(default_factory=list)
    diligence_questions: list = field(default_factory=list)
    memo: str = ""

    def write(self, key: str, value: Any) -> None:
        self.analyses[key] = value

    def read(self, key: str, default=None) -> Any:
        return self.analyses.get(key, default)
