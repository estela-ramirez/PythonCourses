'''
ICS 31 Lab 3 Question 3
Driver: UCI_ID:18108714 Name:Estela Ramirez Ramirez
Navigator: UCI_ID:69329009 Name:Karina Regalo
'''

def main():
   i = get_info()
   continue_or_not(i)

def get_info():
    string_list = []
    letter = input("What letter do you want to count the number of occurences of: ")
    string = input("Enter the string you would like to search: ")
    for x in string:
        string_list.append(x)

    ct =0 
    
    for x in string_list:
        if x == letter:
            ct = ct + 1
    print("# of Occurences of", letter, "found are", ct)
    return ct #or get_info

def continue_or_not(i)->str: #need to do lower or upper for Y and N
    while True:
        ask = input("Do you wnat to continue? Yes(Y) or No(N):")
        ask = ask.upper()
        if ask == "Y":
            get_info()#calls back first function
        elif ask == "N": 
            break
        else:
            print("Your input was neither n or y, please enter n or y: ")
            

main()        





