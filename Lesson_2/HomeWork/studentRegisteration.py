studentList = []


def addStudent(name, surname):
    studentName = name+" "+surname
    studentList.append(studentName)
    print(studentName + " added to student database")


def addMultipleStudent(students):
    for student in students:
        # dict
        for name in student:
            studentName = name+" "+student[name]
            studentList.append(studentName)
            print(studentName + " added to student database")


def removeStudent(name, surname):
    studentName = name+" "+surname
    studentList.remove(studentName)
    print(studentName + " removed to database")


def removeMultipleStudent(students):
    for rmStudent in students:
        for name in rmStudent:
            studentName = name+" "+rmStudent[name]
            if studentName in studentList:
                studentList.remove(studentName)
                print(studentName + " removed to database")


def getStudents():
    print("-"*8+" "+"All student of database"+" "+"-"*8)
    i = 0
    while(len(studentList) > i):
        print(studentList[i])
        i += 1


def getStudentNumber(name, surname):
    studentName = name+" "+surname
    if studentName in studentList:
        print("Student number of " + studentName+" : " +
              str(studentList.index(studentName)))
    else:
        print("Stundet not found")


# print operations
addStudent("Ali", "ahmet")
addMultipleStudent([{"Mehmet": "1"}, {"Mehmet": "2"}, {"Ahmet": "4"}])
getStudents()
getStudentNumber("Mehmet", "2")
removeStudent("Ali", "ahmet")
removeMultipleStudent([{"Mehmet": "1"}, {"Ahmet": "4"}])
getStudents()
