import re

inputs = []
segments = []
overlap_points = []

### Creating segment class
class segment(object):
    def __init__(self, segment):
        points = re.split(" -> |,",segment)
        self.x1 = int(points[0])
        self.y1 = int(points[1])
        self.x2 = int(points[2])
        self.y2 = int(points[3])

        if self.x1 == self.x2:
            self.orientation = "vertical"
        elif self.y1 == self.y2:
            self.orientation = "horizontal"
        else:
            self.orientation = "diagonal"

    # returns a list of points in the line
    def get_points(self):
        points = []
        points.append([self.x1, self.y1])

        if self.x1 > self.x2:
            xmod = -1
        else:
            xmod = 1

        if self.y1 > self.y2:
            ymod = -1
        else:
            ymod = 1

        if self.orientation == "horizontal":
            distance = self.x2 - self.x1
            if xmod > 0:
                for i in range(distance - 1):
                    points.append([self.x1 + i + 1, self.y1])
            if xmod < 0:
                for i in range(abs(distance) - 1):
                    points.append([self.x1 - i - 1, self.y1])

        elif self.orientation == "vertical":
            distance = self.y2 - self.y1

            if ymod > 0:
                for i in range(distance - 1):
                    points.append([self.x1, self.y1 + i + 1])
            if ymod < 0:
                for i in range(abs(distance) - 1):
                    points.append([self.x1, self.y1 - i - 1])
        else:
            distance = self.y2 - self.y1
            if ymod > 0:
                if xmod > 0:
                    for i in range(distance - 1):
                        points.append([self.x1 + i + 1, self.y1 + i + 1])
                if xmod < 0:
                    for i in range(distance - 1):
                        points.append([self.x1 - i - 1, self.y1 + i + 1])
            if ymod < 0:
                if xmod < 0:
                    for i in range(abs(distance) - 1):
                        points.append([self.x1 - i - 1, self.y1 - i - 1])
                if xmod > 0:
                    for i in range(abs(distance) - 1):
                        points.append([self.x1 + i + 1, self.y1 - i - 1])


        points.append([self.x2, self.y2])
        return points

### defining function to compare points
def compare_points(x, y):
    global count
    for i in y:

        if (i in x) and (i not in overlap_points):
            overlap_points.append(i)


####### PART 1
### reading in the data
with open(".\day5.txt") as f:
    for line in f:
        inputs.append(line.rstrip())

### creating segments
for i in inputs:
    segments.append(segment(i))

### find matching points
for i in range(len(segments)):
    for j in range(len(segments) - i - 1):
        if segments[i].orientation != "diagonal" and segments[i + j + 1].orientation != "diagonal":
            compare_points(segments[i].get_points(), segments[i + j + 1].get_points())
print(len(overlap_points))


########### PART 2
overlap_points = []
for i in range(len(segments)):
    for j in range(len(segments) - i - 1):
        compare_points(segments[i].get_points(), segments[i + j + 1].get_points())
print(len(overlap_points))
