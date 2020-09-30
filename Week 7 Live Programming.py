Class Student:
    Name = None
    Quizzes = None

def makeStudent(name:str)->Studnet:
    s = Student
    s.Name = Name
    s.Quizzes = []
    return s

def find_student(name:str, L:list)-> Student: #can not have an else
    for student in L:
        if student.Name == Name:
            return student
        a = makeStudent(Name) #if not in there, it will be added to list
	L.append(a) 
	return a
    
def add_quiz(name:str, quiz:int, L:list):
    student = findStudent(name, l)
    student.Quizzes.append(quiz)


def load_quiz_scores(file_name:str, L:list):
    open_file = open(file_name, "r")
    for line in open_file:
        line = line.split()
        name = line[0]
        quiz = line[2]
        add_quiz(name, quiz, L)
    open_file.close()

def cal_quiz_ave_with_lowest_dropped(L:list)->float:##??
    lowest_quiz = L[0]
    for quiz in L:
        if quiz < lowest_quiz:
            lowest_quiz = quiz
        avg=(sum(L)-min(L))/(len(L)-1)
	return avg

def save_quiz_averages(file_name:str, L):
    open_file = (file_name, "w")
    for student in L:
        avg= calc_quiz_ave_with_lowest_dropped(student.Quizzes)
        file.write(student.Name+" "+str(avg)+"\n")
    file.close()

def main():
    student_list= []
	load_quiz_scores ("Quizzes.txt",student_list)
	save_quiz_avergaes("QuizAve.txt",student_list)
main()
    
