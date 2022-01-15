import os
import unittest
from homework_9a import arithmetic
from logger import log


class MyTests(unittest.TestCase):

    def test_sum(self):
        """Test for sum"""
        t1 = 1
        t2 = 3
        exp = 4
        out = arithmetic(t1, t2, "+")
        self.assertEqual(out, exp, "Something went wrong")
        log.debug("Check the sum with correct result")

    @unittest.expectedFailure
    def test_sum_wrong(self):
        """The wrong sum is expected"""
        t1 = 1
        t2 = 3
        exp = 3
        out = arithmetic(t1, t2, "+")
        self.assertEqual(out, exp, "Something went wrong")


    @unittest.skipIf(os.name != "nt", "Test_02 currently skips")
    def test_diff(self):
        """Skip Test for diff if not a WindowsOS"""
        t1 = 4
        t2 = 3
        exp = 1
        out = arithmetic(t1, t2, "-")
        self.assertEqual(out, exp, "Something went wrong")

    def test_mult(self):
        """Test for mult"""
        t1 = 1
        t2 = 3
        exp = 3
        out = arithmetic(t1, t2, "*")
        self.assertEqual(out, exp, "Something went wrong")
        log.error("Check the log_error")

    def test_div(self):
        """Test for div"""
        t1 = 3
        t2 = 3
        exp = 1
        out = arithmetic(t1, t2, "/")
        self.assertEqual(out, exp, "Something went wrong")
        log.info("Ready to test?")

    def test_div_v2(self):
        """Test for div"""
        t1 = 99
        t2 = 11
        exp = 9
        out = arithmetic(t1, t2, "/")
        self.assertEqual(out, exp, "Something went wrong")
        log.warning("WARNING")

    @unittest.skip("Division by ZERO")
    def test_div_zero(self):
        """Test for div zero"""
        out = arithmetic(2, 0, "/")
        self.assertFalse(out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
