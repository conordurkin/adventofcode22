# Load Packages and data
import pandas as pd
import numpy as np
from collections import defaultdict, deque
with open('data/day12.txt') as file:
    data = file.read().splitlines()

# Clean up the data into a nice dataframe, one character per cell
data = pd.DataFrame(data)
data = data[0].astype('str').str.split('', expand = True)
data = data.iloc[:, 1:-1]
data.columns = np.arange(len(data.columns))

# Get row count, col count, initialize the starting cell
n_rows = data.shape[0]
n_cols = data.shape[1]

# Quick loop to find the Goal point
for row in range(n_rows):
    for col in range(n_cols):
        if data.iloc[row][col] == 'E':
            goal = (row, col)
        else:
            pass

# Function to return a modified 'height' of a given cell to figure out valid paths
def custom_ord(char):
    if char == 'S':
        out = 97
    elif char == 'E':
        out = 122
    else:
        out = ord(char)
    return out

# We're going to solve this backwards, so here's a modified function to find every valid
# Backwards adjacent path for a given cell
def valid_adjacent_path(cell):
    possible_adjacent = list()
    adjacent_cells = list()
    possible_adjacent.append((cell[0], cell[1]-1))
    possible_adjacent.append((cell[0], cell[1]+1))
    possible_adjacent.append((cell[0]-1, cell[1]))
    possible_adjacent.append((cell[0]+1, cell[1]))
    for option in possible_adjacent:
        if (option[0] >= 0) and (option[0] < n_rows) and (option[1] >= 0) and (option[1] < n_cols):
            if custom_ord(data.iloc[option[0], option[1]]) >= custom_ord(data.iloc[cell[0],cell[1]]) - 1:
                adjacent_cells.append(option)
    return adjacent_cells

# Create a defaultdict with all of the valid adjacencies for a given cell
nodes = defaultdict(list)
for row in range(n_rows):
    for col in range(n_cols):
        cell_to_run = (row, col)
        for entry in valid_adjacent_path(cell_to_run):
            nodes[cell_to_run].append(entry)


# Function to find the shortest path using breadth-first search (Depth did not work!)

def shortest_path_down(graph, apex):
    path_list = [[apex]]
    path_index = 0
    previous_nodes = {apex}

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]

        for next_node in next_nodes:

            if custom_ord(data.iloc[next_node[0],next_node[1]]) == 97:
                current_path.append(next_node)
                return current_path

            elif not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1

# Run function, find the shortest path
print(len(shortest_path_down(nodes, goal)) - 1)
