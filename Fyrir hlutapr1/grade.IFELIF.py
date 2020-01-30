grade = float(input("Input a grade: ")) # Do not change this line

if grade < 0.0 or grade > 10.0:
    print("Invalid grade!")
elif grade >= 5.0 and grade <= 10:
    print("Passing grade!")
else:
    print("Failing grade!")