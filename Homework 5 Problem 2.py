"""
ICS 31 Homework 5 Problem 2
Author: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
"""
class Student:
    Name = None
    HW = 0
    Quiz = 0
    Total = 0
    
def makeStudent(Name:str, HW:int, Quiz:int, Total:int) -> Student:
    s = Student()
    s.Name  = Name
    s.HW    = HW
    s.Quiz   = Quiz
    s.Total  = Total
    return s

def find_student(name:str , student_list:list) -> Student:
    for student in student_list:
        if(student.Name == name): #why can't I have it be = Name??
            return student
    return None

def get_HW_Scores(file_name:str, student_list:list) -> list:
    file = open(file_name, "r")
    for line in file.readlines():
        sl = line.strip("\n").split()
        student = find_student(sl[0], student_list)
        na = line.split()[0]
        Hscore = int(line.split()[1])
#print(sl[0]) #names
        
        if(student == None):
            student_list.append(makeStudent(na, Hscore, 0, 0)) #the zero is for the parametrs we don't need her/ from make_Student
        else:
            student.HW += int(Hscore)
            
#print(int(line.split()[1])           
    file.close()
    return student_list
    
def get_Quiz_Scores (file_name:str, student_list:list) -> list:
    file = open(file_name, "r")
    for line in file.readlines():
        sl = line.strip("\n").split()
        student = find_student(sl[0], student_list)
        na = line.split()[0]
        Qscore = int(line.split()[1])

        if(student == None):
            student_list.append(makeStudent(na, 0, Qscore, 0 ))
        else:
            student.Quiz += int(Qscore)

    file.close()
    return student_list
    
def assign_grade(score) -> str: 
    if (score >= 97):
        return "A+"
    elif (97 > score >= 93):
        return "A"
    elif (93 > score >= 90):
        return "A-"
    elif (90 > score >= 87):
        return "B+"
    elif (87 > score >= 83):
        return "B"
    elif(83 > score >= 80):
        return "B-"
    elif (80 > score >= 77):
        return "C+"
    elif (77 > score >= 73):
        return "C"
    elif (73 > score >= 70):
        return "C-"
    elif (70 > score >= 67):
        return "D+"
    elif (67 > score >= 63):
        return "D"
    elif (63 > score >= 60):
        return "D-"
    elif (score  < 60):
        return "F"

def output_Scores(file_name2:str, student_list:list, assignments:int, quizzes:int):
    new_file = open(file_name2, "w")
    for student in student_list:
        
        HW_percent= float(student.HW/assignments)
        quiz_percent= float(student.Quiz/quizzes)
        num= float(HW_percent*.5+quiz_percent*.5)
       
        new_file.write(student.Name + "\n")
        new_file.write("HW_Percent: " + str(HW_percent)+ "% \n")
        new_file.write("Quiz_Percent: " + str(quiz_percent) + "% \n ")
        new_file. write("Overall: " + str(num) + "%" "(" + assign_grade(num) + ")" + "\n")
    new_file.close()
   
def main():
    student_list = []
    assignments = 3
    quizzes = 3
    try:
        student_list = get_HW_Scores("hw.txt", student_list)
        student_list = get_Quiz_Scores("quiz.txt", student_list)
        output_Scores("scores.txt",student_list, assignments, quizzes)
    except FileNotFoundError as e:
        print (e)
        print("File not found")
main()
