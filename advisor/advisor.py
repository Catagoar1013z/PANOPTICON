def generate_security_advice(rule_result, ml_anomaly, risk_result):
    """
    Genera una explicación y recomendaciones de seguridad
    basadas en las evidencias detectadas por PANOPTICON.
    """

    recommendations = []

    if rule_result["risk"] == "high":
        explanation = rule_result["reason"]

        recommendations.append(
            "Review authentication logs for repeated failed login attempts."
        )

        recommendations.append(
            "Temporarily restrict or rate-limit suspicious authentication activity."
        )

        recommendations.append(
            "Verify whether any unauthorized account access occurred."
        )

    elif ml_anomaly:
        explanation = (
            "Machine Learning detected an unusual activity pattern "
            "that differs from the normal behavior observed during training."
        )

        recommendations.append(
            "Review recent activity logs to identify what caused the anomaly."
        )

        recommendations.append(
            "Monitor the affected system for additional unusual behavior."
        )

    else:
        explanation = (
            "No significant suspicious activity was detected by the current "
            "detection methods."
        )

        recommendations.append(
            "Continue monitoring the system for changes in activity patterns."
        )

    return {
        "risk": risk_result["risk"],
        "explanation": explanation,
        "recommendations": recommendations
    }