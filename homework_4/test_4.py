import unittest
import homework_4n


class Check(unittest.TestCase):

    def test_01(self):
        """Check of the first string"""
        out = homework_4n.escape_table(r'\a', 'Bell (alert)')
        exp = "|\t\\a	|	Bell (alert)			|"
        self.assertEqual(out, exp, "Test_01 is incorrect")

    def test_02(self):
        """Check the second string"""
        out = homework_4n.escape_table(r'\b', 'Backspace')
        exp = "|\t\\b	|	Backspace				|"
        self.assertEqual(out, exp, "Test_02 is incorrect")

    def test_03(self):
        """Check the third string"""
        out = homework_4n.escape_table(r'\n', 'New line')
        exp = "|\t\\n	|	New line				|"
        self.assertEqual(out, exp, "Test_03 is incorrect")

    def test_04(self):
        """Check the fourth string"""
        out = homework_4n.escape_table(r'\t', 'Horizontal tab')
        exp = "|\t\\t	|	Horizontal tab			|"
        self.assertEqual(out, exp, "Test_04 is incorrect")

    def test_05(self):
        """Check the fifth string"""
        out = homework_4n.escape_table(r'\\', 'Backslach \\')
        exp = "|\t\\\\	|	Backslach \				|"
        self.assertEqual(out, exp, "Test_05 is incorrect")

    def test_06(self):
        """Check the sixth string"""
        out = homework_4n.escape_table(r'\'', 'Single quotation mark \'')
        exp = "|\t\\\'	|	Single quotation mark '	|"
        self.assertEqual(out, exp, "Test_06 is incorrect")

    def test_of_the_length_01(self):
        """Check the length of the first string"""
        out = homework_4n.escape_table(r'\a', 'Bell (alert)')
        self.assertEqual(len(out), 23, "the length is unappropriated")

    def test_of_the_length_02(self):
        """Check the length of the second string"""
        out = homework_4n.escape_table(r'\b', 'Backspace')
        self.assertEqual(len(out), 21, "the length is unappropriated")

    def test_of_the_length_03(self):
        """Check the length of the third string"""
        out = homework_4n.escape_table(r'\n', 'New line')
        self.assertEqual(len(out), 20, "the length is unappropriated")

    def test_of_the_length_04(self):
        """Check the length of the fourth string"""
        out = homework_4n.escape_table(r'\t', 'Horizontal tab')
        self.assertEqual(len(out), 25, "the length is unappropriated")

    def test_of_the_length_05(self):
        """Check the length of the fifth string"""
        out = homework_4n.escape_table(r'\\', 'Backslach \\')
        self.assertEqual(len(out), 23, "the length is unappropriated")

    def test_of_the_length_06(self):
        """Check the length of the sixth string"""
        out = homework_4n.escape_table(r'\"', 'Double quotation mark \"')
        self.assertEqual(len(out), 32, "the length is unappropriated")

    def test_of_the_length_07(self):
        """Check the length of the seventh string"""
        out = homework_4n.escape_table(r'\'', 'Single quotation mark \'')
        self.assertEqual(len(out), 32, "the length is unappropriated")

    def test_number_tab_07(self):
        """Compare the tabs 7 string"""
        out = homework_4n.escape_table(r'\'', 'Single quotation mark \'')
        exp = out.count("\t")
        self.assertEqual(4, exp, "the length is unappropriated")

    def test_number_tab_06(self):
        """Compare the tabs 6 string"""
        out = homework_4n.escape_table(r'\"', 'Double quotation mark \"')
        exp = out.count("\t")
        self.assertEqual(4, exp, "the length is unappropriated")

    def test_number_tab_05(self):
        """Compare the tabs 5 string"""
        out = homework_4n.escape_table(r'\\', 'Backslach \\')
        exp = out.count("\t")
        self.assertEqual(7, exp, "the length is unappropriated")

    def test_number_tab_04(self):
        """Compare the tabs 4 string"""
        out = homework_4n.escape_table(r'\t', 'Horizontal tab')
        exp = out.count("\t")
        self.assertEqual(6, exp, "the length is unappropriated")

    def test_number_tab_03(self):
        """Compare the tabs 3 string"""
        out = homework_4n.escape_table(r'\n', 'New line')
        exp = out.count("\t")
        self.assertEqual(7, exp, "the length is unappropriated")

    def test_number_tab_02(self):
        """Compare the tabs 2 string"""
        out = homework_4n.escape_table(r'\b', 'Backspace')
        exp = out.count("\t")
        self.assertEqual(7, exp, "the length is unappropriated")

    def test_number_tab_01(self):
        """Compare the tabs 1 string"""
        out = homework_4n.escape_table(r'\a', 'Bell (alert)')
        exp = out.count("\t")
        self.assertEqual(6, exp, "the length is unappropriated")


if __name__ == "main":
    unittest.main(verbosity=2)
