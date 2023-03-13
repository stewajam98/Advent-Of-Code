depths = []
windows = []

### Part 1
# function for counting increases
def count_increases(list):
    count = 0
    for i in range(len(list)):
        if i != 0:
            if list[i] > list[i-1]:
                count+= 1
    return count

# read in sonar depths
with open(".\day1.txt", "r") as f:
    for line in f:
        depths.append(int(line.rstrip()))

print(count_increases(depths))

### Part 2
# Creating windows
for i in range(len(depths)):
    if i + 2 < len(depths):
        window = depths[i] + depths[i+1] + depths[i+2]
        windows.append(window)

print(count_increases(windows))
