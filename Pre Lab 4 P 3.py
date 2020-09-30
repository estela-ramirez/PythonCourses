#This function checks if the data in num is an integer.
def isInt(num: str) -> bool:
    try: 
        int(num)
        return True
    except ValueError:
        return False


#IN OPERATOR
L = [1,2,3]
val = 1
if val in L:
    print( val , "is in the list")
else:
    print(val , "is not in the list")

S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sub_Str = "JK"
if sub_Str in S:
    print( sub_Str , "is in the list")
else:
    print(sub_Str , "is not in the list")
    
#Also note that the empty string is considered in every string
empty = ""
if empty in S:
    print("S has the empty_string")

#String INDEXING
S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
first_15    = S[0:15] #Contains the first 15 letters, or the letters in indexes 0 - 14

last_15     = S[len(S) - 15 : len(S)]       #Specify the end index + 1
last_15_alt = S[len(S) - 15 : ]             #Say start here and grab all

print(first_15)
print(len(first_15))
print()
print(last_15)
print(len(last_15))
print()
print(last_15_alt)
print(len(last_15_alt))

#INDEXING BACKWARDS
#  0  1  2  3  4
#  H  E  L  L  O
# -5 -4 -3 -2 -1
first_15 = S[ -len(S) : (-len(S) + 15)]
last_15 = S[-15: len(S)]     #Contains the last 15 letters, or the letters in indexes -15 to -1
last_15_alt = S[-15 : ]      #Say start here and grab all
print(first_15)
print(len(first_15))
print()
print(last_15)
print(len(last_15))
print()
print(last_15_alt)
print(len(last_15_alt))

#FIND
str1 = "My Example, Sample, Text, String";
str2 = "exam";
#This will return -1, as find is case sensitive
print(str1.find(str2))

#This will return 3, as that is the index of the substring
print(str1.lower().find(str2.lower()))

#This will return -1, as it will start searching after the substring
print(str1.lower().find(str2.lower(), 10))

#This will return 1, as find goes from the front of the string
print(str1.find(str2))


#R.FIND searches backwards and returns the highest rather than lowest index



#This will return 13 as rfind goes from the back of the string
print(str1.rfind(str2))

#This will return 1, as their is no later occurrence before index 10 
print(str1.rfind(str2, 0, 10))

#This will return 13, as their is no later occurrence after index 10 
print(str1.rfind(str2, 10))





