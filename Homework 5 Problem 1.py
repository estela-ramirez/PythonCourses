"""
ICS 31 Homework 5 Problem 1
Author: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
"""
def isPalindrome(txt:str)->bool:
    inverse_string = txt[::-1]
    if txt == inverse_string:
        return True
    else:
        return False

def getPalindrome(txt:str)->str:
    if isPalindrome(txt):
        return "Is_Palindrome"
    else:
        return "Not_Palindrome"

def count_substring(txt:str, sub_string:str)->int:        
    file = open("strings.txt", "r")
    count = txt.count(sub_string)
    return count
    file.close()
             
def build_output(File, sub_string)->list: 
    List = []
    for txt in File.readlines():
        s = count_substring(txt.strip(), sub_string) 
        n = str(s)
        p = getPalindrome(txt.strip())
        List.append(txt.strip() + "\n"+ "\n" + "Sub_String_Count:\t" + n + "\t" + p + "\n" +"\n") 
    return List       

def readfile(file:str, sub_string:str): 
    while True:
        try:
            file = open("strings.txt", "r")
            break
        except FileNotFoundError as e:
            print("FileNotFoundError( Error Number =", e.errno, "):", e.strerror)
            file_name = input ("Input Valid File Name:")
    List = build_output(file, sub_string)
    file.close ()
    return List
       
def print_to_file(New_File, output_data:list): 
    for x in output_data:
        New_File.write(x)
    return x

def write_results(file:str, output_data:list):
    New_File_write = open("string_stats.txt", "w")
    print_to_file(New_File_write, output_data)
    New_File_write.close()

if __name__ == "__main__":
    sub_string = input("Three Letter Substring to Find: ")
    output_data = readfile("strings.txt", sub_string)
    write_results("strings.txt", output_data)
