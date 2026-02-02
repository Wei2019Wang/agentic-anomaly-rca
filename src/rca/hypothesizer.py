from typing import List
from utils.schemas import Hypothesis


def generate_hypotheses(
    priors: dict[str, float]
) -> List[Hypothesis]:
    hypotheses = []

    for cause, prior in priors.items():
        hypotheses.append(
            Hypothesis(
                cause=cause,
                prior=prior,
                score=prior,
                required_evidence=[
                    f"metrics_slice:{cause}",
                    f"external_signal:{cause}",
                ],
            )
        )

    return hypotheses