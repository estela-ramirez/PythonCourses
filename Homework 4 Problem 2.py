'''
ICS 31 Homework 4 probelm 2
Author: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
'''
def isLeapYear(data:int)->str:
    if data % 4 == 0 and data % 100 != 0:
        return "Leap Year"
    elif data % 100 == 0 and data % 400 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"
        
def build_output(file:'file')->list:
    data = []
    read_file = file.readlines()
    for x in read_file:
        data.append(x.strip("\n") + " "+ isLeapYear(int(x.strip("\n")))+"\n")
        
    return data 
            
def build_out(name:str)->list: #a = data
    file = open(name, "r")
    a = build_output(file)
    file.close()
    return a 

def print_to_file(file:'file', data:list):
    for x in data:
        file.write(x)
    return x

def write_out(name:str, data:list):
    file = open(name, "w")
    print_to_file(file, data)
    file.close()

if __name__=="__main__":
    name = input("What is the name of the file, we want to open? ")
    a = build_out(name)
    write_out(name, a)
    print("Leap Year Augment complete")
    
    
