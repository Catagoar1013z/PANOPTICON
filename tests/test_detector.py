from detection.detector import detect_suspicious_activity


def test_multiple_failed_logins():
    result = detect_suspicious_activity(
        requests_count=20,
        failed_logins=5
    )

    assert result["suspicious"] is True
    assert result["risk"] == "high"


def test_normal_activity():
    result = detect_suspicious_activity(
        requests_count=20,
        failed_logins=1
    )

    assert result["suspicious"] is False
    assert result["risk"] == "low"