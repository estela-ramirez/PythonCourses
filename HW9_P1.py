'''
ICS 31 Homework 9 Prblem 1
Driver: UCI_ID: 18108714 Name:EStela Ramirez Ramirez
'''
import string

class Character_Info():
    uppercase = 0
    lowercase = 0
    digit = 0
    punctuation = 0
    whitespace = 0

def make_character_info(uppercase:int, lowercase:int, digit:int, punctuation:int, whitespace:int):
    c =Character_Info()
    c.uppercase = uppercase
    c.lowercase = lowercase
    c.digit = digit
    c.punctuation = punctuation
    c.whitespace = whitespace
    return c
    
def isUpper(char_test:str) -> bool:
    if char_test in string.ascii_uppercase:
        return True
    else:
        return False

def isLower (char_test:str) -> bool:
    if char_test in string.ascii_lowercase:
        return True
    else:
        return False

def isDigit (char_test:str) -> bool:
    if char_test in string.digits:
        return True
    else:
        return False

def isPunctuation(char_test:str) -> bool:
    if char_test in string.punctuation:
        return True
    else:
        return False

def isWhitespace (char_test:str) -> bool:
    if char_test in string.whitespace:
        return True
    else:
        return False

def updateTally(char_test, c:Character_Info):
    
    if isUpper(char_test):
        c.uppercase += 1
        
    elif isLower(char_test):
        c.lowercase += 1
    
    elif isDigit(char_test):
        c.digit += 1
     
    elif isPunctuation(char_test):
        c.punctuation += 1
       
    elif isWhitespace(char_test):
        c.whitespace += 1
      
def assessFile(file_name:str, c) :
    file = open(file_name, "r")
    for line in file.readlines():
        a = list(line)
        for x in a:
            
            updateTally(x, c)
    file.close()
        

def main():
    c = make_character_info(0, 0, 0, 0, 0)
    file_name = input("Input a file name: ")
    assessFile(file_name, c)
    print("The File contained:\nUpper-Case:", " ", c.uppercase,
          "\nLower-Case:" , " ", c.lowercase ,
          "\nDigits:" ,  " ", c.digit ,
          "\nPunctuation:" ,  " ", c.punctuation ,
          "\nWhitespace:" , " ", c.whitespace, sep = "")

                      
if __name__ == "__main__":
    main()



