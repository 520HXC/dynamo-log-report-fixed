import json
from pathlib import Path


REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "no report.json found"
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_report_schema():
    """Criterion 1: report.json has exactly the required keys and value types."""
    report = load_report()
    assert set(report) == {"total_requests", "unique_ips", "top_path"}
    assert type(report["total_requests"]) is int
    assert type(report["unique_ips"]) is int
    assert type(report["top_path"]) is str


def test_request_and_ip_counts():
    """Criterion 2: request and distinct client IP counts match access.log."""
    report = load_report()
    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3


def test_top_path():
    """Criterion 3: the most frequent request-target path is reported."""
    report = load_report()
    assert report["top_path"] == "/index.html"
