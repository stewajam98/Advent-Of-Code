import copy
import numpy as np

picks = []
text_lines = []
boards = []
boards2 = []

### Creating board class
class board(object):
    def __init__(self, spaces):
        self.spaces = np.matrix(np.reshape(spaces, (5,5)))
        self.status = "active"

    def check_space(self, num):
        for i in range(5):
            for j in range(5):
                if self.spaces[i, j] == num:
                    self.spaces[i, j] = "X"

    def check_win(self):
        win = False
        for i in range(5):
            col = True
            row = True

            if np.any(self.spaces[:, i] != "X"):
                col = False
            if np.any(self.spaces[i,:] != "X"):
                row = False

            if col or row:
                win = True
                return win
        return win

    def get_points(self, num):
        sum = 0
        for i in range(5):
            for j in range(5):
                if self.spaces[i, j] != "X":
                    sum += int(self.spaces[i, j])
        return (sum*int(num))

### Part 1
with open(".\day4.txt", "r") as f:
    for line in f:
        text_lines.append(line.rstrip())

board_lines = copy.deepcopy(text_lines[2:])

# saving picks
picks = text_lines[0].split(",")

# creating boards
list = []
for i in range(len(board_lines)):
    if board_lines[i] == "":
        boards.append(board(list))
        boards2.append(board(list))
        list = []
    else:
        line = board_lines[i].split(" ")
        for num in line:
            if num != "":
                list.append(num)

def main():
    ### Part 1
    game_over = False
    count = 0
    while game_over == False:

        for board in boards:
            board.check_space(picks[count])
            if board.check_win() == True:
                print(board.get_points(picks[count]))
                game_over = True
                break

        count += 1


    ### Part 2
    count = 0
    active = len(boards2)
    while active > 0:
        for board in boards2:
            if board.status != "active":
                continue

            board.check_space(picks[count])
            if board.check_win() == True:
                board.status = "Not active"
                active -= 1
                if active == 0:
                    print(board.get_points(picks[count]))

        count += 1

main()
