'''
ICS 31 Homework 5  Problem 2
Author:  UCI_ID: 41596042  Name: Liza Joseph
'''
class Student:
    Name= None
    HW=0
    Quiz=0
    Total=0

def makeStudent(Name: str, HW: int, Quiz:int, Total:int)->Student:
    s=Student()
    s.Name=Name
    s.HW=HW
    s.Quiz=Quiz
    return s
    
def find_student(student_list:list, name:str):
    for student in student_list:
        if name==student.Name:
            return student
    return None

def get_HW_Scores(file_name:str, student_list:list)->list:
   a=open(file_name, "r")
   for line in a:
       i=line.strip("\n").split("\t")
       x=find_student(student_list, i[0])
       if x==None:
           x=Student()
           x.Name=i[0]
           x.HW=int(i[-1])
           student_list.append(x)
       else:
           x.HW+=int(i[-1])
   a.close()
   return student_list

def get_Quiz_Scores(file_name:str, student_list:list)->list:
    b=open(file_name, "r")
    for line in b:
        i=line.strip("\n").split("\t")
        x=find_student(student_list, i[0])
        if x==None:
            x=Student()
            x.Name=i[0]
            x.Quiz=int(i[-1])
            student_list.append(x)
        else:
            x.Quiz+=int(i[-1])
    b.close()
    return student_list
 
def output_Scores(student_list: list):
    file_1= open("scores.txt",'w')
    for x in student_list:
        
        hw_percent= x.HW/3
        quiz_percent= x.Quiz/3
        num= hw_percent*.5+quiz_percent*.5

        file_1.write(x.Name + "\n")
        file_1.write("HW_Percent: "+str(hw_percent)+"%\n")
        file_1.write("Quiz_Percent: "+ str(quiz_percent) + "%\n")
        file_1.write("Overall: "+ str(num)+"%""("+assign_grade(num)+")" +"\n")
    file_1.close()
    
def assign_grade(score):
    if score >=97:
        return "A+"
    elif score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 63:
        return "D"
    elif score >= 60:
        return "D-"
    elif score < 60:
        return "F"
    
    
def main ():
    student_list=[]
    student_list = get_HW_Scores("hw.txt", student_list)
    student_list = get_Quiz_Scores("quiz.txt",student_list)
    output_Scores(student_list)

if __name__ == "__main__":
    main()

 
       
    
