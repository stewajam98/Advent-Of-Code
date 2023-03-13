#########################################
###             GLOBALS
#########################################
# packages
import numpy as np
# variables
actions = []
cycle = 0
x = 1
sum = 0
pixels = ""

#########################################
###            FUNCTIONS
#########################################
def check_cycle():
    global sum
    global pixels

    pixel_num = (cycle - 1)%40
    current_pixels = [x-1, x, x+1]
    symbol = "#" if pixel_num in current_pixels else "."
    pixels = pixels + symbol

    if (cycle - 20) % 40 == 0:
        sum += (x * cycle)
        print("cycle: {}, x: {}, add: {}, sum: {}".format(cycle, x, cycle * x, sum))

#########################################
###       READING IN THE DATA
#########################################
with open(".\\input.txt", "r") as f:
    for line in f:
        actions.append(line.replace("\n","").split())

for act in actions:
    cycle += 1
    check_cycle()

    if act[0] == "noop":
        continue
    else:
        cycle += 1
        check_cycle()
        x += int(act[1])


print(sum)

print(pixels[0:40])
print(pixels[40:80])
print(pixels[80:120])
print(pixels[120:160])
print(pixels[160:200])
print(pixels[200:240])

