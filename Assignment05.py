#Title: Assignment 05
#Desc: This assignment demosntrates using dictionaries, files and exception handling
#Change Log: (Who, When, What)
#   Sam Bircher, 11-15-23, Create script

#Impor the JSON module
import json

#Define the data constants
FILE_NAME: str = 'Enrollments.json'

MENU: str = '''
----Course Registration Menu----
  Select from the following menu:
  1. Register as student for a course
  2. Show current data
  3. Save data to a file
  4. Exit the program
---------------------
'''
#Define the program variables
student_first_name: str = ''
student_last_name: str =''
course_name: str = ''
menu_choice: str =''
student_data: dict = {}
students: list = []
file = None
message: str =''

#When the program starts, read the file data into a list of dictionary rows (table)
try:
    #Open, load, and read the contents of the existing JSON file
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    #Close the file
    file.close()
    #Present error if file does not exist
except FileNotFoundError as e:
    print("Text file must exist before running this script")
    print("---Technical error message---")
    print(e, e.__doc__, type(e), sep='\n')
    #Catch all for unforeseen errors
except Exception as e:
    print("There was a non-specific error!\n")
    print("---Technical error message---")
    print(e, e.__doc__, type(e), sep = '\n')
    #Close the file if it is not already closed
finally:
    if file.closed == False:
        print("Closing the file")
        file.close()

while True:
    #Display the Menu options
    print(MENU)
    menu_choice = input("Enter your menu choice number.")

    if menu_choice == '1':
        try:
            print("-"*50)
            #Prompt the user for the students first name
            student_first_name = input("What is the student's first name?")
            #Validate alphabetical input
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            #Prompt the user for the student's last name
            student_last_name = input("What is the student's last name?")
            #Validate alphabetical input
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = (input("What is the name of the course? "))
            #Add the user input (dictionary data) to the student list
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            #Append the data to the existing student list
            students.append(student_data)

        except ValueError as e:
            print(e)
            print("---Technical error message---")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error.\n")
            print("---Technical error message---")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    elif menu_choice == '2':
        print("-"*50)
        #Iterate through and print all the data in the student list
        for student in students:
            print(f'{student["FirstName"]}, {student["LastName"]}, {student["CourseName"]})')
        print("-"*50)
        continue

    elif menu_choice == '3':
        try:
            #Open Enrollments.json in the write function and save user input
            file = open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
            print('*' * 50)
            print("This data has been saved!")
            continue
        #Error catching if data is not in valid JSON format
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("---Technical error message")
            print(e, e.__doc__, type(e), sep='\n')
        #Catch all for unforseen errors saving data to the JSON file
        except Exception as e:
            print("There was a non-specific error!\n")
            print("---Technical error message---")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    #close the program
    elif menu_choice == '4':
        break