'''
ICS 31 Lab 7  Problem 1
Driver:  UCI_ID: 18108714  Name: Estela Ramirez Ramirez
'''
class Student():
    name = None
    lab_scores = None
    hw_scores = None
    quiz_scores = None
    final_scores = 0 
    course_total = 0
    letter_grade = None

def make_Student(name:str)->Student:
    s =Student()
    s.name = name
    s.lab_scores = []
    s.hw_scores = []
    s.quiz_scores = []
    s.final_scores = 0 
    s.course_total = 0
    s.letter_grade = ""
    return s

class Gradebook():
    student_roster = None
    quizzes_assigned = 0
    hw_assigned = 0
    labs_assigned = 0

#maybe don't need parameters
def make_Gradebook()->Gradebook:
    gb = Gradebook()
    gb.student_roster = []
    return gb

def find_student(gb:Gradebook, name:str)->Student:
    for student in gb.student_roster:
        if student.name == name:
            return student
    student = make_Student(name)
    gb.student_roster.append(student)
    return student


def get_lab_scores(gb:Gradebook, lab_file:str):
    file = open(lab_file, "r")
    first_line = file.readline()
    gb.labs_assigned = int(first_line)
    for line in file.readlines():
        line = line.split()
        name = line[0]
        lab = int(line[2])
        student = find_student(gb, name)
        student.lab_scores.append(lab)
    file.close()
    
    
def get_hw_scores(gb:Gradebook, hw_file:str):
    file = open(hw_file, "r")
    first_line = file.readline()
    gb.hw_assigned = int(first_line)
    for line in file.readlines():
        line = line.split()
        name = line[0]
        hw = int(line[2])
        student = find_student(gb, name)
        student.hw_scores.append(hw)
    file.close()      

  
def get_quiz_scores(gb:Gradebook, quiz_file:str):
    file = open(quiz_file, "r")
    first_line = file.readline()
    gb.quizzes_assigned = int(first_line)
    for line in file.readlines():      
        line = line.split()
        name = line[0]
        quiz = int(line[2])
        student = find_student(gb, name)
        student.quiz_scores.append(quiz)
    file.close()
 
    
def get_final_scores(gb:Gradebook, final_file:str)->list:
    file = open(final_file, "r")
    for line in file.readlines():
        line = line.split()
        name = line[0]
        final = int(line[1])
        student = find_student(gb, name)
        student.final_scores = final
    file.close()

    
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


def cal_total_score_with_lowest_dropped(gb:Gradebook, student)->float:
    L = student.lab_scores
    H = student.hw_scores
    Q = student.quiz_scores
    F = student.final_scores
      
    lab_score = float(((sum(L) - min(L)) / (gb.labs_assigned - 1))*.35)
    hw_score = float(((sum(H)- min(H))/ (gb.hw_assigned - 1))*.25)
    quiz_score = float(((sum(Q)- min(Q))/ (gb.quizzes_assigned -1))*.25)
    final_score = float(F)*.15
    return lab_score + hw_score + quiz_score + final_score

        
def fill_in_computed_course_totals_and_grades_from_gradebook(gb:Gradebook):
    for student in gb.student_roster:
        #if the student did not do all assignments
        while len(student.hw_scores) < gb.hw_assigned:
            student.hw_scores.append(0)
        while len(student.lab_scores) < gb.labs_assigned:
            student.lab_scores.append(0)
        while len(student.quiz_scores) < gb.quizzes_assigned:
            student.quiz_scores.append(0)
        student.course_total = cal_total_score_with_lowest_dropped(gb, student)
        student.letter_grade = assign_letter_grades(student.course_total)

    
def print_course_totals_and_letter_grades_to_file(gb:Gradebook, file:str):
    open_file = open(file, 'w')
    for student in gb.student_roster:
        fill_in_computed_course_totals_and_grades_from_gradebook(gb)
        open_file.write(student.name + '\t' + str(student.letter_grade) + '\t' + str(student.course_total) + '\n')
    open_file.close()

def main():
    gb = make_Gradebook()
    try:
        get_lab_scores(gb, "lab.txt")
        get_hw_scores(gb, "hw.txt")
        get_quiz_scores(gb, "quiz.txt")
        get_final_scores(gb, "final.txt")
        fill_in_computed_course_totals_and_grades_from_gradebook(gb)
        print_course_totals_and_letter_grades_to_file(gb, "course_grades.txt")
    except FileNotFoundError as e:
        print(e)
        print("File not found")                                 
    
if __name__ == "__main__":
    main()
