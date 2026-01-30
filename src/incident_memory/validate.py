import json
from pathlib import Path

from memory.categories import INCIDENT_CATEGORIES


def validate_incidents(incidents_path: str) -> None:
    incidents_path = Path(incidents_path)
    print("Validating incidents...")
    with incidents_path.open() as f:
        for i, line in enumerate(f, start=1):
            incident = json.loads(line)
            root_cause = incident["root_cause"]

            if root_cause not in INCIDENT_CATEGORIES:
                raise ValueError(
                    f"Invalid root_cause '{root_cause}' "
                    f"on line {i}. Must be one of {INCIDENT_CATEGORIES}"
                )
