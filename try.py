class Student:
    name = None
    hw = 0
    lab = 0
    total = 0

def make_student(name:str, hw:int, lab:int, total:int)->Student():
    s = Student()
    s.name = name
    s.hw = hw
    s.lab = lab
    s.total = total
    return s

def find_student(name:str, students:list)->Student:
    for student in students:
        if student.name == name:
            return student.name
    return None
    
def lab_scores(file_name:str, students:list)->list:
    file = open(file_name, "r")
    for line in file.readlines():
        line = line.split()
        name = line[0]
        lab = int(line[1])
        student = find_student(name, students)
        if student == None:
            a = make_student(name, 0, lab, 0)
            students.append(a)
        elif student != None:
            student.lab += int(lab)
    file.close()
    return students

def hw_scores(file_name:str, students:list)->list:
    file = open(file_name, "r")
    for line in file.readlines():
        line = line.split()
        name = line[0]
        hw = int(line[1])
        student = find_student(name)
        if student == None:
            a = make_student(name, 0, hw, 0)
            students.append(a)
        elif student != None:
            student.hw += int(hw)
    file.close()
    return students

    
def outputA(students:list, file_name:str, assignments:int):
    file = open(file_name, "w")
    for student in students:
        student.total = float(((student.hw/assignments)*.5) + ((student.lab/assignments))*.5)
        if student.total > 90:
            file.write(student.name , str(student.total))
    file.close()
    
def main():
    students = []
    assignments = int(input("Assignments: "))
    students = lab_scores("lab.py", students)
    students = hw_scores("hw.py", students)
    outputA(students, "A.txt", assignments)
##    outputB(students, "B.txt", assignments)
##    outputC(students, "C.txt", assignments)
##    outputD(students, "C.txt", assignments)
##    outputF(students, "D.txt", assignments)   
main()








    
