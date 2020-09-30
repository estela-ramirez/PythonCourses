"""
ICS 31 Lab 4 Problem 2
Driver: UCI_ID: 31421979 Name: Emily Lee
Navigator: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
"""

def open_file(file_name:str):
    if file == "Sample_Search_File.txt":
        open_file = open(file_name, "r")
    else:
        return
    for line in open_file:
        return line
    return file

def search_word(file_name:str, word:str)->int:
    file = open("Sample_Search_File.txt", "r")
    count = 0
    for line in file.readlines():
        x = line.split()
        print(x)
        for words in x:
            if words.lower() == word:
                count += 1
    return count
    file.close()

def main():
    name = input("What is the name of the file, we want to open? ")
    word = input("What word do you want to search for? ")
    num = search_word("Sample_Search_File.txt", word)
    print("The target word,",word,", occured", num, "times in the file")


if __name__=="__main__":
    main()

