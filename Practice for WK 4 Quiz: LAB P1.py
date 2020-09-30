def main():
    number_of_people = int(input("Number of People: "))
    ages, names = getAgesAndNames(number_of_people)
    maxA, index = maxAge(ages)
    minA, index = minAge(ages)
    totalsum = sumAge(ages, number_of_people)
    printOldestAndYoungestAverage

def getAgesAndNames(number_of_people)->list:
    names = []
    ages = []
    for x in range(1, number_of_people+1):
        na = input("What is Person #{}'s Name:".format(x))
        names.append(na)
        ag = int(input("What is {}'s age:? ". format(na)))
        ages.append(ag)
        return names, ages

def maxAge(ages:list)->int:
    maxA = 0
    for x in ages:
        if x >= maxA:
            maxA = x
        index = (ages.index(maxA))
        return maxA, index
    
def minAge(ages:list)->int:
    minA = 1000000000
    for x in ages:
        if x <= minA:
            minA = x
        index = (ages.index(minA))
        return minA, index

def sumAge(ages, number_of_people):
    for x in ages:
        totalsum = sum(ages)
        return totalsum

def printOldestAndYoungestAverage(max_age, min_age, total_age, number_of_people, names, ages):
    print(names[minA], "is the youngest and is", ages[minA], "years old")
    print(names[maxA], "is the oldest and is", ages[maxA], "years old")
    print("Average Age is: ", (totalsum/len(ages)))

main()
   
































