import numpy as np
import pandas as pd

# functions
def is_visible(i, j):
    visible = True
    height = forest.loc[i,j]

    if (forest.loc[0:i-1,j].max() >= height and
        forest.loc[i+1:cols, j].max() >= height and
        forest.loc[i, 0:j-1].max() >= height and
        forest.loc[i, j+1:rows].max() >= height):
            visible = False
    
    return visible

def get_score(i, j):
    height = forest.loc[i,j]
    
    if i == 0 or j == 0:
        return 0

    else:
        dist1,dist2,dist3,dist4 = 0, 0, 0, 0
        for g in range(i):
            if i-g-1 < 0:
                break
            elif forest.loc[i-g-1, j] >= height:
                dist1 += 1
                break
            else:
                dist1 += 1

        for g in range(cols - i - 1):
            if i + g + 1 > cols:
                break
            elif forest.loc[i + g + 1, j] >= height:
                dist2 += 1
                break
            else:
                dist2 += 1

        for g in range(j):
            if j-g-1 < 0:
                break
            elif forest.loc[i,j-g-1] >= height:
                dist3 += 1
                break
            else:
                dist3 += 1
        
        for g in range(rows-j - 1):
            if j + g + 1 > rows:
                break
            elif forest.loc[i, j+g+1] >= height:
                dist4 += 1
                break
            else:
                dist4 += 1

        return dist1 * dist2 * dist3 * dist4
                


    return score

# reading in data
forest = []
with open(".\input.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        row = []
        for i in line:
            row.append(int(i))
        forest.append(row)

# global variables
rows = len(forest)
cols = len(forest[0])
forest = pd.DataFrame(forest)

# main
count = 0
max_score = 0
for i in range(cols):
    for j in range(rows):
        count += 1 if is_visible(i, j) else 0
        score = get_score(i,j)
        max_score = score if score > max_score else max_score
print(count)
print(max_score)

