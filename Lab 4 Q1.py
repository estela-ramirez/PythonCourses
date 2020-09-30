"""
ICS 31 Lab 4 Problem 1
Driver: UCI_ID: 31421979 Name: Emily Lee
Navigator: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
"""
'''
def open_file(file_name:str):
    open_file = open("Sample_Search_File.txt", "r")
    open_file.close()
'''

def open_file(file_name:str):
    if file == "Sample_Search_File-2.txt":
        open_file = open(file_name, "r")
    else:
        return
    for line in open_file:
        return line
    return file
   
    
def get_num_lines (file_name: str)-> int:
    x = open("Sample_Search_File.txt", "r")
    num = len(x.readlines())
    return num
    x.close()

def numWords (file:str)->int:
    file = open("Sample_Search_File.txt", "r")
    count = 0
    for line in file.readlines():
        count += len(line.split())
    return count
    file.close()

def numLetters(file:str)->int:
    file = open("Sample_Search_File.txt", "r")
    total = 0
    for letter in file.readlines():
        total = total + len(letter)
    return total
    file.close()

def main():
    file = input("Enter file name: ")
    lines = get_num_lines("Sample_Search_File.txt")
    words = numWords("Sample_Search_File.txt")
    letters = numLetters("Sample_Search_File.txt")
    print("There are", lines, "lines", words, "words, and", letters, "letters in", file)
    

if __name__=="__main__":
    main()



