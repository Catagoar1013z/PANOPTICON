from advisor.advisor import generate_security_advice


def test_advisor_generates_high_risk_recommendations():
    rule_result = {
        "suspicious": True,
        "risk": "high",
        "reason": "Multiple failed login attempts detected."
    }

    risk_result = {
        "risk": "high",
        "confidence": "high",
        "reason": "Rule-based detection and Machine Learning both identified suspicious activity."
    }

    result = generate_security_advice(
        rule_result=rule_result,
        ml_anomaly=True,
        risk_result=risk_result
    )

    assert result["risk"] == "high"
    assert len(result["recommendations"]) > 0
    assert "authentication logs" in result["recommendations"][0]


def test_advisor_generates_monitoring_advice_for_normal_activity():
    rule_result = {
        "suspicious": False,
        "risk": "low",
        "reason": "No suspicious activity detected."
    }

    risk_result = {
        "risk": "low",
        "confidence": "high",
        "reason": "No significant suspicious activity was detected."
    }

    result = generate_security_advice(
        rule_result=rule_result,
        ml_anomaly=False,
        risk_result=risk_result
    )

    assert result["risk"] == "low"
    assert len(result["recommendations"]) > 0
    