result = []

def values():
    #can put result back in
    while True:
        quest = input("Enter a test score to add to the list or type 'quit' to exit: ")
        if quest == "'quit'":
            break
        result.append(int(quest))
    return result #can take this out
#can just put print into this

(values())

def average()->int:
    return result
print("The Average score is", sum(result)/len(result))
(average())


(sum(result)/float(len(result)))

###Fiixed#####

def get_values()->list:
    L = []
    while True:
        ask = input("Enter a test score to add to the list or type 'quit' to exit: ")
        new = ask.lower().strip()
        if new == "'quit'":
            break
        else:
            L.append(ask)
    return L

def calculate(L:list)->float:
    total = 0
    for x in L:
        total += int(x)
    ave = total/len(L)
    return ave
        

def main():
    L = get_values()
    print("The average is", calculate(L))
main()





            

