# Load data, then clean it up into a useable format.
import pandas as pd
data = pd.read_csv('data/day9.csv', header = None)[0]
data_parsed = list()
for entry in data:
    entry_parsed = entry.split(' ')
    direction = entry_parsed[0]
    magnitude = int(entry_parsed[1])
    data_parsed.append([direction, magnitude])

number_of_knots = 10
head = [0,0]
head_locations = list()
head_locations.append(head.copy())

for entry in data_parsed:
    direction = entry[0]
    magnitude = entry[1]
    for i in range(magnitude):
        if direction == 'R':
            head[0] += 1
        elif direction == 'L':
            head[0] -= 1
        elif direction == 'U':
            head[1] += 1
        elif direction == 'D':
            head[1] -= 1
        else:
            pass
        head_locations.append(head.copy())

for knot in range(number_of_knots - 1):
    tail = [0,0]
    tail_locations = list()
    tail_locations.append(tail.copy())

    for head in head_locations:
        if head[0] == tail[0]:
            if abs(head[1] - tail[1]) <= 1:
                pass
            else:
                tail[1] = tail[1] + int((head[1]-tail[1])/abs(head[1]-tail[1]))

        elif head[1] == tail[1]:
            if abs(head[0] - tail[0]) <= 1:
                pass
            else:
                tail[0] = tail[0] + int((head[0]-tail[0])/abs(head[0]-tail[0]))

        else:
            if (abs(head[0] - tail[0]) + abs(head[1] - tail[1])) == 2:
                pass
            else:
                x_move = int((head[0]-tail[0])/abs(head[0]-tail[0]))
                y_move = int((head[1]-tail[1])/abs(head[1]-tail[1]))
                tail[0] = tail[0] + x_move
                tail[1] = tail[1] + y_move

        tail_locations.append(tail.copy())
        head_locations = tail_locations.copy()

unique_locations = list()
[unique_locations.append(x) for x in tail_locations if x not in unique_locations]
print(len(unique_locations))
