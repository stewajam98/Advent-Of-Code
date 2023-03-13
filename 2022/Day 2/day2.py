#####################################################
###         PART 1
#####################################################
# A = rock, B = Paper, C = Scissors
# x = rock, y = paper, c = scissors

# points
#   1 = rock
#   2 = paper
#   3 = scissors

#   0 = loss
#   3 = tie
#   6 = win

#############################
##      PART 2
#############################
# X = LOSE
# Y = TIE
# Z = WIN

matches = []
matches2 = []
round_possibilities = {
    "X": {
        "A" : 4,
        "B" : 1,
        "C" : 7
    },
    "Y": {
        "A" : 8,
        "B" : 5,
        "C" : 2
    },
    "Z": {
        "A" : 3,
        "B" : 9,
        "C" : 6
    }
}

round_possibilities2 = {
    "X": {
        "A" : 3,
        "B" : 1,
        "C" : 2
    },
    "Y": {
        "A" : 4,
        "B" : 5,
        "C" : 6
    },
    "Z": {
        "A" : 8,
        "B" : 9,
        "C" : 7
    }
}

### reading in data 
with open(".\day2.txt", "r") as f:
    for line in f:
        x = line.split()
        matches2.append(x)
        matches.append(x)

# part 1
sum = 0
for match in matches:
    sum += round_possibilities[match[1]][match[0]]
print(sum)

# part 2
sum = 0
for match in matches2:
    sum += round_possibilities2[match[1]][match[0]]
print(sum)