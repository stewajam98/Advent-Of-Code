### for array[i, j] ; i = row, j = col
########################################
####            GLOBALS
########################################
# packages
import numpy as np
# variables
GRID = []
start = {}
end = {}

########################################
####        READING IN DATA
########################################
i = 0
with open(".\input_test.txt", "r") as f:
    for line in f:
        if "S" in line:
            start["j"] = line.index("S")
            start["i"] = i

        if "E" in line:
            end["j"] = line.index("E")
            end["i"] = i

        row = [ord(x) for x in line.replace("S", "a").replace("E", "z") if x != "\n"]
        GRID.append(np.array(row))
        i += 1

GRID = np.array(GRID)

########################################
####            FUNCTIONS
########################################
def moves(i, j):
    
