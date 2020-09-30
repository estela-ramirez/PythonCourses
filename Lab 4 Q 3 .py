'''
ICS 31 Lab 4 Question 3
Driver: UCI_ID: 18108714 Name:Estela Ramirez Ramirez
Navigator: UCI_ID:31421979  Name:Emily Lee
'''

def main():
    num_of_students = get_num_of_students()
    name_list, id_list = get_info(num_of_students)
    open_file("roster.txt", name_list, id_list)
    print("roster.txt has been generated")

def get_num_of_students():
    num_of_students = int(input("How many students are in your class: "))
    return num_of_students

def get_info(num_of_students:int)->list:
    name_list = []
    id_list = []
    for x in range(1, num_of_students+1):
        name = input("Please enter the name of student #{}: ".format(x))
        name_list.append(name)
        iD = input("Please enter {}'s ID:  ".format(name))
        id_list.append(iD)
    return name_list, id_list
                           
def open_file(file_name:str, name_list, id_list): 
    open_file = open("roster.txt", "w")
    for x in range(len(name_list)):
       open_file.write(name_list[x]+"\t"+id_list[x]+"\n")
    open_file.close()

       
if __name__ == "__main__":
    main()
    
