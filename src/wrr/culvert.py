import math

g = 9.80665  # m/s^2

def headwater_inlet_weir(Q: float, b: float, Cd: float = 1.6) -> float:
    """Weir-like inlet control for a sharp-edged rectangular opening.
    Returns head above soffit (approx.). Educational placeholder.
    Q = Cd * b * h^(3/2) * sqrt(2g)  -> solve for h
    """
    if Q <= 0 or b <= 0 or Cd <= 0:
        raise ValueError("Q, b, Cd must be positive")
    h = (Q / (Cd * b * (2*g) ** 0.5)) ** (2.0/3.0)
    return h

def headwater_inlet_orifice(Q: float, A: float, Cd: float = 0.62) -> float:
    """Orifice-like inlet control. Returns head above center of opening (approx.).
    Q = Cd * A * sqrt(2 g h) -> solve for h
    """
    if Q <= 0 or A <= 0 or Cd <= 0:
        raise ValueError("Q, A, Cd must be positive")
    h = (Q / (Cd * A)) ** 2 / (2*g)
    return h

def energy_grade_line_drop(V1: float, V2: float, K: float = 1.0) -> float:
    """Minor loss head h = K * V^2/(2g). If V2 given, use V2 for conservative estimate."""
    return K * max(V1, V2)**2 / (2*g)
