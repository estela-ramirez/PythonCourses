def open_file(file_name: str, mode: str) -> 'file':
    try :
        file = open(file_name, mode)
        return file
    print("FileNotFoundError( Error Number =", e.errno, "):", e.strerror)

f = open_file("none", 'r')
print(“Hello”)

def open_file(file_name_list: list, desired_file_index: int, modes: str) -> ‘file’:
    try :
        file = open(file_name_list[desired_file_index], modes)
        return file
print("IndexError:", str(e))
print("OS or I/O error( Error Number =", e.errno, "):", e.strerror)
print("FileNotFoundError( Error Number =", e.errno, "):", e.strerror)
print("Exception:", str(e))

 except:
        print("Something really unexpected happened, when opening the file")
    return None


def what():
    try:
        #open file
    except FileNotFoundError: #
        print("Sorry Error")
    except Exception:
        print("My bad")

or

def what():
    try:
        #open file
    except FileNotFoundError as e: #
        print(e)#will print python error mode
    except Exception as e:
        print(e)
    else:
        #if there is no error up top thwn it will execute program here




        
