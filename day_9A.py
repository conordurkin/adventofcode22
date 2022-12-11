# Load data, then clean it up into a useable format.
import pandas as pd
data = pd.read_csv('data/day9.csv', header = None)[0]
data_parsed = list()
for entry in data:
    entry_parsed = entry.split(' ')
    direction = entry_parsed[0]
    magnitude = int(entry_parsed[1])
    data_parsed.append([direction, magnitude])

# Initialize with our zeroes and lists of head and tail locations.
head = [0,0]
tail = [0,0]
head_locations = list()
tail_locations = list()
head_locations.append(head.copy())
tail_locations.append(tail.copy())

# First loop - go through the data parsed to make a trail of where the head goes.
# Pass these locations onto the head locations lists.
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

# Second loop - based on the head locations, figure out where the tail is.
# Pass these locations onto the tail location list.
for location in head_locations:
    if location[0] == tail[0]:
        if location[1] == tail[1]:
            pass
        elif abs(location[1] - tail[1]) > 1:
            tail[1] = (location[1] + tail[1]) / 2
        else:
            pass
    else:
        if location[1] == tail[1]:
            if abs(location[0] - tail[0]) > 1:
                tail[0] = (location[0] + tail[0]) / 2
            else: 
                pass
        else:
            if abs(location[1] - tail[1]) > 1:
                tail[1] = (location[1] + tail[1]) / 2
                tail[0] = location[0]
            elif abs(location[0] - tail[0]) > 1:
                tail[0] = (location[0] + tail[0]) / 2
                tail[1] = location[1]
            else:
                pass
    tail_locations.append(tail.copy())

# Dedup the tail locations and print the total unique locations.
unique_locations = list()
[unique_locations.append(x) for x in tail_locations if x not in unique_locations]
print(len(unique_locations))
