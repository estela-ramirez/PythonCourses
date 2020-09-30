'''
ICS 31 Lab 3 Question 1
Driver: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
Navigator: UCI_ID: 69329009 Name: Karina Regalo
'''
def main():
    i = get_n_of_people()
    ns, ag = getsAgesAndNames(i)
    maxb, index = maxAge(ag)
    minb, index2 = minAge(ag)
    s = sumAge(ag)
    printOldestYoungestAverage(index,index2,s,i,ns,ag)

def get_n_of_people():
    return int(input("Number of people: "))

def getsAgesAndNames(number_of_people)->list:
    a =[]
    b =[]
    for x in range(1, number_of_people+1):
        name = input("What is Person #{}'s name: ". format(x))
        a.append(name)
        age = int(input("What is {}'s age? ". format(name)))
        b.append(age)
    return a, b
 
def maxAge(b:list)->int:
    maxb = 0
    for x in b:
        if x >= maxb:
            maxb = x
    index = (b.index(maxb))
    return maxb, index

def minAge(b:list)->int:
    minb = 100000000000
    for x in b:
        if x <= minb:
            minb = x
    index = (b.index(minb))
    return minb, index         

def sumAge(b:list)->int:
    for x in (b):
        sumb = sum(b)
        

def printOldestYoungestAverage(ma,mia,ta,np,ns,ag):
    print( ns[mia], "is the youngest and is", ag[mia], "years old")
    print( ns[ma], "is the oldest and is ", ag[ma], "years old")
    print("Average Age is:",(sum(ag)/len(ag)))
    
main()























