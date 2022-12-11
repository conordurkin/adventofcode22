# Load data, then clean it up into a useable format.
import pandas as pd
data = pd.read_csv('data/day9.csv', header = None)[0]
data_parsed = list()
for entry in data:
    entry_parsed = entry.split(' ')
    direction = entry_parsed[0]
    magnitude = int(entry_parsed[1])
    data_parsed.append([direction, magnitude])

# Initialize with our zeroes and a list of tail locations.
head = [0,0]
tail = [0,0]
tail_locations = list()
tail_locations.append(tail.copy())

# For loop to parse. Load direction, iterate the Head in that direction step by step.
# If tail is too far from head, iterate the tail in the appropriate direction.
# After each step, append the tail location to our list.
for entry in data_parsed:
    direction = entry[0]
    magnitude = entry[1]
    if direction == 'R':
        for i in range(magnitude):
            head[0] += 1
            if head[1] == tail[1]:
                if head[0] > tail[0] + 1:
                    tail[0] += 1
                else:
                    pass
            else:
                if head[0] > tail[0] + 1:
                    tail[1] = head[1]
                    tail[0] += 1
                else:
                    pass
            tail_locations.append(tail.copy())
    elif direction == 'L':
        for i in range(magnitude):
            head[0] += -1
            if head[1] == tail[1]:
                if head[0] < tail[0] -1:
                    tail[0] += -1
            else:
                if head[0] < tail[0] -1:
                    tail[1] = head[1]
                    tail[0] += -1
                else:
                    pass
            tail_locations.append(tail.copy())
    elif direction == 'U':
        for i in range(magnitude):
            head[1] += 1
            if head[0] == tail[0]:
                if head[1] > tail[1] + 1:
                    tail[1] += 1
                else:
                    pass
            else:
                if head[1] > tail[1] + 1:
                    tail[0] = head[0]
                    tail[1] += 1
                else:
                    pass
            tail_locations.append(tail.copy())
    elif direction == 'D':
        for i in range(magnitude):
            head[1] += -1
            if head[0] == tail[0]:
                if head[1] < tail[1] -1:
                    tail[1] += -1
            else:
                if head[1] < tail[1] -1:
                    tail[0] = head[0]
                    tail[1] += -1
                else:
                    pass
            tail_locations.append(tail.copy())
    else:
        pass

# Dedup the tail locations and print the total unique locations.
unique_locations = list()
[unique_locations.append(x) for x in tail_locations if x not in unique_locations]
print(len(unique_locations))
