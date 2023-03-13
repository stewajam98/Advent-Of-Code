import copy

input = []
fish = []
days_pt1 = 80
days_pt2 = 256

def get_fish_count():
    fish_count = 0
    for i in range(9):
        fish_count += fish_dict[str(i)]
    print(fish_count)

#### PART 1
# reading in data
with open(".\day6.txt", "r") as f:
    for line in f:
        input.append(line.rstrip())

#splitting up the fish and creating objects
input_split = input[0].split(",")

fish_dict = {"0": 0,
             "1": 0,
             "2": 0,
             "3": 0,
             "4": 0,
             "5": 0,
             "6": 0,
             "7": 0,
             "8": 0}

### creating initial dictionary values
for i in range(len(input_split)):
    for j in range(9):
        if input_split[i] == str(j):
            fish_dict[str(j)] += 1

### cycling through the days
for i in range(days_pt2):
    daily_dict = copy.deepcopy(fish_dict)
    for j in range(9):
        if j == 0:
            fish_dict["8"] += daily_dict["0"]
            fish_dict["6"] += daily_dict["0"]
            fish_dict["0"] = 0
        else:
            fish_dict[str(j-1)] += daily_dict[str(j)]
            fish_dict[str(j)] -= daily_dict[str(j)]

    if i == days_pt1 - 1:
        get_fish_count()

get_fish_count()
