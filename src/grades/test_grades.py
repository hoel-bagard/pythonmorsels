import unittest


from grades import percent_to_grade


class PercentToGradeTests(unittest.TestCase):
    """Tests for percent_to_grade."""

    def test_a_grades(self):
        self.assertEqual(percent_to_grade(95), "A")
        self.assertEqual(percent_to_grade(90), "A")
        self.assertEqual(percent_to_grade(98), "A")
        self.assertEqual(percent_to_grade(100), "A")
        self.assertEqual(percent_to_grade(97), "A")
        self.assertEqual(percent_to_grade(92), "A")
        self.assertEqual(percent_to_grade(93), "A")

    def test_b_grades(self):
        self.assertEqual(percent_to_grade(85), "B")
        self.assertEqual(percent_to_grade(81), "B")
        self.assertEqual(percent_to_grade(89), "B")
        self.assertEqual(percent_to_grade(87), "B")
        self.assertEqual(percent_to_grade(80), "B")

    def test_c_grades(self):
        self.assertEqual(percent_to_grade(75), "C")
        self.assertEqual(percent_to_grade(70), "C")
        self.assertEqual(percent_to_grade(79), "C")
        self.assertEqual(percent_to_grade(71), "C")

    def test_d_grades(self):
        self.assertEqual(percent_to_grade(65), "D")
        self.assertEqual(percent_to_grade(60), "D")
        self.assertEqual(percent_to_grade(69), "D")
        self.assertEqual(percent_to_grade(68), "D")
        self.assertEqual(percent_to_grade(62), "D")

    def test_f_grades(self):
        self.assertEqual(percent_to_grade(0), "F")
        self.assertEqual(percent_to_grade(9), "F")
        self.assertEqual(percent_to_grade(42), "F")
        self.assertEqual(percent_to_grade(37), "F")
        self.assertEqual(percent_to_grade(59), "F")

    def test_no_rounding_by_default(self):
        self.assertEqual(percent_to_grade(89.4), "B")
        self.assertEqual(percent_to_grade(89.6), "B")
        self.assertEqual(percent_to_grade(90.2), "A")
        self.assertEqual(percent_to_grade(59.9), "F")
        self.assertEqual(percent_to_grade(60.00001), "D")

    # To test bonus 1, comment out the next line
    # @unittest.expectedFailure
    def test_suffix(self):
        self.assertEqual(percent_to_grade(95, suffix=True), "A")
        self.assertEqual(percent_to_grade(92, suffix=True), "A-")
        self.assertEqual(percent_to_grade(97, suffix=True), "A+")
        self.assertEqual(percent_to_grade(100, suffix=True), "A+")
        self.assertEqual(percent_to_grade(81, suffix=True), "B-")
        self.assertEqual(percent_to_grade(86, suffix=True), "B")
        self.assertEqual(percent_to_grade(88, suffix=True), "B+")
        self.assertEqual(percent_to_grade(73, suffix=True), "C")
        self.assertEqual(percent_to_grade(72.6, suffix=True), "C-")
        self.assertEqual(percent_to_grade(64, suffix=True), "D")
        self.assertEqual(percent_to_grade(59, suffix=True), "F")
        self.assertEqual(percent_to_grade(0, suffix=True), "F")
        with self.assertRaises(Exception):  # noqa
            percent_to_grade(0, True)  # suffix is a keyword-only argument

    # To test bonus 2, comment out the next line
    # @unittest.expectedFailure
    def test_rounding(self):
        self.assertEqual(percent_to_grade(89.4, round=True), "B")
        self.assertEqual(percent_to_grade(89.5, round=True), "A")
        self.assertEqual(percent_to_grade(89.5, suffix=False, round=True), "A")
        self.assertEqual(percent_to_grade(89.5, suffix=True, round=True), "A-")
        self.assertEqual(percent_to_grade(96.4, suffix=True, round=True), "A")
        self.assertEqual(percent_to_grade(96.5, suffix=True, round=True), "A+")
        self.assertEqual(percent_to_grade(92.4, suffix=True, round=True), "A-")
        self.assertEqual(percent_to_grade(92.5, suffix=True, round=True), "A")


# To test bonus 3, comment out the next line
# @unittest.expectedFailure
class CalculateGPATests(unittest.TestCase):
    """Tests for calculate_gpa."""

    def test_variety_of_grades(self):
        from grades import calculate_gpa
        self.assertEqual(calculate_gpa(["A", "B", "C", "D", "F"]), 2)
        self.assertEqual(calculate_gpa(["A", "B", "C", "D"]), 2.5)

    def test_with_suffixes(self):
        from grades import calculate_gpa
        self.assertEqual(calculate_gpa(["A-", "B+", "C-", "D+", "F"]), 2)
        self.assertAlmostEqual(
            calculate_gpa(["A-", "B+", "C", "D+", "F"]),
            2.066,
        )
        self.assertAlmostEqual(
            calculate_gpa(["A", "B+", "C", "D+", "F"]),
            2.132,
        )
        self.assertAlmostEqual(
            calculate_gpa(["A-", "B", "C", "D", "F"]),
            1.934,
        )


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class ResultClass(unittest.TextTestResult):
        def was_successful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    import sys
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
