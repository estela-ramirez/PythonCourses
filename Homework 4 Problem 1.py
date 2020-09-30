'''
ICS 31 Homework 4 Problem 1
Author: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
'''

def transfer(source:str, destination:str):
    for line in source:
        destination.write(line)


def manage_transfer(source_name, destination_name):
    source_file = open(source_name, "r")
    source= source_file.readlines() 
    destination = open(destination_name, "w")
    transfer(source, destination)#calls function
    source_file.close()
    destination.close()

if __name__=="__main__":
    source_name = input("Enter the name of the source file for the copy: ")
    destination_name = input("Enter the name of the destination file for the copy: ")
    manage_transfer(source_name, destination_name)
    print("The Copy Operation is now complete", source_name, "has been copied to", destination_name)
    
    
