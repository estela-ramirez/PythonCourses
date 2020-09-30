

def options()->str:
    a = 400
    while True:
        answer = input("Would you like to Fly: Up, Down, Fast Up, or Fast Down: ")
        if answer == 'Up':
            a = a+50
        elif answer == 'Down':
            a = a-50
        elif answer == 'Up Fast':
            a = a+150
        elif answer == 'Fast Down':
            a = a-150
        if a == 0:
            print("You have landed safely")
            break 
        elif a < 0:
            print("You have crashed")
            break

options()
            




##def get_command():
##    ask = input("Would you like to Fly: Up, Down, Fast Up, or Fast Down: ")
##    ask = ask.lower().strip()
##    return ask
##
##def compute():
##    start = 400
##    while True:
##        ask = get_command()
##        if ask == 'up':
##            start+=50
##        elif ask == 'down':
##            start -= 50
##        elif ask == 'fast up':
##            start +=150
##        elif ask == 'fast down':
##            start -=150
##
##        if start == 0:
##            print("Ypu have landed safely")
##            break
##        elif start < 0:
##            print("Oh no !! You have crashed!")
##            break
##
##compute()       
        
        
    















        
