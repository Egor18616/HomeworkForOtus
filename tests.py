import unittest
from quadratic_equation import QuadraticEquation

class TestQuadraticEquation(unittest.TestCase):
    def setUp(self):
        self.quadraticEquation = QuadraticEquation()
    def test_the_equation_has_no_roots(self):
        self.assertEqual(self.quadraticEquation.slove(1, 0, 1), [])
    def test_the_equation_has_two_roots(self):
        self.assertEqual(self.quadraticEquation.slove(1, 0, -1), [1.0, -1.0])
    def test_the_equation_has_one_root(self):
        self.assertEqual(self.quadraticEquation.slove(1, 2, 1), [-1.0, -1.0])
    def test_the_equation_where_a_is_zero(self):
        with self.assertRaises(ValueError) as obj_error:
            self.quadraticEquation.slove(0,1,1)
        self.assertEquals("The coefficient 'a' cannot be equal to 0.", str(obj_error.exception))
    def test_the_equation_where_argument_a_is_nan(self):
        with self.assertRaises(ValueError) as obj_error:
            self.quadraticEquation.slove(float('nan'),1,1)
        self.assertEquals("Arguments cannot be equal to NaN.", str(obj_error.exception))
    def test_the_equation_where_argument_b_is_nan(self):
        with self.assertRaises(ValueError) as obj_error:
            self.quadraticEquation.slove(1, float('nan'),1)
        self.assertEquals("Arguments cannot be equal to NaN.", str(obj_error.exception))
    def test_the_equation_where_argument_c_is_nan(self):
        with self.assertRaises(ValueError) as obj_error:
            self.quadraticEquation.slove(1, 1, float('nan'))
        self.assertEquals("Arguments cannot be equal to NaN.", str(obj_error.exception))
    def test_the_equation_where_argument_a_is_inf(self):
        with self.assertRaises(ValueError) as obj_error:
            self.quadraticEquation.slove(float('inf'),1,1)
        self.assertEquals("Arguments cannot be infinty.", str(obj_error.exception))
    def test_the_equation_where_argument_b_is_inf(self):
        with self.assertRaises(ValueError) as obj_error:
            self.quadraticEquation.slove(1,float('inf'),1)
        self.assertEquals("Arguments cannot be infinty.", str(obj_error.exception))
    def test_the_equation_where_argument_c_is_inf(self):
        with self.assertRaises(ValueError) as obj_error:
            self.quadraticEquation.slove(1,1,float('inf'))
        self.assertEquals("Arguments cannot be infinty.", str(obj_error.exception))

if __name__ == "__main__":
    unittest.main()