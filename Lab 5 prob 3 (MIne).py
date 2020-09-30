class Student:
    Name = None
    HW = 0
    Lab = 0
    Total = 0

def makeStudent (Name:str, HW: int, Lab: int, Total: int) ->Student:
    s = Student ()
    s.Name = Name
    s.Total = Total
    s.Lab = Lab
    s.HW = HW
    return S

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
                student1.HW += float(each[1])
                count =1
        if count == 0:
            student2 = Student()
            student2.Name = each [0]
            student2.HW = float(each[1])
            student_list.append (student2)
    return student_list

def overall_percent(student_list: list, assignments: int) -> list:
    for student in student_list:
        student.Total = float(((student.HW / assignments) * .5) + ((student.Lab / assignments) * .5))
    return student_list

def output_A_grade (student_list:list, file_name:str, assignments:int):
    file = open ("A.txt", "w")
    for student in student_list:
       if (student.Total) >= 90:
           file.write (student.Name + "\n" + "Overall_Percent: " + str(student.Total)  + "% \n")
    file.close()

def output_B_grade (student_list:list, file_name: str, assignments:int):
    file = open ("B.txt", "w")
    for student in student_list:
        if 90 <(Student.Total) >= 80:
            file.write (student.Name + "\n" + "Overall_Percent:" + str(student.Total)+ "% \n")
    file.close()

def output_C_grade (student_list:list, file_name: str, assignments:int):
    file = open ("C.txt", "w")
    for student in student_list:
        if 80 <(Student.Total) >= 70:
            file.write (student.Name + "\n" + "Overall_Percent:" + str(student.Total) + "% \n")
    file.close()

def output_D_grade (student_list:list, file_name: str, assignments:int):
    file = open ("D.txt", "w")
    for student in student_list:
        if 70 <(Student.Total) >= 60:
            file.write (student.Name + "\n" + "Overall_Percent:" + str(student.Total) + "% \n")
    file.close()

def output_F_grade (student_list:list, file_name: str, assignments:int):
    file = open ("F.txt", "w")
    for student in student_list:
        if (Student.Total) < 60:
            file.write (student.Name + "\n" + "Overall_Percent:" + str(student.Total) + "% \n")
    file.close()

def main ():
    student_list = []
    assignments = int (input("How many submitted assignments:"))
    student_list = get_Lab_Scores ("lab.txt", student_list)
    student_list = get_HW_Scores ("hw.txt",student_list)
    student_list = overall_percent(student_list, assignments)
    output_A_grade (student_list, "A.txt", assignments)
    output_B_grade (student_list, "B.txt", assignments)
    output_C_grade (student_list, "C.txt", assignments)
    output_D_grade (student_list, "D.txt", assignments)
    output_F_grade (student_list, "F.txt", assignments)

main ()    
            
