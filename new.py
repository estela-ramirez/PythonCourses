import string

class Pet():
    name = None
    Type = None
    age = 0

def make_Pet(name:str, Type:str, age:int)->Pet:
    p = Pet()
    p.name = name
    p.Type = Type
    p.age = age
    return p

def add_pet(name:str, Type:str, age:int, pets:dict):
    p = make_Pet(name, Type, age)
    if name in pets:
        pets[name].append(p)
    else:
        pets[name] = [p]

def load_pets(file_name: str) -> dict:
    pets = {}
    file = open(file_name, "r")
    for line in file:
        name, pet_type, age = line.split()
        aadd_pet(name, pet_type, int(age), pets)
    file.close()
    return pets


def write_pet_list(ofile:'file', pets:list):
    for pet in pets:
        ofile.write(pet.name + "\t" + pet.Type + "\t" + str(pet.age) + "\n")
        
        

        
def save_sorted_pets(file_name: str, pets: dict):
    ofile = open(file_name,"w")
    for key in sorted(pets.keys()):
        write_pet_list(ofile,pets[key])
    ofile.close()

def main():
    pets = load_pets("pets.txt")
    save_sorted_pets("file_2.txt", pets)

main()
    
    
    
    


