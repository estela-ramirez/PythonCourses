##import random
##
##for x in range(1,10):#9 times
##    for i in range(1,10):
##        print(random.randint(1,10), end=" ")#'s 1-10
##
##
##print("\n")
##
##
##for x in range(1,82):#81 times
##    print(random.randint(1,5), end = " ") #'s 1-5
##
##print("\n")
##
##for j in range(10):
##	for i in range(10):#does it 100 times
##		print(random.randrange(0,10), end=" ")
##
##
##random.seed()
##L = ["apple","beta","cube","doris","eddy","fred"]
##
##for j in range(10):#does it 10 times
##	random.shuffle(L)
##	print(L)
##
##
##def countDown(n: int):
##	if n <= 0:
##		print("Blast Off!")
##	else:
##		print(n)
##		countDown(n-1)





##
##def exp(x: int, n: int) -> int:
##    if n == 0:
##        return 1
##    elif n == 1:
##        return x
##    else:
##        return (x * exp(x,n-1))
##   
##print(exp(2, 5))
##
##class Pet():
##    name = None
##    kind  = None
##
##def make_pet(name:str, kind:str) -> Pet:
##    p = Pet()
##    p.name = name
##    p.kind = kind
##    return p
##
##def find_pet_in_list(name:str, pets:list) ->Pet:
##    for pet in pets:
##        if p.name == name: 
##            return pet
##    pet = make_pet(name)
##    pets.append(pet)
##    return pet
##
##def load_pets_to_list(file_name;str)-> list:
##    pets = []
##    open_file = open(file_name, "r")
##    for line in file.readlines():
##        line = line.split()
##        name = line[0]
##        kind = line[1]
##        pet = make_pet(name, kind)
##        pets.append(pet)
##    open_file.close()
##    return pets
##
##def  get_pets_of_type_from_list(pet_type:str, pets:[Pet]) -> [Pet]:
##    list_of_pet_type = []
##    for pet in pets:
##        if pet.kind == pet_type:
##               list_of_pet_type.append(pet)
##    return list_of_pet_type
##
##
##
##def get_pets_of_type_from_dict(pet_type:str, pets:dict) -> [Pet]:
##    L = []
##    for key in pets:
##        if pets[key].kind == pet_type:
##            L.append(pets[key])
##    return L
##
##
##    
##    
##L= []
##number = "45"
##for x in str(number):
##    L.append(int(x))
##print(L)
##    
##
##number = "45"
##print([int(i) for i in str(number)])
##            
##

















		
