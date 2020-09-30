def i_input()->str:
    return input("What is your: ")

def p_print(color:str)->str:
    print("Your color is '", color, "'", sep = "")

color=i_input()

p_print(color)
