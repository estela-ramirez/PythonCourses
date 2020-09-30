'''
ICS 31 LAb 5 Problem 1
Driver: UCI_ID:18108714 Name:Estela Ramirez Ramirez
Navigator: UCI_ID:50092987 Name:Uyen Tran
'''


def isint(num:str)->str:
    try:
        int(num)
        return ("Is_Int")
    except ValueError:
        return ("Not_Int")
        
def isfloat(num:str)->str:
    try:
        float(num)
        return ("Is_FLoat")
    except ValueError:
        return ("Not_Float")

def digit (num:str) ->str:
    numbers = "0123456789"
    is_int = isint (num)
    for x in num:
        if x in numbers and is_int == "Is_Int":
            return ("Is_All_Number")
        else:
            return ("Not_All_Number")
            
def build_output (File) ->list:
    text = File.readlines()
    buildList = []
    for num in text:
        x = isint (num.strip())
        y = isfloat (num.strip())
        z = digit (num.strip())
        buildList.append (num.strip() + "\t" + x + "\t" + y + "\t" + z + "\n")
    return buildList

def check_and_read_file(name:str):
    while True:
        try:
            open_file = open(name, "r")
            break
        except FileNotFoundError as e:
            print("FileNotFoundError( Error Number =", e.errno, "):", e.strerror)
            name = input("Input File Name: ")
    x = build_output(open_file)
    open_file.close ()
    return x

def print_to_file (File, data):
    for elm in data:
        File.write (elm)

def write_out (name, data):
    openWrite = open ("Stuff.txt", "w")
    print_to_file (openWrite, data)
    openWrite.close()

if __name__ == "__main__":
    name = input("Input File Name: ")
    data = check_and_read_file (name)
    write_out (name, data)
