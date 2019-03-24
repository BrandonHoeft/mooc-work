print("Hello World!")

sample_set = {1, 2, 3, 4, 4, 4}
print(sample_set)

sample_dict = {"name": "Brandon",
               "grades": [70, 75, 80, 94, 59],
               "exams": {"final": 70,
                         "midterm": 75}}

print(sample_dict["name"])
print(sample_dict["grades"][0])
print(sample_dict["exams"]["final"])

# Appending to a list
my_list = []
my_list.append(5) # modifies in place. doesn't return anything.
print(my_list)
my_list.append('el duderino')
print(my_list)

s = create_student()
#add_grade(s, 89) # PASSING BY REFERENCE. student is a reference to the same dictionary. Behind the scenes, we are referencing the same dictionary.
#add_grade(s, 74)
#add_grade(s, 95)
#print(s)
# test calculate avg_grade()
#s2 = create_student()
#print(calculate_avg_grade(s2))
#add_grade(s2, 57)
#add_grade(s2, 68)
#print(calculate_avg_grade(s2))
#print_student_details(s)



###############################################################################
# APP: Create new students, and calculate the grades of students 

student_list = []


def create_student():
    """Ask the user to input their name. Returns a dictionary
    with default empty list of their grades."""

    name = input("Please enter the student's name: ")
    grades = []
    return {'name': name, 'grades': grades}


# Create another method that will append a grade to the empty grades list of the created student.
def add_grade(student, grade):
    """Append a grade to the student's dictionary"""
    student['grades'].append(grade) # modifies in place. doesn't return anything.
    return None


def calculate_avg_grade(student):
    """add together all of the student's grades and divide them
    by the number of tests taken."""
    count = len(student['grades'])
    total = sum(student['grades']) 
    if count == 0:
        pass
    else:
        return total / count



def print_student_details(student):
    print('{n} has an average grade of: {g}'.format(n=student['name'], g=calculate_avg_grade(student)))


def print_student_list(student_list):
    for i, student in enumerate(student_list):
        print("ID: ", str(i))
        print_student_details(student)


def menu():
    """User interface for the student grades application"""
    
    selection = input("Press 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'g' to add a new grade for a student, "
                      "or 'q' to quit the program: ")
    if selection == 'p':
        print_student_list(student_list)
    elif selection == 's':
        student_list.append(create_student())
    elif selection == 'g':
        student_id = int(input("To add a grade, enter Student's ID (as a #): "))
        student = student_list[student_id]
        new_grade = int(input("Enter the grade to be added (as a #): "))
        add_grade(student, new_grade)
    elif selection == 'q':
        pass
    

