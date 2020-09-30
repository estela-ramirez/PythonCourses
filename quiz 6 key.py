
class Student:
	name = None
	scores = None

def make_student(name: str) -> Student:
	s = Student()
	s.name = name
	s.scores = []
	return s

def find_student(name: str, students: dict) -> Student:
	if name not in students:
		s = make_student(name)
		students[name] = s
	else:
		s = students[name]
	return s

def add_exam(name: str, score: int, students: dict):
	s = find_student(name, students)
	s.scores.append(score)

def load_exam_scores(file_name: str, students: dict):
	open_file = open(file_name,"r")
	for line in open_file:
		trio = line.split()
		add_exam(trio[0], int(trio[2]), students)
	open_file.close()

def calc_exam_ave_with_lowest_dropped(scores: list) -> float:
	return (sum(scores) - min(scores)) / (len(scores) - 1)

def print_name_and_exam_averages(file_name: str, students: dict):
	file = open(file_name,"r")
	for line in file:
		name = line.strip()
		s = find_student(name, students)
		print(name, calc_exam_ave_with_lowest_dropped(s.scores))
	file.close()

def main():
	students = {}
	load_exam_scores("exams.txt", students)
	print_name_and_exam_averages("names.txt", students)

main()
