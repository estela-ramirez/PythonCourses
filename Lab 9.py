import string
#wk 9 lectures
#pet stuff
'''
ICS 31 Lab 9  Problem 1
Driver:  UCI_ID: 18108714  Name: Estela Ramirez Ramirez
'''
'''
for key in sorted(cards.keys()):
    print("Cards with value", key, "are", cards[key])
'''
class Pet():
    name = ""
    age = 0
    pet_type = ""

def make_pet(name:str, age:int, pet_type:str)->Pet:
    p = Pet()
    p.name = name
    p.age = age
    p.pet_type = pet_type
    return p

def add_pet(name: str, age: int, pet_type: str, pets: dict):
    new_pet = make_pet(name, age, pet_type)
    pets[name] = new_pet
    

def load_pets(file_name: str) -> dict:
    pets = {}
    file =  open(file_name, "r")
    for line in file.readlines():
        line = line.split()
        name = line[0]
        age = line[2]
        pet_type = line[1]
        pet = add_pet(name, age, pet_type, pets)#adds to dictionary
    file.close()
    return pets

    
def save_sorted_pets (file_name: str, pets: dict):
    #sorted_pets  = sorted(pets.items(), key = lambda t:t[0])
    sorted_pets = sorted(pets.keys())
    file = open(file_name, "w")
    for key in sorted_pets:
        file.write((str(pets[key].name) + "\t" + str(pets[key].pet_type) + "\t" + str(pets[key].age) +"\n"))
    file.close()
        
        
def main():
    pets_dict = load_pets("pets.txt")
    save_sorted_pets("sorted_pets.txt" , pets_dict)
    

if __name__ == "__main__":
    main()

    




















