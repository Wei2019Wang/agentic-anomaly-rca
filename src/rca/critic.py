from typing import List
from .schemas import Hypothesis, Evidence, CriticResult, CriticOutput


MIN_ACCEPTABLE_SCORE = 0.5


def critique_hypotheses(
    hypotheses: List[Hypothesis],
    evidence: List[Evidence],
) -> CriticOutput:
    results: List[CriticResult] = []

    evidence_sources = {e.source for e in evidence}

    for h in hypotheses:
        if h.cause in evidence_sources:
            revised_score = h.score
            supported = True
            reason = "Supporting evidence found"
        else:
            revised_score = h.score * 0.2
            supported = False
            reason = "No supporting evidence"

        results.append(
            CriticResult(
                hypothesis_id=h.cause,
                original_score=h.score,
                revised_score=revised_score,
                supported=supported,
                reason=reason,
            )
        )

    top_score = max(r.revised_score for r in results) if results else 0.0

    return CriticOutput(
        results=results,
        should_retry=top_score < MIN_ACCEPTABLE_SCORE,
    )
