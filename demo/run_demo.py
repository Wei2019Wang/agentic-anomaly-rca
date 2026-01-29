import argparse
import json
from rca.rca_agent import RCAAgent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alert_id", required=True)
    args = parser.parse_args()

    # v0 synthetic input
    anomalies = [2, 7]
    available_dims = ["country", "device", "supply_source"]

    agent = RCAAgent(available_dims)
    report = agent.explain(args.alert_id, anomalies)

    print(json.dumps(report.model_dump(), indent=2))

if __name__ == "__main__":
    main()
