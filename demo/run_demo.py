import argparse
import json

from graphs.rca_graph import build_rca_graph
from utils.schemas import RCAState

# python demo/run_demo.py --alert_id ALERT_123

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alert_id", required=True)
    args = parser.parse_args()

    # v0 synthetic input
    

    graph = build_rca_graph()


    state = RCAState(
        alert_id=args.alert_id,
        anomaly="RPM dropped significantly",
        max_retries=2,
    )

    final_state = graph.invoke(state)

   # Print final RCA output
    print(
        json.dumps(
            {
                "alert_id": final_state["alert_id"],
                "report": final_state["report"],
                "confidence": final_state["confidence"],
                "hypotheses": final_state.get("hypotheses") or [],
                "evidence": final_state.get("evidence") or [],
            },
            indent=2,
            default=str,  # Handle any non-serializable objects
        )
    )


if __name__ == "__main__":
    main()
