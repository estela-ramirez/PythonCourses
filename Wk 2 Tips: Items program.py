def ask_n_items()->int:
    return int(input("How many items did you buy? "))


def times()->float:
    items = ask_n_items()
    total = 0
    for x in range(items):
        ask = float(input("Item price: "))
        total += ask
    return total

def fifteen(total:float)->float:
    return total *.15

def twenty(total:float)->float:
    return total *.2

def twentyfive(total:float)->float:
    return total *.25

def main():
    total = times()
    f = fifteen(total)
    t = twenty(total)
    tf = twentyfive(total)
    newf = total + f
    newt = total + t
    newtf = total + tf
    print("Total spent is $", total)
    print("15% Tip is", "$",f, "totals to be",newf, "\n18% Tip is", "$",t,"totals to be",newt)
    print("25% Tip is", "$",tf, "totals to be", newtf)

main()
    
