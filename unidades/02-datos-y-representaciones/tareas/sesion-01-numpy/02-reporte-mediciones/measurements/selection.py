"""Independent selections built from validated measurement matrices."""

import numpy as np

from measurements.processing import FloatArray, validate_shape


def select_warm_rounds(readings: FloatArray, threshold: float) -> FloatArray:
    """Return independent rows whose north-room temperature meets the threshold."""
    validate_shape(readings)
    if not np.isfinite(readings).all():
        raise ValueError("Selection requires finite readings")
    if not np.isfinite(threshold):
        raise ValueError("Threshold must be finite")
    return readings[readings[:, 0] >= threshold].copy()
