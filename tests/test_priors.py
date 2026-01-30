from rca.priors import adjust_prior_with_memory, initialize_prior


def test_prior_shift_toward_memory():
    prior = initialize_prior()

    retrieved = [
        {"root_cause": "Weather"},
        {"root_cause": "Weather"},
        {"root_cause": "ExperimentChange"},
    ]

    adjusted = adjust_prior_with_memory(prior, retrieved, alpha=0.5)

    assert adjusted["Weather"] > prior["Weather"]
    assert adjusted["ExperimentChange"] > prior["ExperimentChange"]

