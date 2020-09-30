'''
Question 1: Ask the user for the total number of papers submitted in a class. Ask the user for the number of students in the class. Output the average number of papers submitted per student. Assume class has more than zero students, and all numbers are integers.
Sample Output:
>>>
How many papers were submitted:  100
How many students are in the class:  20
The average number of papers submitted per student is 5.0
'''
'''
a=int(input("How many papers were submitted: "))
b=int(input("How many students are in the class: "))
print("The average number of papers submitted per student is", a+b/2)
'''

'''
Question 2: Prompt the user for three numbers and then output their
sum, difference, product, quotient, remainder, average.
First number always before second number and second before third for each operation.
Assume the second and third numbers will not be zero.
Sample Output:
>>>
Enter the first number: 10
Enter the second number: 25
Enter the third number: 15.6
The sum of 10.0 25.0 15.6 is 50.6
The difference of 10.0 25.0 15.6 is -30.6
The product of 10.0 25.0 15.6 is 3900.0
The quotient of 10.0 25.0 15.6 is 0.025641025641025644
The remainder of 10.0 25.0 15.6 is 10.0
The average of 10.0 25.0 15.6 is 16.866666666666667
'''
'''
a=float(input('Enter the first number: '))
b=float(input('Enter the second number: '))
c=float(input('Enter the third number: '))
print("The sum of", a,b,c, "is", a+b+c)
print('The difference of', a,b,c, 'is', a-b-c)
print('The product of', a,b,c, 'is', a*b*c)
print('The quotient of', a,b,c, 'is', a/b/c)
print('The remainder of', a,b,c, 'is', a%b%c)
print('The average of', a,b,c, 'is', (a+b+c)/3)
'''
'''
Question 3: Ask the user for 3 words/phrases.
Output all possible combinations of the 3 strings.
(first + second + third, third + second + first, etc.)
Sample Output:

>>> 
Enter the first word: hello
Enter the second word: pizza
Enter the third word: world
hello pizza world
hello world pizza
pizza hello world
pizza world hello
world hello pizza
world pizza hello
'''

'''
a=input('Enter the first word: ')
b=input('Enter the seconnd word: ')
c=input('Enter the third word: ')
print(a, b, c)
print(a, c, b)
print(b, a, c)
print(b, c, a)
print(c, a, b)
print(c, b, a)
'''

'''
Question 4: Ask the user for a length and then create functions to provide you
with the appropriate areas for the following shapes:

Write a function that provides the area of a circle with a diameter of length. 

Write a function that provides the area of a triangle
whose length and height are equal to the user provided length.

Write a function that provides the area of a square with sides of the provided length. 


Sample Output:
>>> 
Enter the side/diameter length:  5.2
Area of the Circle is: 21.237166338267002
Area of the Triangle is: 13.520000000000001
Area of the Square is: 27.040000000000003
'''
'''
import math

a=float(input('Enter the side/diamter length: '))

print("Area of the Circle is: ", math.pi*(a/2)**2)
print('Area of the Triangle is: ', (a*a)/2)
print('Area of a Square is: ', (a**2))

'''
'''
Question 2: Draw a Triangle using the ‘*’ character. The Triangle should have its length (vertical side) on the left side of the screen and a base of length n, where n is input by the user. Assume n is always an integer.
 
Sample Output:
>>>
Left Facing Triangle's base size:  5
*
**
***
****
*****
'''
'''
i=int(input("Left Facing Triangle's base size: "))
n=1
while i>=n:
    print('*'*n)
    n+=1
'''
'''
What is your favorite color? blue
What is your favorite OS? Linux
What is your favorite font? Times New Roman

Your favorite color is 'blue'
Your favorite OS is 'Linux'
Your favorite font is 'Times New Roman'
'''
'''
def favorite_color()->str:
    return input("What is your favorite color? ")

def favorite_OS()->str:
    return input("What is your favorite OS? ")

def favorite_font()->str:
    return input("What is your favorite color? ")

def print_favorite_color(color:str)->str:
    print("Your favorite color is '", color, "'", sep = "")

def print_favorite_OS(OS:str)->str:
    print("Your favorite OS is '", OS, "'", sep = "")

def print_favorite_font(font:str)->str:
    print("Your favorite string is '", font, "'", sep = "")
    
color=favorite_color()
OS=favorite_OS()
font=favorite_font()

print(' ')

print_favorite_color(color)
print_favorite_OS(OS)
print_favorite_font(font)
'''
'''
def i_color()->str:
    return input("What is ")

def p_color(color:str)->str:
    print("Your color '", color, "'", sep = "")

color=i_color()

print(' ')

p_color(color)

'''
    



def input_f()->str:
    return input("What is? ")

def print_f(n:str)->str:
    print("Your name '", n, "'", sep = "")

n=input_f()

print(' ')

print_f(n)
























