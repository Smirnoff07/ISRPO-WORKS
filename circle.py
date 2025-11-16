import math

def area(r):
    """Принимает радиус круга r, возвращает его площадь."""
    return math.pi * r * r

def perimeter(r):
    """Принимает радиус круга r, возвращает его длину окружности."""
    return 2 * math.pi * r


import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_common_area(self):
        res = area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected, places = 7)

    def test_common_perimeter(self):
        res = perimeter(10)
        expected = 2 * math.pi * 10
        self.assertAlmostEqual(res, expected, places = 7)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
