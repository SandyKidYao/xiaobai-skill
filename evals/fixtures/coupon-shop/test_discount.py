import pytest

from discount import apply_coupon


def test_above_threshold():
    assert apply_coupon(250, "FULL200_30") == 220


def test_below_threshold():
    assert apply_coupon(150, "FULL200_30") == 150


def test_unknown_coupon():
    with pytest.raises(ValueError):
        apply_coupon(100, "NOPE")
