#####################################
##              GLOBALS
#####################################
# packages
import numpy as np

# variables
MOVES = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
    "UR": np.array([1,1]),
    "UL": np.array([-1,1]),
    "DR": np.array([1,-1]),
    "DL": np.array([-1,-1]),
}
#####################################
##              CLASSES
#####################################
class head:
    def __init__(self):
        self.position = np.array([0, 0])

    def get_position(self):
        return self.position
    
    def move(self, direction):
        self.position += MOVES[direction]

        return self.position

class tail:
    def __init__(self):
        self.position = np.array([0,0])
        self.position_list = [[0,0]]

    def move(self, head_position):
        if are_touching(head_position, self.position):
            return
        else:
            diff = head_position - self.position
            move = np.copysign(((abs(diff/2))+0.1).round(),diff).astype(int)
            self.position += move.astype(int)
            if list(self.position) not in self.position_list:
                self.position_list.append(list(self.position))
            return

    def get_unique_positions(self):
        length = len(self.position_list)
        return length

    def get_position(self):
        return self.position


#####################################
##             FUNCTIONS
#####################################
def are_touching(head, tail):
    # getting all of the neighbors of the tail
    neighbors = np.matrix([
        [-1, 1], [0, 1], [1, 1],
        [-1, 0], [0, 0], [1, 0],
        [-1, -1], [0, -1], [1,-1]
    ]) + tail

    touching = True if any(np.equal(neighbors, head).all(1)) else False

    return touching
    
#####################################
##          READING IN DATA
#####################################
# reading in the data
movements = []
with open(".\input.txt", "r") as f:
    for line in f:
        movements.append(line.replace("\n", "").split())

# creating the kntos
head = head()
knots = [head]
for i in range(9):
    new_tail = tail()
    knots.append(new_tail)

# cycling through movements
for line in movements:
    for i in range(int(line[1])):
        for i in range(10):
            if i == 0:
                knots[0].move(line[0])
            else:
                knots[i].move(knots[i-1].get_position())

print("Part 1: {}".format(knots[1].get_unique_positions()))
print("Part 2: {}".format(knots[-1].get_unique_positions()))