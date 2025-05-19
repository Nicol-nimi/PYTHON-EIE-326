possible_grades = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'F': 0}

total = 0
total_units_offered= 0

for i in range(6):
    grade = input(f"Grade in course {i+1} (A-F): ").upper()
    units = int(input(f"Units for course {i+1}: "))

    if grade in possible_grades:
        total += possible_grades[grade] * units
        total_units_offered += units
    else:
        print("Invalid grade entered. Please use A, B, C, D, or F.")
        break

if total > 0:
    gpa = total / total_units_offered
    print("Your GPA is:", round(gpa, 2))
