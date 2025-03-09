student_grade = input("Enter your grade: ")


# providing for instance where student may include a % sign
student_grade = student_grade.replace("%", "")

# rounding up or down to the nearest whole number and converting to an int
student_grade_float = float(student_grade)
student_grade_rounded = round(student_grade_float)
student_grade = int(student_grade_rounded)

if student_grade <= 40:
    print("You have failed.")
elif student_grade >= 40 and student_grade <= 49:
    print("You have a pass.")
elif student_grade >= 50 and student_grade <= 59:
    print("You have a merit.")
elif student_grade >= 60 and student_grade <= 69:
    print("You have a merit 1.")
elif student_grade >= 70:
    print("You have a distinction.")     