class Student:
   Name = None
   Quiz = 0

def make_student(name, quiz):
   s = Student()
   s.Name = name
   s.Quiz = quiz
   return s

def load_students(file_name):
   my_file = open(file_name, "r")
   students = {}
   
   for line in my_file:
       fields = line.split()
       s = make_student(fields[0],float(fields[1]))
       if fields[0] in students:
           students[fields[0]].append(s)
       else:
           students[fields[0]] = [s]
 
   my_file.close()
   return students

def avg_quiz_score_by_name(name, students):
   avg = 0
   for student in students[name]:
           avg += student.Quiz
   return avg / len(students[name])


def print_avg_score_by_name(students):
   for key in sorted(students.keys()):
      for s in students[key]:
          print("The Average Score for", s.Name ,"was", avg_quiz_score_by_name(s.Name,students))

def main():
   in_file   = input("Enter the input File Name: ")
   students  = load_students(in_file)
   print_avg_score_by_name(students)
main()
