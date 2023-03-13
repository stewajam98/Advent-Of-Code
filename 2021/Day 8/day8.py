import copy

lines = []
output = []
inputs = []
values = [2, 4, 3, 7]

# read in data
with open(".\day8.txt", "r") as f:
    for line in f:
        lines.append(line.rstrip())

#split line of numbers and get the "output" values
for line in lines:
    split = line.split(" | ")
    inputs.append(split[0])
    output.append(split[1])

### PART 1
#cycling through output and counting nums
num = 0
for i in output:
    digits = i.split()
    for j in digits:
        if(len(j) in values):
            num += 1

print(num)

### PART 2
# running through each line
sum = 0
for i in range(len(inputs)):
    # creating the dictionary
    dict = {}
    digits = inputs[i].split()
    # finding the first 4 digits that are 1, 7, 4, and 8
    for j in digits:
        n = len(j)
        if n == 2:
            dict[1] = [list(j), 2]
        elif n == 3:
            dict[7] = [list(j), 3]
        elif n == 4:
            dict[4] = [list(j), 4]
        elif n == 7:
            dict[8] = [list(j), 7]

    # fidning digits of length 6 (9, 6, and 0)
    for j in digits:
        n = len(j)
        let = list(j)
        if n == 6:
            if(all(elem in let for elem in dict[4][0])):
                dict[9] = [let, 6]
            elif(all(elem in let for elem in dict[1][0])):
                dict[0] = [let, 6]
            else:
                dict[6] = [let, 6]

    # finding digits of length 5 (5, 3, and 2)
    for j in digits:
        n = len(j)
        let = list(j)
        if n == 5:
            if(all(elem in let for elem in dict[1][0])):
                dict[3] = [let, 5]
            elif(all(elem in dict[9][0] for elem in let)):
                dict[5] = [let, 5]
            else:
                dict[2] = [let, 5]

    codes = output[i].split()
    values = []
    for j in codes:
        n = len(j)
        for key in dict:
            if n == dict[key][1]:
                if(all(elem in list(j) for elem in dict[key][0])):
                    values.append(key)
    value = (values[0] * 1000) + (values[1] * 100) + (values[2] * 10) + values[3]
    sum += value
print(sum)