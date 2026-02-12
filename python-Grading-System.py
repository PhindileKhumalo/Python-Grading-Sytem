# A simple python script to calculate grades based on scores.input a score and get a grade

def calculate_grade(mark):
    if mark >=80:
        return "A"
    elif mark >=70:
        return "B"
    elif mark >=60:
        return "C"
    elif mark >=50:
        return "D"
    else:
        return "F"
# Prompt the user to enter their marks and convert the input to an integer
mark= int(input("Enter your marks: "))

# Call the function
print("Grade: ",calculate_grade(mark))  

