def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    marks = []

    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / 5

    print("\n--- Student Result ---")
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", calculate_grade(percentage))
