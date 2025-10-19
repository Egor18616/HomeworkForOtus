import math

class QuadraticEquation:
    def __init__(self):
        pass
    def slove(self, a: float, b: float, c: float, e: float = 1e-9):
        if any(math.isnan(arg) for arg in [a, b, c, e]):
            raise ValueError("Arguments cannot be equal to NaN.")
        if any(math.isinf(arg) for arg in [a, b, c, e]):
            raise ValueError("Arguments cannot be infinty.")
        if math.isclose(a, 0.0, rel_tol = e):
            raise ValueError("The coefficient 'a' cannot be equal to 0.")
        d = pow(b, 2) - 4 * a * c
        if d < 0:
            return []
        elif d > 0:
            return[-b+math.sqrt(d)/(2*a), -b-math.sqrt(d)/(2*a)]
        else:
            return [(-b/(2*a)), (-b/(2*a))]