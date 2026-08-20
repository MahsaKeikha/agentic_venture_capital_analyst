from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXAMPLES_DIR = ROOT / "examples"
OUTPUT_DIR = ROOT / "outputs"

DISCLAIMER = (
    "Research and investment-process support only. Not personalized financial advice. "
    "Human verification and approval are required before circulation or action."
)

REQUIRED_FIELDS = [
    "company",
    "sector",
    "stage",
    "round",
    "product",
    "team",
    "traction",
    "business_model",
    "market",
]
