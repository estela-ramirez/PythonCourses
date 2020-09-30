'''
ICS 31 Lab 5  Problem 3
Driver:  UCI_ID: 39858997  Name: Santiago Uriarte
Navigator:  UCI_ID: 87491775  Name: David Palacios
'''
class Student:
    Name    = None
    HW      = 0
    Lab     = 0
    Total    = 0

def makeStudent(Name: str, HW: int, Lab: int, Total: int) -> Student:
    s = Student()
    s.Name  = Name
    s.Total  = Total
    s.Lab   = Lab
    s.HW    = HW
    return s


def getStudent(name:str, student_list: list) ->  Student:
    for student in student_list:
        if(student.Name == name):
            return student
    return None


def get_Lab_Scores(file_name: str, student_list: list) -> list:
    file = open(file_name, "r")
    for line in file.readlines():
        student = getStudent(line.split()[0], student_list)
        if(student != None):
            student.Lab += int(line.split()[1])
        if(student == None):
            student_list.append(makeStudent(line.split()[0], 0, int(line.split()[1]), 0))
    file.close()
    return student_list
                

def get_HW_Scores(file_name: str, student_list: list) -> list:
    file = open(file_name, "r")
    for line in file.readlines():
        student = getStudent(line.split()[0], student_list)
        if(student != None):
            student.HW += int(line.split()[1])
        if(student == None):
            student_list.append(makeStudent(line.split()[0], int(line.split()[1]), 0, 0))
    file.close()
    return student_list


def set_overall_percent(student_list: list, assignments: int) -> list:
    for student in student_list:
        student.Total = float(((student.HW / assignments) * .5) + ((student.Lab / assignments) * .5))
    return student_list


def output_A_grade(student_list: list, file_name: str, assignments: list):
    file = open(file_name, "w+")
    for student in student_list:
        if(student.Total >= 90):
            file.write(student.Name + "\n" + "Overall_Percent: " + str(student.Total) + "% \n")
    file.close()

def output_B_grade(student_list: list, file_name: str, assignments: int):
    file = open(file_name, "w+")
    for student in student_list:
        if(student.Total >= 80 and student.Total < 90):
            file.write(student.Name + "\n" + "Overall_Percent: " + str(student.Total) + "% \n")
    file.close()


def output_C_grade(student_list: list, file_name: str, assignments: int):
    file = open(file_name, "w+")
    for student in student_list:
        if(student.Total >= 70 and student.Total < 80):
            file.write(student.Name + "\n" + "Overall_Percent: " + str(student.Total) + "% \n")
    file.close()


def output_D_grade(student_list: list, file_name: str, assignments: int):
    file = open(file_name, "w+")
    for student in student_list:
        if(student.Total >= 60 and student.Total < 70):
            file.write(student.Name + "\n" + "Overall_Percent: " + str(student.Total) + "% \n")
    file.close()

def output_F_grade(student_list: list, file_name: str, assignments: int):
    file = open(file_name, "w+")
    for student in student_list:
        if(student.Total < 60):
            file.write(student.Name + "\n" + "Overall_Percent: " + str(student.Total) + "% \n")
    file.close()


def main():
    student_list = []
    assignments = int(input("How many submitted assignments: "))
    try:
        student_list = get_Lab_Scores("lab.py", student_list)
        student_list = get_HW_Scores("hw.py", student_list)
        student_list = set_overall_percent(student_list, assignments)
        output_A_grade(student_list, "A.txt" , assignments)
        output_B_grade(student_list, "B.txt" , assignments)
        output_C_grade(student_list, "C.txt" , assignments)
        output_D_grade(student_list, "D.txt" , assignments)
        output_F_grade(student_list, "F.txt" , assignments)
    except FileNotFoundError:
        print("File not found")

main()

