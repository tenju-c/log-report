import json
from pathlib import Path


def load_report():
    """Success criterion 1: The agent creates a JSON report at /app/report.json."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json was not created"

    with report_path.open() as f:
        return json.load(f)


def test_request_count():
    """Success criterion 2: The report contains the correct total number of requests."""
    report = load_report()

    assert report["total_requests"] == 6, (
        "total_requests should equal the number of requests in access.log"
    )


def test_unique_clients():
    """Success criterion 3: The report contains the correct set of unique client IPs."""
    report = load_report()

    assert sorted(report["unique_clients"]) == sorted(
        [
            "192.168.0.1",
            "192.168.0.2",
            "10.0.0.5",
        ]
    )


def test_popular_pages():
    """Success criterion 4: The report contains the correct page request counts."""
    report = load_report()

    assert report["popular_pages"] == {
        "/index.html": 3,
        "/about.html": 2,
        "/api/login": 1,
    }
