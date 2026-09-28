import numpy as np
from fastapi import FastAPI

from ai.anomaly_model import PanopticonAnomalyModel
from detection.detector import detect_suspicious_activity
from detection.risk_engine import calculate_risk
from advisor.advisor import generate_security_advice

app = FastAPI(title="Panopticon")


# Create and train the Machine Learning model
ml_model = PanopticonAnomalyModel()

training_data = np.array([
    [20, 1, 300],
    [25, 0, 450],
    [18, 1, 280],
    [30, 2, 350],
    [22, 1, 400],
    [27, 0, 320],
    [24, 1, 380],
    [19, 0, 290],
    [26, 1, 360],
    [21, 2, 410],
])

ml_model.train(training_data)


@app.get("/")
def home():
    return {
        "project": "Panopticon",
        "status": "online",
        "message": "Cybersecurity monitoring system is running."
    }


@app.get("/analyze")
def analyze_activity(
    requests_count: int,
    failed_logins: int,
    duration: int
    ):
    rule_result = detect_suspicious_activity(
        requests_count=requests_count,
        failed_logins=failed_logins
    )

    ml_input = np.array([
    [requests_count, failed_logins, duration]
    ])

    ml_result = ml_model.predict(ml_input)
    
    risk_result = calculate_risk(
    rule_result=rule_result,
    ml_anomaly=bool(ml_result[0])
    )
    
    security_advice = generate_security_advice(
    rule_result=rule_result,
    ml_anomaly=bool(ml_result[0]),
    risk_result=risk_result
    )
    
    return {
    "rule_based_detection": rule_result,
    "machine_learning_anomaly": bool(ml_result[0]),
    "risk_assessment": risk_result,
    "security_advice": security_advice
    }