"""Example unit tests for the hydraulics functions.

These show how to verify code against things you know as a hydraulic
engineer: closure of equations, hand calculations, and physical limits.
Use the same idea to test YOUR functions - especially AI-generated ones.

Run with:  pytest  (or: make test)
"""

import math

import pytest

from wrr.standard_step import (
    discharge_rectangular,
    froude_rectangular,
    normal_depth_rectangular,
    specific_energy_rectangular,
)


def test_normal_depth_closes_manning_equation():
    # The depth returned by the solver must reproduce the input discharge
    # when plugged back into Manning's equation.
    Q, b, n, S0 = 25.0, 5.0, 0.035, 0.001
    yn = normal_depth_rectangular(Q, b, n, S0)
    assert discharge_rectangular(yn, b, n, S0) == pytest.approx(Q, rel=1e-6)


def test_normal_depth_against_hand_calculation():
    # Hand calc: b = 10 m, y = 2 m, n = 0.030, S0 = 0.0005
    # A = 20 m^2, P = 14 m, R = 10/7 m
    # Q = (1/n) * A * R^(2/3) * sqrt(S0)
    b, n, S0 = 10.0, 0.030, 0.0005
    y_expected = 2.0
    Q = (
        (1.0 / n)
        * (b * y_expected)
        * (b * y_expected / (b + 2 * y_expected)) ** (2 / 3)
        * math.sqrt(S0)
    )
    assert normal_depth_rectangular(Q, b, n, S0) == pytest.approx(y_expected, rel=1e-6)


def test_froude_is_one_at_critical_depth():
    # Critical depth in a rectangular channel: yc = (q^2 / g)^(1/3)
    Q, b = 25.0, 5.0
    q = Q / b
    yc = (q**2 / 9.80665) ** (1 / 3)
    assert froude_rectangular(yc, Q, b) == pytest.approx(1.0, rel=1e-6)


def test_specific_energy_exceeds_depth():
    # E = y + V^2/(2g) is always larger than the flow depth alone.
    y, Q, b = 1.5, 25.0, 5.0
    assert specific_energy_rectangular(y, Q, b) > y
