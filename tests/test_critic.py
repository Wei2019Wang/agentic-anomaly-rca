import pytest

from rca.critic import critique_hypotheses
from utils.schemas import Hypothesis, Evidence


def test_supported_hypothesis_not_penalized():
    """
    Hypothesis should keep its score if matching evidence exists.
    """
    hypotheses = [
        Hypothesis(
            cause="Weather",
            prior=0.3,
            score=0.7,
            required_evidence=[]
        )
    ]

    evidence = [
        Evidence(
            source="Weather",
            output={"storm": True},
            citation="weather.get_events(region=US)",
            success=True,
        )
    ]

    output = critique_hypotheses(hypotheses, evidence)

    assert len(output.results) == 1
    result = output.results[0]

    assert result.supported is True
    assert result.original_score == 0.7
    assert result.revised_score == 0.7
    assert output.should_retry is False


def test_unsupported_hypothesis_penalized():
    """
    Hypothesis without evidence should be penalized and trigger retry.
    """
    hypotheses = [
        Hypothesis(
            cause="InfraLatency",
            prior=0.4,
            score=0.8,
            required_evidence=[]
        )
    ]

    evidence = []  # no evidence at all

    output = critique_hypotheses(hypotheses, evidence)

    assert len(output.results) == 1
    result = output.results[0]

    assert result.supported is False
    assert result.original_score == 0.8
    assert result.revised_score < 0.8
    assert output.should_retry is True


def test_mixed_support_hypotheses():
    """
    Only hypotheses with matching evidence should remain strong.
    """
    hypotheses = [
        Hypothesis(
            cause="Weather",
            prior=0.2,
            score=0.6,
            required_evidence=[]
        ),
        Hypothesis(
            cause="ExperimentChange",
            prior=0.5,
            score=0.9,
            required_evidence=[]
        ),
    ]

    evidence = [
        Evidence(
            source="ExperimentChange",
            output={"rollback": True},
            citation="experiments.get_changes(window=24h)",
            success=True,
        )
    ]

    output = critique_hypotheses(hypotheses, evidence)

    scores = {
        r.hypothesis_id: r.revised_score
        for r in output.results
    }

    assert scores["ExperimentChange"] == 0.9
    assert scores["Weather"] < 0.6
    assert output.should_retry is False

