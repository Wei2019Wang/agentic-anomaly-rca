from rca.schemas import RCAExplanation, RCAReport


class RCAAgent:
    def __init__(self, available_dims):
        self.available_dims = available_dims
    
    def explain(self, alert_id: str, anomalies: list[int]) -> RCAReport:
        explanations = []

        for anomaly_id in anomalies:
            dims = self.available_dims[:2]

            explanation = (
                f"Anomaly at index {anomaly_id} is correlated with shifts "
                f"in {dims[0]} and {dims[1]}"
            )

            explanations.append(
                RCAExplanation(
                    anomaly_id=anomaly_id,
                    dimensions=dims,
                    explanation=explanation,
                    confidence=0.6
                )
            )

        return RCAReport(alert_id=alert_id, explanations=explanations)
    
