
def hello():
    
    while True:
        ask = input("Are you a boy or a girl?").upper()
        if ask == "BOY":
            print("You are a boy")
        elif ask == "GIRL":
            print("You are a girl")
        else:
            print("You are an alien???")
            break

def main():
    hello()
main()
        
