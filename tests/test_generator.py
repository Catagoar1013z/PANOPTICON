from data.generator import (
    generate_normal_event,
    generate_suspicious_event,
    generate_dataset,
)


def test_normal_event_has_expected_structure():
    event = generate_normal_event()

    assert "requests_count" in event
    assert "failed_logins" in event
    assert "duration" in event

    assert 15 <= event["requests_count"] <= 40
    assert 0 <= event["failed_logins"] <= 2
    assert 200 <= event["duration"] <= 600


def test_suspicious_event_has_expected_structure():
    event = generate_suspicious_event()

    assert "requests_count" in event
    assert "failed_logins" in event
    assert "duration" in event

    assert 150 <= event["requests_count"] <= 500
    assert 5 <= event["failed_logins"] <= 30
    assert 5 <= event["duration"] <= 60


def test_dataset_has_requested_size():
    dataset = generate_dataset(100)

    assert len(dataset) == 100

    for event in dataset:
        assert "requests_count" in event
        assert "failed_logins" in event
        assert "duration" in event
        assert "label" in event