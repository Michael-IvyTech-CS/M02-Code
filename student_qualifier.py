"""
student_qualifier.py
Michael Barthauer
Accepts student name and gpa as input; returns 
whether student made the Dean's List and/or Honor Roll
"""

last_name = input("Enter student last name (or ZZZ to quit): ")

while last_name != 'ZZZ':
    first_name = input("Enter student first name: ")
    gpa = float(input("Enter student gpa: "))

    if gpa >= 3.5:
        print("This student has made the Dean's List!")
    if gpa >= 3.25:
        print("This student has made the Honor Roll!")
    
    last_name = input("Enter student last name (or ZZZ to quit): ")
