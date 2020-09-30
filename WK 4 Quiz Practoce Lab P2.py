def main():
    num_of_tests = int(input("Enter the number of Tests to be entered: "))
    gradeList = record_tests(num_of_tests)
    output_grades(test_scores)

def record_tests(num_of_tests):
    testScores = []
    for x in range(num_of_tests):
        scores = float(input("Enter a test score: "))
        testScores.append(scores)
    return testScores

def assign_grade(testScores:list)->str:
    gradeList = []
    for x in range(testScores):
        if x >= 97:
           x = "A+"
           gradeList.append(x)

def output_grades(test_scores):
    for x in range(len(scoreList)):
        print("Test #{} the grade is".format(x), scoreList[x])
    average was sum
    

main()

 

Write a function output_grades(test_scores)
Outputs the test number and its score.

Test # 0 the grade is  A+
Test # 1 the grade is  A+
Test # 2 the grade is  A
Test # 3 the grade is  C+
Test # 4 the grade is  B
The Average Score was : 91.0
>>> 

