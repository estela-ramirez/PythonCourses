'''
def add_final(name:str, final:int, student_list:list):
    student = find_student(name, student_list)
    student.final_scores(final)
    
def get_final_scores(final_file:str, stduent_list)->list:
    #have to do it differently because not appending to a list, but a class
    open_file = open(final_file, "r")
    for line in open_file.readlines():
        line = line.split()
        name = line[0]
        fscore = line[1]
        add_finlal(name, final, student_list)
    open_file.close()

    
def add_hw(name:str, hw:int, student_list:list):
    student = find_student(name, student_list)
    student.hw_scores(hw)

def get_hw_scores(hw_file:str, student_list:list):
    open_file = open(hw_file, "r")
    for line in open_file.readlines():
        line = line.split()
        name = line[0]
        hw = line[2]
        add_hw(name, hw , student_list)
    open_file.close()      

def cal_hw_avg_with_lowest_dropped(student_list:list)->float:
    lowest_hw = student_list[0]
    for hw in student_list:
        if hw < lowest_hw:
            lowest_hw = hw:
                total =  (sum(student_list)-(lowest_hw))
                avg = total/(len(stduent_lsit)-1) # get length from file
                return avg 



  
def add_quiz(name:str, quiz:int, student_list:list):
    student = find_student(name, student_list)
    student.quiz_scores(quiz)
    
def get_quiz_scores(quiz_file:str, student_list:list):
    open_file = open(quiz_file, "r")
    for line in open_file.readlines():
        line = line.split()
        name = line[0]
        quiz = line[2]
        add_quiz(name, quiz, student_list)
    open_file.close()

def cal_quiz_avg_with_lowest_dropped(student_list:list)->float:
    lowest_quiz = student_list[0]
    for quiz in student_list:
        if quiz < lowest_quiz:
            lowest_quiz = quiz:
                total =  (sum(student_list)-(lowest_quiz))
                avg = total/(len(stduent_lsit)-1) # get length from file
                return avg 
'''

def cal_lab_score_with_lowest_dropped(student_list:list)->float:    
    lowest_lab = student_list[0]
    for lab in student_list:
        if lab < lowest_lab:
            lowest_lab = lab
            total =  (sum(student_list)-(lowest_lab))
            avg = total/(len(stduent_lsit)-1) # get length from file
            score = (avg * .25)
            return score



        
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

def output_scores(new_file:str, student_list:list, gb):



##        get_hw_scores("hw.txt", gb)
##        get_quiz_scores("quiz.txt", gb)
##        get_final_scores("final.txt", gb) 
