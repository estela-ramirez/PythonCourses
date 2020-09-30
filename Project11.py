from pathlib import Path

def change_input_to_path(cmd:str)->str:
    cmd = cmd[1:]
    cmd = cmd[1:]
    cmd_path = Path(cmd)
    return cmd_path

def slice_two(cmd:str)->str:
    cmd = cmd[1:]
    cmd = cmd[1:]
    return cmd
      
def check_if_D_or_R_exists_or_not(cmd:str)->bool: 
    cmd_path = change_input_to_path(cmd)
    if cmd_path.exists():
        return True
    else:
        return False
    
def check_if_D_or_R_is_dir_or_not(cmd:str)->bool: 
    cmd_path = change_input_to_path(cmd)
    if cmd_path.is_dir():
        return True
    else:
        return False


def get_cmd_and_check_it()->str:
    cmd = input()
    while True:
    
        if len(cmd) < 3:
            print("ERROR")
            cmd = input()
        elif (cmd[0]!="D" and cmd[1]!=' ') or (cmd[0]!="R" and cmd[1]!=' '):
            print("ERROR")
            cmd = input()
        elif check_if_D_or_R_exists_or_not(cmd) is False:
            print("ERROR")
            cmd = input()
        elif check_if_D_or_R_is_dir_or_not(cmd) is False:
            print("ERROR")
            cmd = input()
        else:
            return cmd
            

def print_dir_paths_if_input_is_D(cmd_path:str):
    cmd_list = sorted(list(cmd_path.iterdir()))
    for x in cmd_list:
        if x.is_dir():
            pass
        else:
            print(x)

##def make_list_for_D(cmd:str)->list:
##    L = []
##    cmd_list = sorted(list(cmd_path.iterdir()))
##    for x in cmd_list:
##        if x.is_dir():
##            pass
##        else:
##            L.append(x)
##    return L


def print_if_input_is_R(cmd_path:str):
    for x in cmd_path.iterdir():
        if x.is_dir():
            print_if_input_is_R(x)
        else:
            print(x)

##def make_list_for_R(cmd:str)->list:
##    L = []
##    for x in cmd_path.iterdir():
##        if x.is_dir():
##            print_if_input_is_R(x)
##        else:
##            print(x)
##            L.append(x)
##    return L

           
def print_for_D_or_R():
    cmd = get_cmd_and_check_it()
    cmd_path = change_input_to_path(cmd)   
    if cmd[0] == "D":
        print_dir_paths_if_input_is_D(cmd_path)
    if cmd[0] == "R":
        print_if_input_is_R(cmd_path)

##def return_list_for_D_or_R(cmd:str)->list:
##    cmd = get_cmd_and_check_it()
##    cmd_path=change_input_to_path(cmd)
##    if cmd[0]=="D":
##        return make_list_for_D(cmd_path)
##    else:
##        return make_list_for_R(cmd_path)
        

 
def if_input_is_N_check_if_Valid_filename_or_not(narrow_input:str,L:list)->bool:
    narrow_input_path = change_input_to_path(narrow_input)
 
  
    
    if narrow_input_path.is_file():##### not a Path yet
        return True
    else:
        return False
   
def get_input_to_narrow_search()->str:
    possible_input_list = ["N", "E", "T", "<", ">"]
    narrow_input = input()
    while True:
        if len(narrow_input) < 4:
            print("length")
            narrow_input = input()
        elif narrow_input[0] not in possible_input_list or narrow_input[1] != " ":
            print("first two characters")
            narrow_input = input()
        elif slice_two(narrow_input) == "":
            print("empty after second characters")
            narrow_input = input()
        elif narrow_input[0] == "N":#################
            if if_input_is_N_check_if_Valid_filename_or_not(narrow_input) is False:
                print("Invalid")
                narrow_input = input() 
        elif narrow_input[0] == "<" or ">":
            try:
                n = int(slice_two(narrow_input))
            except ValueError:
                print("not numbers")
                narrow_input = input()
            else:
                if n < 0:
                    print("less than 0")
                    narrow_input = input()
        else:##stops working after this
            print(narrow_input)
            return narrow_input

def main():
    print_for_D_or_R()
    get_input_to_narrow_search()
                  

if __name__ == '__main__':
    main()





 
