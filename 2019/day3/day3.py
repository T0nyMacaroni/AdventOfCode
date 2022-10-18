#!/usr/bin/python3

input = open("input", "r")

wire1 = input.readline().split(',')
wire2 = input.readline().split(',')

# getting rid of the /n in the last element
wire1[-1] = wire1[-1][0:-1]
wire2[-1] = wire2[-1][0:-1]

GRID = []
CROSS = []
distances = []
center = []

RUN = False


def calc_grid(wire):
    x_max = 0
    x_min = 0
    x_val = 0
    y_max = 0
    y_min = 0
    y_val = 0
    for element in wire:
        if element[0:1] == 'R':
            x_val = x_val + int(element[1:])
        elif element[0:1] == 'L':
            x_val = x_val - int(element[1:])
        elif element[0:1] == 'U':
            y_val = y_val + int(element[1:])
        elif element[0:1] == 'D':
            y_val = y_val - int(element[1:])
        else:
            print("error: unknown direction")

        if x_val > x_max:
            x_max = x_val

        if x_val < x_min:
            x_min = x_val

        if y_val > y_max:
            y_max = y_val

        if y_val < y_min:
            y_min = y_val

    # print("XMAX: {}, XMIN: {}, YMAX: {}, YMIN: {}".format(x_max, x_min, y_max, y_min))
    return [x_max, x_min, y_max, y_min]


def draw_grid():
    w1 = calc_grid(wire1)
    w2 = calc_grid(wire2)
    x_max = w2[0]
    x_min = w2[1]
    y_max = w2[2]
    y_min = w2[3]

    if w1[0] > x_max:
        x_max = w1[0]

    if w1[2] > y_max:
        y_max = w1[2]

    if w1[1] < x_min:
        x_min = w1[1]

    if w1[3] < y_min:
        y_min = w1[3]

    x_length = x_max + abs(x_min) + 1
    y_length = y_max + abs(y_min) + 1

    for i in range(y_length):
        line = []
        for j in range(x_length):
            line.append(".")
        GRID.append(line)

    GRID[y_max][abs(x_min)] = "o"
    # print(y_max, y_length)
    return [y_max, abs(x_min)]


center = draw_grid()


def draw_line(wire, x_pos, y_pos, grid, run):
    for element in wire:
        if element[0:1] == 'R':
            distance = int(element[1:])
            for i in range(1, distance + 1):
                # print(y_pos,x_pos,i)
                if grid[y_pos][x_pos + i] == "w" and run == True:
                    grid[y_pos][x_pos + i] = "X"
                    CROSS.append([y_pos, x_pos + i])
                else:
                    grid[y_pos][x_pos + i] = "w"
            x_pos = x_pos + distance
        elif element[0:1] == 'L':
            distance = int(element[1:])
            for i in range(1, distance + 1):
                # print(y_pos,x_pos,i)
                if grid[y_pos][x_pos - i] == "w" and run == True:
                    grid[y_pos][x_pos - i] = "X"
                    CROSS.append([y_pos, x_pos - i])
                else:
                    grid[y_pos][x_pos - i] = "w"
            x_pos = x_pos - distance
        elif element[0:1] == 'U':
            distance = int(element[1:])
            for i in range(1, distance + 1):
                # print(y_pos,x_pos,i)
                if grid[(y_pos - i)][x_pos] == "w" and run == True:
                    grid[(y_pos - i)][x_pos] = "X"
                    CROSS.append([y_pos - i, x_pos])
                else:
                    grid[(y_pos - i)][x_pos] = "w"
            y_pos = y_pos - distance
        elif element[0:1] == 'D':
            distance = int(element[1:])
            for i in range(1, distance + 1):
                if grid[(y_pos + i)][x_pos] == "w" and run == True:
                    grid[(y_pos + i)][x_pos] = "X"
                    CROSS.append([y_pos + i, x_pos])
                else:
                    grid[(y_pos + i)][x_pos] = "w"
            y_pos = y_pos + distance
        else:
            print("error: unknown direction")
    RUN = True
    return grid


GRID = draw_line(wire1, center[1], center[0], GRID, RUN)
GRID = draw_line(wire2, center[1], center[0], GRID, True)

# Manhattan Distance = is |X1-Y1|+|X2-Y2|

for points in CROSS:
    distance = abs(center[0] - abs(points[0])) + abs(center[1] - abs(points[1]))
    distances.append(distance)

distances.sort()
print(distances)
