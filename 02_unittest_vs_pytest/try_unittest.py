import unittest
 
def square(n):
    return n*n
 
def cube(n):
    return n*n*n
 
class Test(unittest.TestCase):
    def test_square_2(self):
        self.assertEqual(square(2), 4)
 
    def test_square_3(self):
        self.assertEqual(square(3), 9)

    def test_cube(self):
        self.assertEqual(cube(2), 8)
