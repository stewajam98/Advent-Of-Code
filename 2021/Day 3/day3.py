import copy

inputs = []
gamma_list, epsilon_list = [], []


### Functions
# Function for reading binary
def binaryList_to_number(list):
    number = 0
    #cycles through each part of the binary list and adds 2 ^ the inverse index
    for i in range(len(list)):
        if list[-(i + 1)] == 1:
            number += 2**(i)
    return number

# Function for popping item
def remove_objects(list, num, index):
    list_2 = copy.deepcopy(list)
    for object in list_2:
        if object[index] != str(num):
            list.remove(object)
    return list

# Rating selection
def rating_selection(list, common_type = "most"):
    for i in range(input_length):
        if len(list) == 1:
            return list

        zeros = 0
        ones = 0

        for input in list:
            if input[i] == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            choice = "0"
        elif ones > zeros:
            choice = "1"

        if common_type == "most":
            if choice == "0":
                list = remove_objects(list, 0, i)
            elif choice == "1":
                list = remove_objects(list, 1, i)
            else:
                list = remove_objects(list, 1, i)
        elif common_type == "least":
            if zeros > ones:
                list = remove_objects(list, 1, i)
            elif zeros == ones:
                list = remove_objects(list, 0, i)
            else:
                list = remove_objects(list, 0, i)
        else:
            return("ERROR: wrong common_type")


    return list

### Part 1
# read in data
with open(".\day3.txt", "r") as f:
    for line in f:
        inputs.append(line.rstrip())

# get length of binary number
input_length = len(inputs[0])

# cycle through each index
for i in range(input_length):
    zeros = 0
    ones = 0

    # goes through each input and checks if the bit at the index is 1 or zero
    # adds one to the category
    for input in inputs:
        if input[i-1] == "0":
            zeros += 1
        else:
            ones += 1

    # if more zeros in this index, append a 0 to gamma and 1 to epsilon
    # opposite if 1 was more common
    if zeros > ones:
        gamma_list.append(0)
        epsilon_list.append(1)
    else:
        gamma_list.append(1)
        epsilon_list.append(0)


gamma = binaryList_to_number(gamma_list)
epsilon = binaryList_to_number(epsilon_list)
print(gamma*epsilon)

### Part 2
oxygen_list = copy.deepcopy(inputs)
carbon_list = copy.deepcopy(inputs)


oxygen = rating_selection(oxygen_list, "most")
carbon = rating_selection(carbon_list, "least")

oxygen = [int(char) for char in oxygen[0]]
carbon = [int(char) for char in carbon[0]]


oxygen = binaryList_to_number(oxygen)
carbon = binaryList_to_number(carbon)
print(oxygen * carbon)
