import numpy as np
import pytest

from measurements.selection import select_warm_rounds


def test_exact_threshold_selects_complete_rows() -> None:
    readings = np.array(
        [
            [26.0, 28.0, 24.0],
            [27.0, 29.0, 25.0],
            [28.0, 30.0, 26.0],
            [29.0, 31.0, 27.0],
        ]
    )
    selected = select_warm_rounds(readings, 27.0)
    np.testing.assert_array_equal(
        selected,
        [[27, 29, 25], [28, 30, 26], [29, 31, 27]],
    )


def test_no_match_keeps_three_columns() -> None:
    readings = np.array([[22.0, 24.0, 20.0]])
    selected = select_warm_rounds(readings, 100.0)
    assert selected.shape == (0, 3)


@pytest.mark.parametrize("threshold", [np.nan, np.inf, -np.inf])
def test_nonfinite_threshold_is_rejected(threshold: float) -> None:
    with pytest.raises(ValueError, match="Threshold"):
        select_warm_rounds(np.ones((2, 3)), threshold)


@pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
def test_nonfinite_reading_is_rejected(value: float) -> None:
    readings = np.array([[22.0, 24.0, 20.0], [value, 25.0, 21.0]])
    with pytest.raises(ValueError, match="finite readings"):
        select_warm_rounds(readings, 22.0)


@pytest.mark.parametrize(
    "readings",
    [np.array([22.0, 24.0, 20.0]), np.ones((2, 2)), np.empty((0, 3))],
)
def test_invalid_shape_is_rejected(readings: np.ndarray) -> None:
    with pytest.raises(ValueError):
        select_warm_rounds(readings, 22.0)


def test_result_can_change_without_modifying_input() -> None:
    readings = np.array([[22.0, 24.0, 20.0], [27.0, 29.0, 25.0]])
    original = readings.copy()
    selected = select_warm_rounds(readings, 27.0)
    selected[0, 0] = 100.0
    np.testing.assert_array_equal(readings, original)
    assert not np.shares_memory(selected, readings)
