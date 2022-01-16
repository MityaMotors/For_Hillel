import unittest
import HW_5

class TestHW5(unittest.TestCase):

    def test_01(self):
        """Check the string"""
        out = HW_5.check_homework()
        self.assertIsInstance(out, str)

    def test_02(self):
        """Check list and Capitalisation """
        stringa = "john marta james Morgan Adam Maria huang"
        out = HW_5.check_homework(stringa)
        self.assertIsInstance(out, list)
        names = " ".join(out)

        for i in out:
            self.assertEqual(i[0], i[0].upper(), f"get: {i}")


if __name__ == "__main__":
    unittest.main(verbosity=2)