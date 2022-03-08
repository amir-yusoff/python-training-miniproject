import pandas as pd
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AMIR-PC\SQLEXPRESS;'
                      'Database=training_project;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

print('Connected to SQL Server')


#function for option 1 | add student info

def addStudent():
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dob = input("Enter Student DOB: ")
    age = int(input("Enter Student Age: "))
    street = input("Enter Student Street: ")
    state = input("Enter Student State: ")
    country = input("Enter Student Country: ")
    postcode = int(input("Enter Student Postcode: "))
    phone = input("Enter Student Phone: ")
    email = input("Enter Student Email: ")

    cursor.execute("""
        INSERT INTO 
            dbo.Student_Personal 
        VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id, name, dob, age, street, state, country, postcode, phone, email))

    conn.commit()
    print('Student information successfully added\n')

#function for option 2 | insert student marks

def addMarks():
    id = input("Enter Student ID: ")
    malay = int(input("Enter marks for Malay:"))
    english = int(input("Enter marks for English:"))
    science = int(input("Enter marks for Science:"))
    maths = int(input("Enter marks for Maths:"))
    arts = int(input("Enter marks for Arts:"))
    history = int(input("Enter marks for History:"))
    geography = int(input("Enter marks for Geography:"))

    total = malay + english + science + maths + arts + history + geography
    average = total / 7

    if average >= 80:
        result = 'PASS'
        grade = 'A'
    elif average >= 70:
        result = 'PASS'
        grade = 'B'  
    elif average >= 60:
        result = 'PASS'
        grade = 'C'
    elif average >= 50:
        result = 'PASS'
        grade = 'D'
    else:
        result = 'FAIL'
        grade = 'F'

    cursor.execute("""
        INSERT INTO 
            dbo.Student_Marks 
        VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id, malay, english, science, maths, arts, history, geography, total, average, result, grade))

    conn.commit()
    print('Student marks successfully added\n')

#function for option 3 | update student info

def updateStudent():
    id = int(input("Enter Student ID to update: "))

    print('What to update?')
    print('1. Student Name')
    print('2. Student DOB')
    print('3. Student Age')
    print('4. Student Street')
    print('5. Student State')
    print('6. Student Country')
    print('7. Student Postcode')
    print('8. Student Phone')
    print('9. Student Email\n')

    menu = int(input('Enter your choice: '))

    if menu == 1:
        update = input("Enter Student Name: ")
        cursor.execute("UPDATE dbo.Student_Personal SET Std_Name = '%s' WHERE Std_ID = %d " %(update, id))
    elif menu == 2:
        update = input("Enter Student DOB: ")
        cursor.execute("UPDATE dbo.Student_Personal SET Std_DOB = '%s' WHERE Std_ID = %d " %(update, id))
    elif menu == 3:
        update = int(input("Enter Student Age: "))
        cursor.execute("UPDATE dbo.Student_Personal SET Std_Age = %d WHERE Std_ID = %d " %(update, id))
    elif menu == 4:
        update = input("Enter Student Street: ")
        cursor.execute("UPDATE dbo.Student_Personal SET Std_Street = '%s' WHERE Std_ID = %d " %(update, id))
    elif menu == 5:
        update = input("Enter Student State: ")
        cursor.execute("UPDATE dbo.Student_Personal SET Std_State = '%s' WHERE Std_ID = %d " %(update, id))
    elif menu == 6:
        update = input("Enter Student Country: ")
        cursor.execute("UPDATE dbo.Student_Personal SET Std_Country = '%s' WHERE Std_ID = %d " %(update, id))
    elif menu == 7:
        update = int(input("Enter Student Postcode: "))
        cursor.execute("UPDATE dbo.Student_Personal SET Std_Postcode = %d WHERE Std_ID = %d " %(update, id))
    elif menu == 8:
        update = input("Enter Student Phone: ")
        cursor.execute("UPDATE dbo.Student_Personal SET Std_Phone = '%s' WHERE Std_ID = %d " %(update, id))
    elif menu == 9:
        update = input("Enter Student Email: ")
        cursor.execute("UPDATE dbo.Student_Personal SET Std_Email = '%s' WHERE Std_ID = %d " %(update, id))
    else:
        print('Invalid input')
    
    conn.commit()
    print('Student information successfully updated\n')

