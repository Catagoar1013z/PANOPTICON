import random


def generate_normal_event():
    """
    Genera un evento sintético que representa actividad normal.
    """

    return {
        "requests_count": random.randint(15, 40),
        "failed_logins": random.randint(0, 2),
        "duration": random.randint(200, 600)
    }


def generate_suspicious_event():
    """
    Genera un evento sintético que representa actividad sospechosa.
    """

    return {
        "requests_count": random.randint(150, 500),
        "failed_logins": random.randint(5, 30),
        "duration": random.randint(5, 60)
    }


def generate_dataset(size=100):
    """
    Genera un conjunto de eventos normales y sospechosos.
    """

    dataset = []

    for _ in range(size):
        if random.random() < 0.8:
            event = generate_normal_event()
            event["label"] = "normal"
        else:
            event = generate_suspicious_event()
            event["label"] = "suspicious"

        dataset.append(event)

    return dataset