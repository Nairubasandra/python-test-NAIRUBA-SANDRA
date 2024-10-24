# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
def student_marks():
    if student_marks >= 90:
        print('Grade A')
    elif student_marks >= 80:
        print('Grade B') 
    elif student_marks >= 70:
        print('Grade C')
    elif student_marks >= 60:
        print('Grade D')
    elif student_marks >=40:
        print('Grade E')
    else:
        print('Grade F')
