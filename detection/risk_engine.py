def calculate_risk(rule_result, ml_anomaly):
    """
    Combina la detección basada en reglas y Machine Learning
    para determinar el nivel de riesgo.
    """

    if rule_result["risk"] == "high" and ml_anomaly:
        return {
            "risk": "high",
            "confidence": "high",
            "reason": "Rule-based detection and Machine Learning both identified suspicious activity."
        }

    if rule_result["suspicious"] or ml_anomaly:
        return {
            "risk": "medium",
            "confidence": "medium",
            "reason": "At least one detection method identified unusual activity."
        }

    return {
        "risk": "low",
        "confidence": "high",
        "reason": "No significant suspicious activity was detected."
    }