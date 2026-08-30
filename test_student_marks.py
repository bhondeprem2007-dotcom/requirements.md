from student_marks import calculate_grade

assert calculate_grade(95) == "A+"
assert calculate_grade(85) == "A"
assert calculate_grade(75) == "B"
assert calculate_grade(65) == "C"
assert calculate_grade(55) == "D"
assert calculate_grade(40) == "F"

print("All tests passed successfully!")
