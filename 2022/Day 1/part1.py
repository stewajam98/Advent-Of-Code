elves = []
calories = []

### reading in data
with open(".\part1.txt", "r") as f:
    for line in f:
        x = line.replace("\n", "")
        if(x != ""):
            calories.append(int(x))
        else:
            elves.append(calories)
            calories = []

#### part 1
max = 0
for elf in elves:
    sum = 0
    for snack in elf:
        sum += snack
    if sum > max:
        max = sum

print(max)

#### part 2
elves_total = []
for elf in elves:
    sum = 0
    for snack in elf:
        sum += snack
    elves_total.append(sum)

elves_total.sort(reverse = True)
top3 = elves_total[0] + elves_total[1] + elves_total[2]
print(top3)