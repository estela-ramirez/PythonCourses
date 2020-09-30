my_str = "Hello World"
print(len(my_str))

my_list =[1,2,3,4,5,6]
print(len(my_list))
      
for x in range(0, len(my_str)):
    print(my_str[x])

for y in range(0, len(my_list)):
    print(my_list[y])

print("Hello", "World")
print("Hello" + " "+ "World" + "\n")

for x in range(0, len(my_str)):
    print(my_str[x],  end = "")



for letter in my_str:
    print(letter)

print(" ")

for elm in my_list:
    print(elm)

my_str = "   Space is Big   "
print(my_str)
print(my_str.strip())
print(my_str.lower())
print(my_str.strip().lower()) # takes out white space and lowercases it all
print(my_str)

my_str = my_str.strip().lower() # does not work like this
print(my_str)

for elem in my_list:
    if elem == 4:
        print("I found 4! ")

max = -1000000
for elem in my_list:
    if elem > max:
        max = elem
        print("Max value in", my_list, "is", max)


'''

def print_intro(msg: str):
    print(msg)


def return_val(arg: str) -> str:
    return "hello " + arg + "world "


def return_val(arg: str) -> str:
    ret =  "hello " + arg + "world "
    return ret

def main():
     print_intro(return_val("cruel"))

def main():
    in = return_val("cruel")
    print_intro(in)

'''


















































