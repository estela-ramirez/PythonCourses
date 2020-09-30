class Student:
    name = None
    quiz = None


def make_student(name: str, quiz:int) -> Student:
    s = Student()
    s.name = name
    s.quiz = quiz
    return s

def load_students(file_name:str)->dict:
    students = {}
    file = open(file_name, "r")
    for line in file.readlines():
        line = line.split()
        name = line[0]
        quiz = int(line[1])
        s = make_student(name, quiz)
        if name in students:
            students[name].append(s)
        else:
            students[name] = [s]
    file.close()
    return students
    

def avg_quiz_score_by_name(name:str, students)->float:
    avg = 0
    for student in students[name]:
        avg += student.quiz
        avg = avg/ len(students[name])
    return avg

def print_avg_score_by_name(students:dict):
    for name in sorted(students.keys()):#key or name
        avg = avg_quiz_score_by_name(name, students)
        print(key, "ave", avg)

def main():
    file_name = input("File:")
    students = load_students(file_name)
    print_avg_score_by_name(students)
main()
    


            
    
