class Student():
    name = None
    quiz = None

def make_student(name:str, quiz:int) -> Student:
    s = Student()
    s.name = name
    s.quiz = quiz
    return s

def load_students(file_name:str):
    file = open(file_name, "r")
    students = {}
    for line in file:
        line = line.split()
        name = line[0]
        quiz = line[1] #
        s = make_student(name, int(quiz))
        if name in students:
            students[name].append(s)
        else:
            students[name] = [p]
    file.close()
    return students

def avg_quiz_score_by_name(name:str, students:dict)->int:
    avg = 0
    for student in students[name]:
        avg += s.quiz
        avg = avg/ len(students[name])
    return avg

def print_avg_score_by_name(students:dict):
    for key in sorted(students.keys()):
        for value in students[key]:
            avg = avg_quiz_score_by_name(value.name,students)
            print("The Average Score for", value ,"was", str(avg))

def main():
    file_name = input("File Name:")
    students = load_students(file_name)
    print_avg_score_by_name(students)
main()
        
    
