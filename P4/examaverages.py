##
#  This program computes the average exam grade for multiple students.
#

# Obtain the number of exam grades per student.
num_exams = int(input("How many exam grades does each student have? "))

# Initialize more_grades to a non-sentinel value.
more_grades = "Y"

# Compute average exam grades until the user wants to stop.
while more_grades == "Y":

    # Compute the average grade for one student.
    print("Enter the exam grades.")
    total = 0
    for i in range(1, num_exams + 1):
        score = int(input("Exam %d: " % i))  # Prompt for each exam grade.
        total = total + score

    average = total / num_exams
    print("The average is %.2f" % average)

    # Prompt whether the user wants to enter grades for another student.
    more_grades = input("Enter exam grades for another student (Y/N)? ")
    more_grades = more_grades.upper()
