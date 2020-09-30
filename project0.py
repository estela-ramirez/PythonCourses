'''
ICS 32 Project 0
Driver: UCI_ID: 18108714 Name:EStela Ramirez Ramirez
'''
'0<n>999'

def ask()->int:
    return int(input())
         
def compute():
    a = "+-+\n| |\n+-+"
    b  = "+-+"
    c = "| |"
    d = "+-+-+"
    n = ask()
    last_space_equation = 2*n-2
    if n == 1:
        print(a)           
    else:
        print(b, "\n", c, sep = "")
        for x in range(n-1):
            first = 2*x
            eq = 2*x + 2
            print(first*" "+d)
            print(eq*" "+c)           
     
        print(last_space_equation*" "+b)       
compute()


