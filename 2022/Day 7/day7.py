###########################################
####            CLASSES
###########################################
class directory:
    # initial set up of the class
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.size = 0

    # returning the object name
    def get_name(self):
        return self.name

    # getting and returning the size of the object
    def get_size(self):
        if self.size == 0:
            for i in self.inventory:
                self.size += i.get_size()
            print("{}, {}".format(self.name, self.size))
        
        return self.size

    # adding an object to the inventory
    def add_inventory(self, obj):
        self.inventory.append(obj)

class file:
    # initial set up of the class
    def __init__(self, name, size):
        self.name = name
        self.size = size

    # returns the name of the file
    def get_name(self):
        return self.name

    # returns the size of the file
    def get_size(self):
        return self.size



###########################################
####            GETTING DATA
###########################################
# reading in the data
lines = []
with open(".\input.txt", "r") as f:
    for line in f:
        lines.append(line.replace("\n", ""))

# creating full directories
main = directory("main")
directories = [main]
path = ["main"]
current_directory = main
for i in range(len(lines)):
    line = lines[i].split()
    
    # if line starts with $ then it's a command 
    if line[0] == "$":
        if line[1] == "cd":
            # move back one directory
            if line[2] == "..":
                path.pop()
                for dir in directories:
                    if dir.get_name() == path[-1]:
                        current_directory = dir
            # move to main directory
            elif line[2] == "/":
                path = ["main"]
                current_directory = main
            # move to next directory
            else:
                path.append(line[2])
                for dir in directories:
                    if dir.get_name() == path[-1]:
                        current_directory = dir

    # if line starts with dir then it's a new directory
    elif line[0] == "dir":
        new_directory = directory(line[1])
        current_directory.add_inventory(new_directory)
        directories.append(new_directory)
    
    # else it's a new file
    else:
        new_file = file(line[1], int(line[0]))
        current_directory.add_inventory(new_file)

###########################################
####             PART 1
###########################################
main.get_size()

sum = 0
for dir in directories:
    size = dir.get_size()
    if size < 100000:
        sum += size
print("Part1: {}".format(sum))

###########################################
####             PART 2
###########################################
total_disk_space = 70000000
update_space = 30000000
free_space = total_disk_space - main.get_size()
space_needed = update_space - free_space

smallest_directory = main
smallest_directory_size = main.get_size()
for dir in directories:
    size = dir.get_size()
    if size >= space_needed:
        if size < smallest_directory_size:
            smallest_directory_size = size
            smallest_directory = dir

print("Part2: {}, {}".format(smallest_directory.get_name(), smallest_directory_size))
