# Lists storing student names and their corresponding grades
names = ['ram', 'sham', 'raj', 'sachin']
grades = [50, 70, 80, 90]

# Read the student's name from the user
student_name = input("Enter the name of the student: ").strip().lower()

# Check if the student is in the list
if student_name in names:
    # Find the index of the student's name
    index = names.index(student_name)
    # Get the corresponding grade
    student_grade = grades[index]
    print(f"{student_name.capitalize()}'s grade is: {student_grade}")
else:
    print("Student not found.")
