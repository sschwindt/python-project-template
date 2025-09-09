import math
import pytest
from src.hydraulics.standard_step import normal_depth_rectangular, froude_rectangular

def test_normal_depth_rectangular_smoke():
    yn = normal_depth_rectangular(Q=25.0, b=5.0, n=0.03, S0=0.001)
    assert yn > 0.0
    # sanity: subcritical for these parameters
    Fr = froude_rectangular(yn, 25.0, 5.0)
    assert Fr < 1.0

@pytest.mark.heavy
def test_units_sensitivity():
    yn1 = normal_depth_rectangular(Q=10.0, b=3.0, n=0.035, S0=0.002)
    yn2 = normal_depth_rectangular(Q=10.0, b=3.0, n=0.035, S0=0.002, y0=yn1*1.2)
    assert abs(yn1 - yn2) < 1e-6
