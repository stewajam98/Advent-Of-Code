x, y, aim = 0, 0, 0
commands = []

### Part 1
# Reading in data
with open(".\day2.txt", "r") as f:
    for line in f:
        commands.append(line.rstrip())

# Making moves
for command in commands:
    command_list = command.split()

    if command_list[0] == "forward":
        x += int(command_list[1])
    elif command_list[0] == "down":
        y += int(command_list[1])
    elif command_list[0] == "up":
        y -= int(command_list[1])

print(x*y)
print("---------------")

### Part 2
x, y = 0, 0

for command in commands:
    command_list = command.split()

    if command_list[0] == "down":
        aim += int(command_list[1])
    elif command_list[0] == "up":
        aim -= int(command_list[1])
    elif command_list[0] == "forward":
        x += int(command_list[1])
        y += int(command_list[1]) * aim

print(x*y)
