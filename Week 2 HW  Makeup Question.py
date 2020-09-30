'''
ICS 31 Week 2 Makeup Homework
Author: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
'''

def main():
    Max_Temp = 102.5
    fix_Temp(Max_Temp)

def fix_Temp(Max_Temp)->float:
    Max_Temp = 102.5
    while True:
        ask = float(input("Enter a temperature: "))
        if ask > Max_Temp:
            print("The temperature is too hot ")
            print("Temperature is Cool now, Check back in 30 minutes ")
        elif ask < Max_Temp:
            print("Temperature is Cool Now, Check back in 30 minutes ")
            break


main()

##def fix_Temp(f:float):
##    ask = float(input("Enter temperature: "))
##    while True:
##        if ask > f:
##            print("The temperature is too hot\nTemperature is Cool now, Check back in 30 minutes")
##            ask = float(input("Enter temperature: "))
##        else:
##            print("Temperature is Cool Now\nCheck back in 30 min")
##            break
##
##def main():
##    Max_Temp = 102.5
##    fix_Temp(Max_Temp)
##
##main()



