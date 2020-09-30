from pathlib import Path

def change_input_to_path(cmd:str)->str:
    cmd = cmd[1:]
    cmd = cmd[1:]
    cmd_path = Path(cmd)
    return cmd_path
      
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
    cmd = input("length: ")
    while True:
    
        if len(cmd) < 3:
            print("ERROR")
            cmd = input("Length: ")
        elif (cmd[0]!="D" and cmd[1]!=' ') or (cmd[0]!="R" and cmd[1]!=' '):
            print("ERROR")
            cmd = input("Not D or R : ")
        elif check_if_D_or_R_exists_or_not(cmd) is False:
            print("ERROR")
            cmd = input("DNE: ")
        elif check_if_D_or_R_is_dir_or_not(cmd) is False:
            print("ERROR")
            cmd = input("Not Dir: ")
        else:
            return cmd
            

def print_dir_paths_if_input_is_D(cmd:str):   
    cmd_path = change_input_to_path(cmd)
    cmd_list = sorted(list(cmd_path.iterdir()))
    for x in cmd_list:
        print(x)
    
def print_if_input_is_R(cmd:str):##recursive 
    print_dir_paths_if_input_is_D(cmd)
    #subdirectories
   

def print_for_D_or_R():
    cmd = get_cmd_and_check_it()
    if cmd[0] == "D":
        print_dir_paths_if_input_is_D(cmd)
    if cmd[0] == "R":
        print_if_input_is_R(cmd)
        
         
if __name__ == '__main__':
    print_for_D_or_R()
    

##def if_input_is_N_check_if_Valid_filename_or_not(narrow_input:str)->bool:
##    narrow_input_path = change_input_to_path(narrow_input)#might not want to change to Path?
##    if narrow_input_path.is_file():
##        return True
##    else:
##        return False
##
##
##    
##def get_input_to_narrow_search():
##    possible_input_list = ["N", "E", "T", "<", ">"]
##    narrow_input = input()
##    while True:
##        if len(narrow_input) < 3:
##            print("ERROR")
##            narrow_input = input()
##        elif narrow_input[0] not in possible_input_list or narrow_input[1] != " ":
##            print("ERROR")
##            narrow_input = input()
    

            
        
        






 