#function for option 4 | delete student info
def deleteStudent():
    id = int(input("Enter Student ID to delete: "))
    cursor.execute("DELETE FROM dbo.Student_Personal WHERE Std_ID = %d " %(id))
    conn.commit()
    print('Student information successfully deleted\n')

#function for option 5 | search student info

def searchStudent():
    id = int(input("Enter Student ID to search: "))

    cursor.execute('''
                SELECT * 
                FROM Student_Personal
                LEFT JOIN Student_Marks ON Student_Personal.Std_ID = Student_Marks.Std_ID
                WHERE Student_Personal.Std_ID = ?
                '''
                , id)
    row = cursor.fetchone()

    if row == None:
        print('Student not found')
    else:
        print('Student found')
        print('------------DETAILS--------------')
        print('Student ID: ', row[0])
        print('Student Name: ', row[1])
        print('Student DOB: ', row[2])
        print('Student Age: ', row[3])
        print('Student Street: ', row[4])
        print('Student State: ', row[5])
        print('Student Country: ', row[6])
        print('Student Postcode: ', row[7])
        print('Student Phone: ', row[8])
        print('Student Email: ', row[9])
        print('\n-------------MARKS---------------')
        print('Student Malay Marks: ', row[11])
        print('Student English Marks: ', row[12])
        print('Student Science Marks: ', row[13])
        print('Student Maths Marks: ', row[14])
        print('Student Arts Marks: ', row[15])
        print('Student History Marks: ', row[16])
        print('Student Geography Marks: ', row[17])
        print('\nGrade: ', row[21])
        print('Result: ', row[20])
        print('\n')

    conn.commit()

    print('Student info displayed\n')


#function for option 6 | display all student report
#function for option 6 | display all student report

def displayReport():
    cursor.execute('''
                SELECT * 
                FROM Student_Personal
                LEFT JOIN Student_Marks ON Student_Personal.Std_ID = Student_Marks.Std_ID
                ''')
    rows = cursor.fetchall()

    for row in rows:
        print('------------DETAILS--------------')
        print('Student ID: ', row[0])
        print('Student Name: ', row[1])
        print('Student DOB: ', row[2])
        print('Student Age: ', row[3])
        print('Student Street: ', row[4])
        print('Student State: ', row[5])
        print('Student Country: ', row[6])
        print('Student Postcode: ', row[7])
        print('Student Phone: ', row[8])
        print('Student Email: ', row[9])
        print('\n-------------MARKS---------------')
        print('Student Malay Marks: ', row[11])
        print('Student English Marks: ', row[12])
        print('Student Science Marks: ', row[13])
        print('Student Maths Marks: ', row[14])
        print('Student Arts Marks: ', row[15])
        print('Student History Marks: ', row[16])
        print('Student Geography Marks: ', row[17])
        print('\nGrade: ', row[21])
        print('Result: ', row[20])
        print('\n')

    conn.commit()

    print('All student info displayed\n')


# function to print menu

def print_menu():      
    print('STUDENT MANAGEMENT SYSTEM\n')

    print('1. Add a new student information')
    print('2. Insert student marks')
    print('3. Update student information')
    print('4. Delete student information')
    print('5. Search student information')
    print('6. Display all student report')
    print('0. Exit')
    print('\n')

# main program

while(True):
    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')

    if option == 1:
        addStudent()
    elif option == 2:
        addMarks()
    elif option == 3:
        updateStudent()
    elif option == 4:
        deleteStudent()
    elif option == 5:
        searchStudent()
    elif option == 6:
        displayReport()
    elif option == 0:
        print('Exiting...')
        break
    else:
        print('Invalid option. Please enter a number between 1 and 6.\n')









