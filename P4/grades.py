##
#  This program computes information related to a sequence of grades obtained
#  from the user. It computes the number of passing and failing grades, 
#  computes the average grade and finds the highest and lowest grade.
#

# Initialize the counter variables.
num_passing = 0
num_failing = 0

# Initialize the variables used to compute the average.
total = 0
count = 0

# Initialize the min and max variables.
min_grade = 100.0  # Assuming 100 is the highest grade possible.
max_grade = 0.0

# Use a while loop with a priming read to obtain the grades.
grade = float(input("Enter a grade or -1 to finish: "))
while grade >= 0.0:
    # Increment the passing or failing counter.
    if grade >= 60.0:
        num_passing = num_passing + 1
    else:
        num_failing = num_failing + 1

    # Determine if the grade is the min or max grade.
    if grade < min_grade:
        min_grade = grade
    if grade > max_grade:
        max_grade = grade

    # Add the grade to the running total.
    total = total + grade
    count = count + 1

    # Read the next grade.
    grade = float(input("Enter a grade or -1 to finish: "))

# Print the results.
if count > 0:
    average = total / count
    print("The average grade is %.2f" % average)
    print("Number of passing grades is", num_passing)
    print("Number of failing grades is", num_failing)
    print("The maximum grade is %.2f" % max_grade)
    print("The minimum grade is %.2f" % min_grade)
