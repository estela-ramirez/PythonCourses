
file_1 = open("Sample.txt.py")
#This command will create the file if does not
#exist, or wipe (DELETE) all data in the file when it is opened

file_2 = open("output.txt", 'w')

file_3 = open("add_to_me.txt", 'a')
# this will open it up so you can
#append at the end of the file


file_1.close() # closing files
file_2.close()
file_3.close()


#How to write a file
file_2 = open("output.txt", 'w')
file_2.write("Hello this is my first output\n")
# pass the text we want to write
file_2.write("This is now writing on line 2.")
file_2.write("Still on Line 2.\n")
file_2.close()

Hello this is my first output
This is now writing on line 2. Stilgl on Line 2


#How to read a file
file_1 = open("output.txt")
#This will print every line in the file out to the terminal.

for line in file_1:
    print(line)
   
#This moves the cursor back to the beginning of the file
file_1.seek(0)

#This function lets us read a file line by line
#assuming it is delimited by newlines

first_line = file_1.readline()
print(first_line)

#These two instructions read the first 5 letters
#and then prints them
first_five = file_1.read(5)
print(first_five)

# similarly, readlines()
#does the same thing as list(file_1)
print(file_1.readlines())




