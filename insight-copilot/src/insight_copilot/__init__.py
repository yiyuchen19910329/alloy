# src/insight_copilot/__init__.py
def health() -> dict[str, str]:
    """回傳服務健康狀態。"""
    return {"status": "ok"}
