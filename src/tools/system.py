# src/tools/system.py

from typing import Dict, Any


def get_latency(service: str | None = None) -> Dict[str, Any]:
    """
    Mock system latency lookup.
    """
    return {
        "service": service or "ads",
        "latency_p50_ms": 45,
        "latency_p95_ms": 120,
        "latency_p99_ms": 250,
        "status": "normal",
        "anomaly_detected": False,
    }


def get_pipeline_status() -> Dict[str, Any]:
    """
    Mock data pipeline status lookup.
    """
    return {
        "pipeline_id": "data_ingestion",
        "status": "healthy",
        "last_success": "2024-01-15T10:30:00Z",
        "last_failure": None,
        "throughput_events_per_sec": 1000,
        "error_rate": 0.001,
    }
