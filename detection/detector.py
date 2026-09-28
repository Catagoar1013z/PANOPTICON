def detect_suspicious_activity(requests_count, failed_logins):
    """
    Analiza una actividad básica y determina si parece sospechosa.
    """

    if failed_logins >= 5:
        return {
            "suspicious": True,
            "risk": "high",
            "reason": "Multiple failed login attempts detected."
        }

    if requests_count >= 100:
        return {
            "suspicious": True,
            "risk": "medium",
            "reason": "Unusually high number of requests detected."
        }

    return {
        "suspicious": False,
        "risk": "low",
        "reason": "No suspicious activity detected."
    }