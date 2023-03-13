# 96 for lowercase
# 64 for upercase (64 - 26) = 38

rucksacks = []
rucksacks2 = []
items = []


with open(".\day3.txt", "r") as f:
    i = 0
    group = []
    for line in f:
        line = line.replace("\n","")
        # data for part 2
        group.append(line)
        if i % 3 == 2 and i != 0:
            rucksacks2.append(group)
            group = []
        i += 1
            
        # data for part 1
        length = len(line)
        rucksacks.append([line[0:int(length/2)],line[int(length/2):]])


### Part 1
sum = 0
for sack in rucksacks:
    for item in sack[1]:
        if item in sack[0]:
            items.append(item)
            if item.isupper():
                sum += ord(item) - 38
            else:
                sum += ord(item) - 96
            break

print(sum)

### Part 2
sum = 0
print(len(rucksacks2))
for group in rucksacks2:
    for item in group[0]:
        if (item in group[1]) and (item in group[2]):
            if item.isupper():
                sum += ord(item) - 38
            else:
                sum += ord(item) - 96
            break

print(sum)
