
class Student:
    Name    = None
    HW      = 0
    Lab     = 0
    Quiz    = 0

s = Student() #Creates a default Student and assigns it to s
s.Name = "Apple"
print(s.Name)
print(s.HW)
print(s.Lab)
print(s.Quiz)

s.Quiz = 100
print(s.Name, "HW =", s.HW,"Lab =",  s.Lab, "Quiz =", s.Quiz)
s.Lab = 90
print(s.Name, "HW =", s.HW,"Lab =",  s.Lab, "Quiz =", s.Quiz)
s.HW = 50
print(s.Name, "HW =", s.HW,"Lab =",  s.Lab, "Quiz =", s.Quiz)
s.HW += 50
print(s.Name, "HW =", s.HW,"Lab =",  s.Lab, "Quiz =", s.Quiz)








#We can also write functions that create a student with some values for us
def makeStudent(Name, HW, Lab, Quiz):
    s = Student()
    s.Name  = Name
    s.Quiz  = Quiz
    s.Lab   = Lab
    s.HW    = HW
    return s

#We can make a list of Students

roster = []
roster.append(s)    #This adds Apple to our roster

#Lets add a nother student
roster.append(makeStudent("Cube", 90,90,90))

print(roster[1].Name, "HW =", roster[1].HW,"Lab =",  roster[1].Lab, "Quiz =", roster[1].Quiz)

#We can also change data for students, after they are in the list
roster[1].HW -= 5
print(roster[1].Name, "HW =", roster[1].HW,"Lab =",  roster[1].Lab, "Quiz =", roster[1].Quiz)

roster[1].HW += 15 
print(roster[1].Name, "HW =", roster[1].HW,"Lab =",  roster[1].Lab, "Quiz =", roster[1].Quiz)





#We can also make update functions such as
def modifyHW(student, increment):
    student.HW += increment


modifyHW(roster[1],15)
print(roster[1].Name, "HW =", roster[1].HW,"Lab =",  roster[1].Lab, "Quiz =", roster[1].Quiz)
#Now Cube has a 115 points in HW









