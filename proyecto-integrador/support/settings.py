"""Read and validate the embedding configuration."""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import cast


@dataclass(frozen=True)
class Settings:
    model_name: str
    batch_size: int
    device: str


def load_settings(path: Path) -> Settings:
    """Load a small JSON configuration and reject ambiguous values."""
    raw = cast(object, json.loads(path.read_text(encoding="utf-8")))
    if not isinstance(raw, dict):
        raise ValueError("Configuration must be a JSON object")

    model_name = raw.get("model_name")
    batch_size = raw.get("batch_size")
    device = raw.get("device")
    if not isinstance(model_name, str) or not model_name.strip():
        raise ValueError("model_name must be a nonempty string")
    if (
        isinstance(batch_size, bool)
        or not isinstance(batch_size, int)
        or batch_size <= 0
    ):
        raise ValueError("batch_size must be a positive integer")
    if not isinstance(device, str) or not device.strip():
        raise ValueError("device must be a nonempty string")
    return Settings(model_name.strip(), batch_size, device.strip())
