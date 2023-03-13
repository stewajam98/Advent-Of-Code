import numpy as np

### PART 1
positions = []
# reading in data
with open(".\day7.txt", "r") as f:
    for line in f:
        #splitting lines into a list
        input = line.split(",")
        for i in input:
            #appending each item in line list to the end of the total positions list
            positions.append(int(i))

#turning positions into a numpy array
positions = np.array(positions)

""" #taking median
median = np.median(positions)

# adding the value of the move to distance
distance = 0
for i in positions:
    distance += abs(i - median)

print(distance) """

### PART 2
# taking the mean value
max = np.max(positions)
ans = 1 << 60

for pos in range(max):
    req = 0
    for i in positions:
        dist = abs(i - pos)
        cost = dist * (dist + 1) // 2
        req += cost
    ans = min(ans, req)

print(ans)

