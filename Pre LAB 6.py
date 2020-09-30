'''
Pre Lab 6
'''
my_dict = {}
values = []
my_dict["Key_1"] = values
print(my_dict["Key_1"])
print()

my_dict["Key_1"].append("Hello")
my_dict["Key_1"].append("World")

print(my_dict["Key_1"])
print()

my_dict.clear()   #clears everything


my_dict["Apple"]    = 10
my_dict["Square"]   = 50
my_dict["Cube"]     = 100
my_dict["Circle"]   = 30


for key in my_dict:
    print("my_dict[",key,"]\t= ", my_dict[key], sep = "") #sep to keep alignment
print()


#check if key is inict
key_to_check = "Apple"
if key_to_check in my_dict:
    print(key_to_check, "is a key")
else:
    print(key_to_check,"is not a key")
    
print()

#remove things from dict/ will remove Cube
del my_dict["Cube"]


for key in my_dict:
    print("my_dict[",key,"]\t= ", my_dict[key], sep = "")
print()

#classes with dict
class Sample:
    sample_field = None

my_dict["Cube"] = Sample()
my_dict["Cube"].sample_field = "Sample Entry"

print(my_dict["Cube"].sample_field)
print()

#Break
for x in range(0,100):
    if x  == 5:
        break
    print(x, end = ", ")
print()
print("Resume")

print()
#MENU INTERFACE
def main():
    d = {}
    while True:
        present_menu()
        cmd = get_command()
        if cmd == "Q":
            break
        evaluate_command(d, cmd)

def present_menu():
    print("I - Insert")
    print("L - Look up")
    print("P - Print")
    print("Q - Quit")

def get_command() -> str:
    return input("Enter command: ").strip().upper()

def print_dict(d: dict):
        for p in d.items():
            print(d.items)
            print("Course:", p[0], "Teacher:", p[1])

def evaluate_command(d: dict, cmd: str):
    if cmd == "I":
        w = input("Enter course name: ")
        d[w] = input("Enter teacher name: ")
    elif cmd == "L":
        w = input("Enter course name: ")
        print(d[w])
    elif cmd == "P":
        print_dict(d)
    else:
        print("Invalid command")

main()

