elf_pairs = []

with open(".\input.txt", "r") as f:
    for line in f:
        pairs = line.replace("\n", "").replace("-",",").split(",")
        for i in range(len(pairs)):
            pairs[i] = int(pairs[i])
        elf_pairs.append(pairs)

print(elf_pairs)

# part 1
count = 0
for pair in elf_pairs:
    if (((pair[0] >= pair[2]) and (pair[1] <= pair[3])) or 
        ((pair[0] <= pair[2]) and (pair[1] >= pair[3]))):
        count += 1
print(count)

# part 2
count = 0
for pair in elf_pairs:
    if(((pair[0] <= pair[2]) and (pair[1] >= pair[2])) or
       ((pair[0] <= pair[3]) and (pair[1] >= pair[3])) or
       ((pair[0] >= pair[2]) and (pair[1] <= pair[3])) or 
       ((pair[0] <= pair[2]) and (pair[1] >= pair[3]))):
       count += 1
print(count)