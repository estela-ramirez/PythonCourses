'''
ICS 31 Lab 3 Question 2
Driver: UCI_ID:69329009 Name: Karina Regalo
Navigator: UCI_ID: 18108714 Namme:Estela Ramirez Ramirez
'''
def main(): 
    i=get_n_of_tests()
    score_list = assign_grade(record_tests(i))
'''
    sumScores(num_of_tests)#fix
'''    


def get_n_of_tests():
    return int(input("Enter the number of Tests to be entered: "))

def record_tests(num_of_tests)->list:
    score_list=[]
    for x in range(1, num_of_tests+1):
        num_of_tests=int(input("Enter a test score: "))
        score_list.append(num_of_tests)
    return score_list
    

def assign_grade(score_list:list)->str:
    for x in range(0, len(score_list)):
        if x >=97:
            x == "A+"
        elif x >=93:
            x == "A"
        elif x>=90:
            x=="A-"
        elif x>=87:
            x=="B+"
        elif x>=83:
            x=="B"
        elif x>=80:
            x=="B-"
        elif x>=77:
            x=="C+"
        elif x>=73:
            x=="C"
        elif x>=70:
            x>="C-"
        elif x>=67:
            x=="D+"
        elif x>=63:
            x=="D"
        elif x>=60:
            x=="D-"
        elif x<60:
            x=="F"
    print(score_list[x])
    return score_list[x]
'''        
#outputs the test number and its score
def sumScores(num_of_tests):
    for x in range(1, num_of_tests+ 1):
        print("Test #{} the score is". format(x), num_of_tests)
'''
'''
sumscores = sum(score_list)/len(score_list) #int object is not iterable
print("The Average was:", sumscores)
'''
main()
'''
Test # 0 the grade is  A+
Test # 1 the grade is  A+
Test # 2 the grade is  A
Test # 3 the grade is  C+
Test # 4 the grade is  B
'''
