import re
from copy import deepcopy as dc

boxes = []
steps = []
start = True
with open(".\input.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        if line == '':
            start = False
        elif start == True:
            boxes.append(line)
        else:
            steps.append(line)


# creating the stacks
num_stacks = int(boxes[-1][-2])
stacks = []
for i in range(num_stacks):
    stacks.append([])

for line in boxes:
    stack = 0
    if line[1] == "1":
        break
    for i in range(len(line)):
        if ((stack * 4) + 1) == i:
            if line[i] != " ":
                stacks[stack] = [line[i]] + stacks[stack]
            stack += 1

stacks2 = dc(stacks)


# getting the movements
movements = []
for line in steps:
    line = re.sub('[^0-9]', ' ', line)
    line = line.split()
    line = [int(x) for x in line]
    for i in range(3):
        line[i] = line[i] - 1 if i > 0 else line[i]
    movements.append(line)


################################
####          PART 1
################################
# moving the boxes around
for step in movements:
    for i in range(step[0]):
        stacks[step[2]].append(stacks[step[1]].pop())

# getting the top crates
top_crate = ""
for stack in stacks:
    top_crate += stack[-1]

print(top_crate)

################################
####          PART 2
################################
# moving the boxes around
for step in movements:
    moving_crates = []
    for i in range(step[0]):
        moving_crates = [stacks2[step[1]].pop()] + moving_crates
    stacks2[step[2]] += moving_crates

# getting the top crates
top_crate = ""
for stack in stacks2:
    top_crate += stack[-1]

print(top_crate)