"""
ICS 31 Lab 5 Problem 2
Driver: UCI_ID: 50092987 Name: Uyen Tran
Navigator: UCI_ID: 18108714 Name:Estela Ramirez Ramirez
"""
class Student():
    Name = None
    Lab = 0
        
def makeList (openFile:'file') -> Student:
    text = openFile.readlines ()
    studentList = []
    s = Student()
    s.Name = text[0].split()[0]#appends name
    s.score = int(text[0].split()[1])#appends score
    studentList.append(s)
    for line in text[1:]: #why backwards?
        each = line.strip().split()
        print(each)
        count = 0
        for student1 in studentList:
            if student1.Name == each[0]:
                student1.score += int(each [1])
                count = 1 #counts name of student
        if count == 0: #if name is not in list
            student2 = Student()
            student2.Name = each[0]
            student2.score = int(each [1])
            studentList.append (student2)
    return studentList
            
def getFile(file_name:str):
    while True:
        try:
           openFile = open(file_name, "r")
           break
        except FileNotFoundError as e:
            print (e)
            file_name = input ("Input Valid File Name:")
    x = makeList(openFile)
    openFile.close()
    print()
    return x

def getScore (file:'file', studentList:list, num:int) ->int:
    for i in range (len(studentList)):
        lab_percent = int(studentList[i].score)/int(num)
        file.write (studentList[i].Name + "\n" + "Lab_Percent:" + str(lab_percent) + "%\n\n")
    
def write_out (file_name2:str, studentList:list, num:int):
    openFile = open (file_name2, 'w')
    file = openFile
    getScore (file, studentList,num)
    openFile.close()   

if __name__ == "__main__":
    file_name = "lab.txt"
    file_name2 = "lab_scores.txt"
    num = int(input("Enter how many assignments, should each student have submitted: "))
    studentList = getFile (file_name)
    write_out (file_name2, studentList, num)





    
