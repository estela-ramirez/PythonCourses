"""
ICS 31 Lab 5 Problem 3
Driver: UCI_ID: 338298 Name: Estela Ramirez Ramirez
Navigator: UCI_ID: 50092987 Name: Uyen Tran
"""

class Student:
    Name = None
    HW = 0
    Lab = 0
    Total = 0

def get_Lab_Scores (file_name: str, student_list:list) ->list:
    while True:
        try:
            openFile = open (file_name, 'r')
            break
        except FileNotFoundError as e:
            print (e)
            file_name= input ("Input File Name:")
    Lab = openFile.readlines ()
    s = Student()
    s.Name = Lab[0].split()[0]
    s.Lab = int(Lab[0].split()[1])
    student_list.append (s)
    for line in Lab [1:]:
        each = line.strip().split()
        count = 0
        for student1 in student_list:
            if student1.Name == each[0]:
                student1.Lab += int(each[1])
                count =1
        if count == 0:
            student2 = Student()
            student2.Name = each [0]
            student2.Lab = int (each[1])
            student_list.append (student2)
    return student_list

def get_HW_Scores (file_name2: str, student_list:list) ->list:
    while True:
        try:
            openFile = open (file_name2, 'r')
            break
        except FileNotFoundError as e:
            print (e)
            file_name2= input ("Input File Name:")
    HW = openFile.readlines ()
    for line in HW:
        each = line.strip().split()
        count = 0
        for student1 in student_list:
            if student1.Name == each[0]:
                student1.HW += int(each[1])
                count =1
        if count == 0:
            student2 = Student()
            student2.Name = each [0]
            student2.HW = int (each[1]) 
            student_list.append (student2)
    return student_list

def output_A_grade (student_list:list, file_name: str, assignments:int):
    openA = open ("A.txt", "w")
    for i in range (len(student_list)):
        Total = (int(student_list[i].HW)/int(assignments))*.5 + (int(student_list[i].Lab)/int(assignments))*.5
        if Total >= 90:
            FileA = openA.write (student_list[i].Name + "\n" + "Overall_Percent:" +
                                     str(Total)  + "% \n")
    openA.close()

def output_B_grade (student_list:list, file_name: str, assignments:int):
    openB = open ("B.txt", "w")
    for i in range(len(student_list)):
        Total = (int(student_list[i].HW)/int(assignments))*.5 + (int(student_list[i].Lab)/int(assignments))*.5
        if Total >= 80 and Total < 90:
            openB.write (student_list[i].Name + "\n" + "Overall_Percent:" +
                                     str(Total)+ "% \n")
    openB.close()

def output_C_grade (student_list:list, file_name: str, assignments:int):
    openC = open ("C.txt", "w")
    for i in range(len(student_list)):
        Total = (int(student_list[i].HW)/int(assignments))*.5 + (int(student_list[i].Lab)/int(assignments))*.5
        if Total >= 70 and Total <80:
            openC.write (student_list[i].Name + "\n" + "Overall_Percent:" +
                                     str(Total) + "% \n")
    openC.close()

def output_D_grade (student_list:list, file_name: str, assignments:int):
    openD = open ("D.txt", "w")
    for i in range (len(student_list)):
        Total = (int(student_list[i].HW)/int(assignments))*.5 + (int(student_list[i].Lab)/int(assignments))*.5
        if Total >= 60 and Total < 70:
            FileD = openD.write (student_list[i].Name + "\n" + "Overall_Percent:" +
                                     str(Total) + "% \n")
    openD.close()

def output_F_grade (student_list:list, file_name: str, assignments:int):
    openF = open ("F.txt", "w") 
    for i in range (len(student_list)):
        Total = (int(student_list[i].HW)/int(assignments))*.5 + (int(student_list[i].Lab)/int(assignments))*.5
        if Total < 60:
            FileF = openF.write (student_list[i].Name + "\n" + "Overall_Percent:" +
                                     str(Total) + "% \n")
    openF.close()

def main ():
    student_list = []
    assignments = int (input("How many submitted assignments:"))
    student_list = get_Lab_Scores ("lab.txt", student_list)
    student_list = get_HW_Scores ("hw.txt",student_list)
    output_A_grade (student_list, "A.txt", assignments)
    output_B_grade (student_list, "B.txt", assignments)
    output_C_grade (student_list, "C.txt", assignments)
    output_D_grade (student_list, "D.txt", assignments)
    output_F_grade (student_list, "F.txt", assignments)

main ()    
            
