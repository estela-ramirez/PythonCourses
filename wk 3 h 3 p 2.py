'''
ICS 31 omework 3 Problem 2
Author: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
'''
def main():
    num_of_temps = int(input("How many temperatures would you like to convert: "))
    temperature_list, types_list= record_temps(num_of_temps)
    #convert is called in output
    output(temperature_list, types_list)

def record_temps(num_of_temps)->list:
    temperature_list = []
    types_list = []
    for x in range(1, num_of_temps+1):
        user_temp = (input("Enter a Temperature: "))
        temperature_list.append(user_temp)
        user_type = (get_temp_type())
        types_list.append(user_type) #calls the function, no need to in main 
    return temperature_list, types_list

def get_temp_type():# will be added into types list
    while True: # needs while/ till user puts it in right
        types_list = input("Is the temperature in Farenheit(F) or Celcius(C): ")
        if types_list == "C":
            return types_list
        elif types_list == "F":
            return types_list
        else:
            print("ERROR:", types_list, "is not a valid scale, enter F or C")

def convert(temperature_list, initial_type):
    C = "°C"
    F = "°F"
    temperature_list = float(temperature_list) # changes str --> float, for math
    if initial_type == "C":
        return str(temperature_list*1.8+32) +C 
    else:
        return str((temperature_list-32)/1.8) +F 

def output(temperature_list, types_list):
    for x in range(len(temperature_list)):
        print(temperature_list[x], "°", types_list[x], "is", convert(temperature_list[x], types_list[x]))
    
main()
    
