map = []

### defining functions
def check_lower(x, y,value):
    try:
        if map[x][y] < value:
            return False
        else:
            return True
    except:
        return True

# reading in the data
with open(".\day9.txt", "r") as f:
    for line in f:
        values = list(line.rstrip())
        for i in range(len(values)):
            values[i] = int(values[i])
        map.append(values)
    
# getting the dimensions of the map
x = len(map[0])
y = len(map)

### PART 1
# looping through and finding low values. This requires checking to make sure you aren't going out of bounds
lows = []
for i in range(y):
    for j in range(x):
        value = map[i][j]
        if value != 9:
            lower = []
            lower.append(check_lower(i, j+1,value))
            lower.append(check_lower(i, j-1,value))
            lower.append(check_lower(i+1, j,value))
            lower.append(check_lower(i-1, j,value))

            if False not in lower:
                lows.append([value, i, j])

#adding risk values
risk = 0
for i in lows:
    risk += i[0] + 1
print(risk)

### PART 2
def search_left(low):
    count = 0
    i = low[1]
    j = low[2]

    stop = False
    steps = 1
    while stop == False:
        

        