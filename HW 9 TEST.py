import string
print(string.punctuation)

def sem(test):
    if test in string.punctuation:
        print("yes")
        return True
    else:
        print("no")
        return False

def main():
    test = "&"
    sem(test)
main()
