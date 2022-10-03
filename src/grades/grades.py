def percent_to_grade(in_percentage: float, *, suffix: bool = False, round: bool = False) -> str:
    """Convert a percentage to a grade by using a specific flavor of the A-F grading system used in the US."""
    grades = ["F"] + [grade + suf for grade in ["D", "C", "B", "A"] for suf in (("-", "", "+") if suffix else ("", ))]
    thresholds = [57 + 3*i + i//3 for i in range(1, len(grades))] if suffix else range(60, 91, 10)
    in_percentage = int(in_percentage + 0.5) if round else in_percentage

    for i in range(len(thresholds)):
        if in_percentage < thresholds[i]:
            return grades[i]
    return grades[-1]


def calculate_gpa(in_grades: list[str]) -> float:
    """Accepts a sequence of letter grades and returns the grade point average based on the exercise"s rules."""
    grades = [grade + suffix for grade in ["D", "C", "B", "A"] for suffix in ("-", "", "+")]
    grade_to_score: dict[str, float] = {"F": 0}
    grade_to_score |= {grade: round(2/3 + score/3, 2) for grade, score in zip(grades, range(len(grades)))}

    score = sum(grade_to_score[grade] for grade in in_grades)
    return score / len(in_grades)


def main():
    # Base exercise:
    res, expected_res = percent_to_grade(72.5), "C"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(89.6), "B"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(60), "D"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(100), "A"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(2), "F"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 1
    # Allow a keyword-only suffix argument to be passed to your percent_to_grade function.
    # When suffix is True, you should add - and + suffixes to the grade according to another set of rules.
    res, expected_res = percent_to_grade(72.5, suffix=True), "C-"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(89.6, suffix=True), "B+"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(60, suffix=True), "D-"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(100, suffix=True), "A+"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(2, suffix=True), "F"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 2
    # Accept another optional keyword-only argument: round. When round is True you should round percentages to their
    # nearest whole number before calculating grades, with .5 always rounding upward.
    res, expected_res = percent_to_grade(69.4, round=True), "D"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(69.6, round=True), "C"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(72.5, suffix=True, round=True), "C"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = percent_to_grade(89.6, suffix=True, round=True), "A-"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 3
    # Create another function called calculate_gpa which accepts a sequence of letter grades and returns
    # the grade point average based on the following rules: ...
    res, expected_res = calculate_gpa(["D+", "C", "A-", "B"]), 2.5
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = calculate_gpa(["B+", "A", "C+", "F"]), 2.415
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    print("Passed the tests.")


if __name__ == "__main__":
    main()
