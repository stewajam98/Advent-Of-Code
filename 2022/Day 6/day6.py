import numpy as np

input = []
with open(".\input.txt", "r") as f:
    for line in f:
        input = list(line.replace("\n", ""))
input = np.array(input)

# part 1
for i in range(len(input) - 3):
    string = input[i:i+4]
    if len(np.unique(string)) == 4:
        print(i+4)
        break

# part 2
for i in range(len(input) - 13):
    string = input[i:i+14]
    if len(np.unique(string)) == 14:
        print(i+14)
        break