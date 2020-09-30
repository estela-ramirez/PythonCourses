'''
ICS 31 omework 3 Problem 2
Author: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
'''
def main():
    num_of_temps = int(input("How many temperatures would you like to convert: "))
    temperature, types = record_temps(num_of_temps)  
    output(temperature, types)
    
def record_temps(num_of_temps)->list:
    temperature = []
    types = []
    
    for x in range(num_of_temps):
        temperature.append(input("Enter a Temperature: "))
        types.append(get_temp_type())###
        
    return temperature, types

def get_temp_type():
    while True: 
        types = input("Is the temperature in Farenheit(F) or Celcius(C): ")####
        if types == "C" or types == "F":
            return types
        else:
            print("ERROR:", types, "is not a valid scale, enter F or C")
            
def convert(temperature, initial_type):
    temperature = int(temperature)
    if initial_type == "F":
        return str((temperature -32)/1.8)+ "°C"
    else:
        return str(temperature*1.8+32)+ "°F"
    
    
def output(temp_list, temp_types):
    for x in range(len(temp_list)):
        print(temp_list[x], "°", temp_types[x], "is", convert(temp_list[x], temp_types[x]))
    

main()

       temperature.append(input("Enter a Temperature: "))#change#################
        temperature.append(temp)
        types.append(get_temp_type()) #calls the function, no need to in main 





'''
def get_temp_type(): 
    for x in range(numb_of_temps):
        temperature = int(input("Enter a temperature: "))
        temp_list. append(temperature)
        print(temp_list)
        for x in temp_type:
            if temp_type == "F":
                return "F"
            elif temp_type == "C":
                return "C"
            else:
                print("ERROR:", temp_type, "is not a valid scale, enter F or C")
 
'''






