
def favorite_color()->str:
    return str(input("What is your favorite color? "))
a=favorite_color()

def favorite_OS()->str:
    return str(input("What is your favorite OS?"))
b=favorite_OS()

def favorite_font()->str:
    return str(input("What is your favorite font?"))
c=favorite_font()

print(' ')

print("Your favorite color is '",a, "'", sep = "")

print("Your favorite OS is '", b, "'", sep = "")

print("Your favorite font is '", c, "'", sep = "")

