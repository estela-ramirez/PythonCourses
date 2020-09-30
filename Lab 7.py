'''
ICS 31 Lab 7  Problem 1
Driver:  UCI_ID: 18108714  Name: Estela Ramirez Ramirez
'''
class Student:
    name = None
    lab_scores = None
    hw_scores = None
    quiz_scores = None
    final_scores = 0 
    course_total = 0
    letter_grade = None

def make_Student(name:str)->Student:
    s =Student
    s.name = name
    s.lab_scores = []
    s.hw_scores = []
    s.quiz_scores = []
    s.final_scores = 0 
    s.course_total = 0
    s.letter_grade = ""
    return s

class Gradebook:
    student_roster = None
    quizzes_assigned = 0
    hw_assigned = 0
    labs_assigned = 0

#maybe don't need parameters
#student_roster:list, quizzes_assigned:int, hw_assigned:int, labs_assigned:int
def make_Gradebook(student_roster:list, quizzes_assigned:int, hw_assigned:int, labs_assigned:int)->Gradebook:
    gb = Gradebook()
    gb.student_roster = []
    gb.quizzes_assigned = quizzes_assigned 
    gb.hw_assigned = hw_assigned
    gb.labs_assigned = labs_assigned
    return gb

def find_student(name:str, gb:Gradebook)->Student:
    for student in gb.student_roster:
        if student.name == name:
            return student
    student = make_Student(name)
    gb.student_roster.append(student)
    return student


def get_lab_scores(lab_file:str, gb:Gradebook):
    open_file = open(lab_file, "r")
    first_line = open_file.readline()
    gb.labs_assigned = int(first_line)
    for line in open_file.readlines():
        line = line.split()
        name = line[0]
        lab = int(line[2])
        student = find_student(name, gb)
        student.lab_scores.append(lab)
        print(student.lab_scores)
    open_file.close()
    
    
def get_hw_scores(hw_file:str, gb:Gradebook):
    open_file = open(hw_file, "r")
    first_line = open_file.readline()
    gb.hw_assigned = int(first_line)
    for line in open_file.readlines():
        line = line.split()
        name = line[0]
        hw = int(line[2])
        student = find_student(name, gb)
        student.hw_scores.append(hw)
    open_file.close()      

  
def get_quiz_scores(quiz_file:str, gb:Gradebook):
    open_file = open(quiz_file, "r")
    first_line = open_file.readline()
    gb.quizzes_assigned = int(first_line)
    for line in open_file.readlines():      
        line = line.split()
        name = line[0]
        quiz = int(line[2])
        student = find_student(name, gb)
        student.quiz_scores.append(quiz)
    open_file.close()
 
    
def get_final_scores(final_file:str, gb:Gradebook)->list:
    open_file = open(final_file, "r")
    for line in open_file.readlines():
        line = line.split()
        name = line[0]
        final = int(line[1])
        student = find_student(name, gb)
        student.final_scores = final
    open_file.close()


def cal_total_score_with_lowest_dropped(gb:Gradebook, student)->float:
    print(student.name)
    L = student.lab_scores
    H = student.hw_scores
    Q = student.quiz_scores
    F = student.final_scores
    print(L)####why is it an empty list?????
    print(H)
    print(Q)
    print(F)
      
    lab_score = float(((sum(L) - min(L)) / (gb.labs_assigned - 1))*.35)
    hw_score = float(((sum(H)- min(H))/ (gb.hw_assigned - 1))*.25)
    quiz_avg = float(((sum(Q)- min(Q))/ (gb.quizzes_assigned -1))*.25)
    final_score = float(F)*.15
    return sum(lab + hw + quiz + final)

    
def assign_letter_grades(score)->str:
    if (score >= 97.5):
        return "A+"
    elif (97.5 > score >= 93.5):
        return "A"
    elif (93.5 > score >= 90):
        return "A-"
    elif (90 > score >= 86.5):
        return "B+"
    elif (86.5 > score >= 83.5):
        return "B"
    elif(83.5 > score >= 80):
        return "B-"
    elif (80 > score >= 76.5):
        return "C+"
    elif (76.5 > score >= 73.5):
        return "C"
    elif (73.5 > score >= 70):
        return "C-"
    elif (70 > score >= 66.5):
        return "D+"
    elif (66.5 > score >= 63.5):
        return "D"
    elif (63.5 > score >= 60):
        return "D-"
    elif (score  < 60):
        return "F"            




def assignment_filler(gb, student):
    while len(student.hw_scores) < gb.num_of_hw_assigned:
        student.hw_scores.append(0)
    while len(student.lab_scores) < gb.num_of_labs_assigned:
        student.lab_scores.append(0)
    while len(student.quiz_scores) < gb.num_of_quizzes_assigned:
        student.quiz_scores.append(0)

        
def fill_in_computed_course_totals_and_grades_from_gradebook(gb):
    for student in gb.student_roster:
        assignment_filler(gb, student)#if they didn't do 4th assignment
        student.course_total = cal_total_score_with_lowest_dropped(gb, student)
        student.letter_grade = assign_grade(student.course_total)

    
def print_course_totals_and_letter_grades_to_file(file_name, gb):
    open_file = open(file_name, 'w')
    for student in gb.student_roster:
        fill_in_computed_course_totals_and_grades_from_gradebook(gb)
        file.write(student.name + '\t' + student.letter_grade + '\t' + student.course_total + '\n')
    open_file.close()

def main():
    gb = make_Gradebook([], 0, 0 , 0)
    try:
        get_lab_scores("lab.txt", gb)
        get_hw_scores("hw.txt", gb)
        get_quiz_scores("quiz.txt", gb)
        get_final_scores("final.txt", gb)
        fill_in_computed_course_totals_and_grades_from_gradebook(gb)
        print_course_totals_and_letter_grades_to_file("course_grades.txt", gb)
    except FileNotFoundError as e:
        print(e)
        print("File not found")                                 
    
if __name__ == "__main__":
    main()

##a = 1
##def test(b: int) -> int:
##    return b
##c = test(a)
##c = c + 1
##print(a)
##print()


##
##a = gb.student_roster.index(student)
##    return a
