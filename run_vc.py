import argparse
import json
from config import DISCLAIMER, EXAMPLES_DIR, OUTPUT_DIR
from orchestrator import VCOrchestrator


def main():
    parser = argparse.ArgumentParser(description="F26 Agentic Venture Capital Analyst")
    parser.add_argument("--case", required=True, help="Case ID, for example VC-1001")
    parser.add_argument("--offline", action="store_true", help="Run deterministic offline workflow")
    parser.add_argument("--ship", action="store_true", help="Human approval for internal circulation")
    args = parser.parse_args()

    case_path = EXAMPLES_DIR / f"{args.case}.json"
    if not case_path.exists():
        raise SystemExit(f"Case not found: {case_path}")

    with case_path.open("r", encoding="utf-8") as handle:
        case = json.load(handle)

    memory = VCOrchestrator(case).run()
    status = "APPROVED FOR INTERNAL CIRCULATION" if args.ship else "DRAFT - HUMAN REVIEW REQUIRED"

    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / f"{args.case}_investment_memo.md"
    output_path.write_text(
        memory.memo + f"\n\n---\nStatus: **{status}**\n\n{DISCLAIMER}\n",
        encoding="utf-8",
    )

    print(memory.memo)
    print(f"\nSTATUS: {status}")
    print(DISCLAIMER)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
