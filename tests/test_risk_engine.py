from detection.risk_engine import calculate_risk


def test_high_risk_when_rules_and_ml_detect_threat():
    rule_result = {
        "suspicious": True,
        "risk": "high",
        "reason": "Multiple failed login attempts detected."
    }

    result = calculate_risk(
        rule_result=rule_result,
        ml_anomaly=True
    )

    assert result["risk"] == "high"
    assert result["confidence"] == "high"


def test_low_risk_when_no_threat_is_detected():
    rule_result = {
        "suspicious": False,
        "risk": "low",
        "reason": "No suspicious activity detected."
    }

    result = calculate_risk(
        rule_result=rule_result,
        ml_anomaly=False
    )

    assert result["risk"] == "low"
    assert result["confidence"] == "high"