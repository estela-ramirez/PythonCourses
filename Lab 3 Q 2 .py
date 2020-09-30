'''
ICS 31 Lab 3 Question 2
Driver: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
Navigator: UCI_ID: 69329009 Name: Karina Regalo
'''
def main():
    i = get_n_of_tests()
    sl = record_tests(i)
    g = assign_test_scores(sl)
    output_test_scores(g,sl)

def get_n_of_tests():
    return int(input("Enter the number of Tests to be entered: "))

def record_tests(num_of_tests)->list:
    test_scores_list=[]
    for x in range(1, num_of_tests):           
        if (test_scores >= 93) ==True:
            test_scores = "A"
            test_scores_list.append(test_scores)
            
        elif (test_scores >= 90) ==True:
            test_scores = "A-"
            test_scores_list.append(test_scores)
            
        elif (test_scores >= 87) ==True:
            tets_scores = "B+"
            test+scores_list.append(test_scores)
            
        elif (test_scores >= 83) ==True:
            test_scores = "B"
            test_scores_list.append(test_scores)
            
        elif (test_scores >= 80) ==True:
            test_scores = "B-"
            test_scores_list.append(test_scores)
            
        elif (test_scores >= 77) ==True:
            test_scores = "C+"
            test_scores_list.append(test_scores)
            
        elif (test_scores >= 73) ==True:
            test_scores = "C"
            test_scores_list.append(test_scores)
            
        elif (test_scores >= 70) ==True:
            test_scores = "C-"
            test_scores_list.append(test_scores)
            
        elif (test_scores >= 67) ==True:
            test_scores = "D+"
            test_scores_list.append(test_scores)
            
        elif (test_scores >= 63) ==True:
            test_scores = "D"
            test_scores_list.append(test_scores)
            
        elif (test_scores  >= 60) ==True:
            test_scores = "D-"
            test_scores_list.append(test_scores)
            
        elif (test_scores < 60) ==True:
            test_scores = "F"
            test_scores_list.append(test_scores)

        return test_scores_list

def output_test_scores(g,sl):
    for x in range(0,len(g)):
        print("Test #{} the grade is".format(x), g[x]) # only prints out for 0
    print("The Average Score was:", (sum(sl)/len(sl)))

main()







