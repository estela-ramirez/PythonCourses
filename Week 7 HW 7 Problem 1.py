'''
ICS 31 Homework 7  Problem 1
Driver:  UCI_ID: 18108714  Name: Estela Ramirez Ramirez
'''
def open_file(file_name:str, mode:str) -> 'file':
    file = open(file_name, mode)
    return file
        
def is_filename_valid(file_name:str) -> bool:
    if file_name[-4:] == ".col":
        return True
    else:
        return False

def get_FileName() -> str:
    while True:
        file_name = input("Please enter the name of the Collection File(.col) to Load and Save to: ")
        if is_filename_valid(file_name):
            return file_name
       
class Coin():
    Grade = None
    Value = 0
    Year = 0
    Country = ""
    Mint = ""

def make_coin(Grade:str, Value:float, Year:int, Country:str, Mint:str)-> Coin:
    c = Coin()
    c.Grade = Grade
    c.Value = Value
    c.Year = Year
    c.Country = Country
    c.Mint = Mint
    return c

def loadCollection(file_name:str, records:list) -> list:
    file = open_file(file_name, "r")
    for line in file.readlines():
        line  = line.strip("\n").split(",")
        grade = line[0]
        value = float(line[1])
        year = int(line[2])
        country = line[3]
        mint = line[4]
        coin = make_coin(grade, value, year, country, mint)
        records.append(coin)
    file.close()
    return records

def present_menu():
    print("\n", "Coin Collection Commands: Insert(I), Lookup By Year(Y), Lookup by Country(C), ", sep = "")
    print("Lookup by Value(V), Save(S), Quit and Save(Q), Print All(P), Quit and Don't Save(X) ")

def get_command()->str:
    cmd_list = ["I", "Y", "C", "V", "S", "Q", "P", "X"]
    while True:
        cmd = input("Please enter your command: ").strip().upper()
        if cmd in cmd_list:
            return cmd
            break
        else: 
            print(cmd ," is not a valid command. Valid Coin Collection Commands are:", sep = "")    

def getGrade(grades:str) -> str:#needs to be upper??????
    while True:
        grade = input("Enter the Coin's Grade: ")  
        if grade in grades:
            return grade
            break
        else:
            print("Invalid Grade")


def getValue() -> float:#what if they input letters
    while True:
        value = input("Enter the Coin's Value: ")
        negative = "-"
        if negative in value:
            print("Invalid Value")
        else:
            return float(value)
            break

def getYear() -> int:#what if they input letters
    while True:
        year = input("Enter the Coin's Year of Production: ")
        negative = "-"
        if negative in year:
            print("Invalid Year")
        else:
            return int(year)
            break

def getCountry() -> str:
    while True:
        country = input("Enter the Coin's Country of Origin: ")
        if country == "":
            print("\nNo Country Entered")
        else:
            return country
            break

def getMint() -> str:
    while True:
        mint = input("Enter the Coin's Mint: ")
        if mint == "":
            print("\nNo Mint Entered")
        else:
            return mint
            break

def insertCoin(records:list, grades:str):
    grade = getGrade(grades)
    value = getValue()
    year = getYear()
    country = getCountry()
    mint = getMint()
    coin = make_coin(grade, value, year, country, mint)
    records.append(coin)

def lookUpByYear(records:list) -> int: ##what if no matches
    print("\n")
    coin_number = 0
    year = input("Enter the desired Year: ")
    for coin in records:
        if int(year) == coin.Year:
            coin_number +=1
            print_coin(coin_number, coin)
       
def lookUpByCountry(records:list) -> int: #what if no matches
    print("\n")
    coin_number = 0
    country = input("Enter the Country of Origin to list coins from: ")
    for coin in records:
        if country == coin.Country:
            coin_number +=1
            print_coin(coin_number, coin)

def getCondition() -> str:
    while True:
        condition = input("Do you want to find coins with value >= (G) or <=(L) or == (E)\nPlease enter your selection: ")
        condition = condition.upper()
        return condition
       

def lookUpByValue(records:list) -> int: #what if no matches
    print("\n")
    value = float(input("Enter the Price to sort around: "))
    condition = getCondition()
    coin_number = 0
    for coin in records:
        if condition == "G":
            if value < coin.Value:
                coin_number += 1
                print_coin(coin_number, coin)
      
        elif condition == "L":
            if value > coin.Value:
                coin_number += 1
                print_coin(coin_number, coin)

        elif condition == "E": 
            if value == coin.Value:
                coin_number += 1
                print_coin(coin_number, coin)
            
def saveCollection(records:Coin , file_name:str): 
    file = open_file(file_name, "w") 
    for coin in records:
        file.write(coin.Grade + ',' + str(coin.Value) + ',' + str(coin.Year) + ',' + coin.Country + ',' + coin.Mint + '\n')
    file.close()
    print("\n","Beginning Save","\n","Save Complete","\n", sep = "")

def quitSave(records:Coin, file_name:str):
    saveCollection(records, file_name)
    import sys
    sys.exit(0)

def printAll(records:list):
    coin_number = 0
    for coin in records:
        coin_number +=1
        print_coin(coin_number, coin)
	
def exitNow():
    import sys
    sys.exit(0)

def print_coin(coin_number:int, coin:Coin):
    print("Coin #",coin_number)
    print("Grade: ", coin.Grade, "\n", "Value: " , coin.Value, "\n" , "Year: " ,
              coin.Year , "\n" , "Country of Origin: " , coin.Country  , "\n" , "Mint: " , coin.Mint, "\n", sep = "")

##def evaluate_command(cmd:str)
    
def main():
    records = []
    grades = ["Mint", "Fine", "Good", "Fair", "Poor"]
    print("The Coin Collection program can load an old Collection or create a new one. ")
    print("If you specify a file that does not exist then, the program will create it when saving. ")
    while True:
        file_name  = get_FileName()
        try:
            loadCollection(file_name, records)
            break
        except FileNotFoundError as e:
            print("\n", "File Does Not Exist", sep = "")
    while True:
        present_menu()
        cmd = get_command()
        if cmd  == "I":
            insertCoin(records, grades)
        elif cmd == "Y":
            lookUpByYear(records)
        elif cmd == "C":
            lookUpByCountry(records)
        elif cmd  == "V":
            lookUpByValue(records)
        elif cmd == "S":
            saveCollection(records, file_name)
        elif cmd  == "Q":
            quitSave(records, file_name)
        elif cmd  == "P":
            printAll(records)
        elif cmd == "X":
            exitNow()                 
main()


