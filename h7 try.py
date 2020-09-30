class Contact:
    Name = None
    Number = None
    Email = None
    Note = None

def makeContact(Name:str, Number:str, Email:str, Note:str) -> Contact:
    c = Contact()
    c.Name = Name
    c.Number = Number
    c.Email = Email
    c.Note = Note
    return c
    
def present_menu():
    print("Rolodex Commands: Insert(I), Remove(R), Lookup By Name(F), Lookup by Phone Number(N), ")
    print("Lookup by Email(E), Save(S), Quit and Save(Q), Print All(P), Quit and Don't Save(X) ")
    
def get_command() -> str:
    return input("Please enter your command: ").strip().upper()

def print_dict(d:dict): 
    for key in d:
        print("\n")
        print("Name:" , d[key].Name , "\n" , "Phone Number:" ,
              d[key].Number , "\n" , "Email:" , d[key].Email , "\n" , "Note:" , d[key].Note, sep = "")
        print("\n")

def command_I(d: dict, cmd: str):
    print("\n")
    name = input("Enter the Contact's Name: ")
    num = input("Enter the Contact's Phone Number: ")
    mail = input("Enter the Contact's Email: ")
    note = input("Enter a Note about the Contact: ")
    contact = makeContact(name, num, mail, note)
    d[name] = contact
    print("\n")

def command_F(d: dict, cmd: str):
    print("\n")
    name = input("Enter the Name of the Contact, which you want to lookup: ")
    if name in d:
        print("Name:",d[name].Name,"\n","Phone Number: ",d[name].Number,
              "\n", "Email: ",d[name].Email,"\n","Note: ",d[name].Note, sep = "")
        print("\n")
        
def command_N(d: dict, cmd: str):
    print("\n")
    number = input("Enter the Phone Number of the Contact that you want to lookup: ")
    for key in d:
        if d[key].Number == number:
            print("Name:", d[key].Name, "\n", "Phone Number: ",d[key].Number,
              "\n", "Email: ",d[key].Email, "\n","Note: ", d[key].Note, sep = "")
            print("\n")
            
                 
def command_E(d: dict, cmd: str):
    print("\n")
    email = input("Enter the Email of the Contact that you want to lookup: ")
    for key in d:
        if d[key].Email == email:
            print("Name:", d[key].Name, "\n", "Phone Number: ",d[key].Number,
              "\n", "Email: ",d[key].Email, "\n","Note: ", d[key].Note, sep = "")
            print("\n")

        
def command_R(d: dict, cmd: str):
    print("\n")
    name = input("Enter the Name of the Contact, which you want to delete: ")
    if name in d:
        del d[name]
    print("Record Deleted")
    print("\n")
        
def command_P(d: dict, cmd: str):
    print_dict(d)
        
##def command_L(d: dict, cmd: str):
##    w = input("Rolodex name (current default is default.rol): ")
##    if w == '':
##        file = open("default.rol.txt", "r")
##        for line in file.readlines():
##            linesplit = line.split()
##            na =linesplit[0]
##            num = linesplit[1]
##            mail = linesplit[2]
##            no = linesplit[3]
##            contact = makeContact(na, num, mail, no)
##            d[na] = contact
##        file.close
##        print("Contacts added from default.rol ", "\n")
##    else:
##        file = open(w, "r")   
##        for line in file.readlines():
##            linesplit = line.split()
##            na = linesplit[0]
##            num = linesplit[1]
##            mail = linesplit[2]
##            no = linesplit[3]
##            contact = makeContact(na, num, mail, no)
##            d[na] = contact 
##        file.close()
##        print("Contacts added from", w, "\n")
'''
def default_file(file:str, d:dict): #have to remove commas
    file = open(file, "r")
    for line in file.readlines():
        linesplit = line.split()
        na =linesplit[0]
        num = linesplit[1]
        mail = linesplit[2]
        no = linesplit[3]
        contact = makeContact(na, num, mail, no)
        d[na] = contact
    file.close
    

def user_file(file:str, d:dict): #have to remove commas  #strip whitespace
    file = open(file, "r")   
    for line in file.readlines():
        linesplit = line.split()
        na = linesplit[0]
        num = linesplit[1]
        mail = linesplit[2]
        no = linesplit[3]
        contact = makeContact(na, num, mail, no)
        d[na] = contact 
    file.close()
'''






    
def command_S(d: dict, cmd: str):
    w = input("Save contacts to which file (default is default.rol): ")
    if w == '': 
        file = open("default.rol.txt", "w")
        for key in d:
            file.write(str(d[key].Name) + '\t'+ str(d[key].Number) + '\t' + str(d[key].Email) + '\t' + str(d[key].Note) + "\n")
        file.close()
        print("\n")
        print("Beginning Save"+"\n"+"Save Complete"+"\n")
        
    else: 
        file_2 = open(w, "w")
        for key in d:
            file_2.write(str(d[key].Name) + '\t' + str(d[key].Number) + '\t' + str(d[key].Email) + '\t' + str(d[key].Note) + "\n")
        file_2.close
        print("\n")
        print("Beginning Save"+"\n"+"Save Complete"+"\n")    

def main():
    d = {}
    print("The Rolodex program allows editing of named Rolodex files. ")
    print("If you specify a file that does not exist, the program will create it when saving. ", "\n")
    file_name = input("Please enter the name of the Collection File(.col) to Load and Save to: ")      
        
    
    while True:
        present_menu()
        cmd = get_command()
##        try:
##            if file_name == '':
##                default_file("default.col.txt", d)#
##            else:
##                user_file(file_name, d)#
##        except FileNotFoundError as e:
##            print("\n")
##            print(e)
##            print("Invalid File" + "\n")
##            error_file = input("Please enter the name of the Collection File(.col) to Load and Save to: ")
##            
        if cmd == "I":
            command_I( d, cmd)
        elif cmd == "F":
            command_F( d, cmd)
        elif cmd == "N":
            command_N( d, cmd)
        elif cmd == "E":
            command_E( d, cmd)
        elif cmd == "R":
            command_R( d, cmd)
        elif cmd == "P":
            command_P( d, cmd)
        elif cmd == "S":
            command_S( d, cmd)
        elif cmd == "Q":
            command_S( d, cmd)
            break
        elif cmd == "X": 
            break
        else:
            print("Invalid command")        
main()        


