from insight_copilot import health


def test_health() -> None:
    assert health() == {"status": "ok"}
