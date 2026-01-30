from incident_memory.retrieve import retrieve_similar_incidents

def test_retrieve_similar_incidents():
    results = retrieve_similar_incidents(
        "advertiser paused spend",
        top_k=2,
    )

    assert len(results) == 2
    assert "incident_id" in results[0]
    assert "root_cause" in results[0]
