# Load packages and datafile
import numpy as np
import pandas as pd
import ast

with open('data/day14.txt') as file:
    data = file.read().splitlines()

# We'll use this function to help parse the datafile
def get_segment(a, b):
    segment_list = list()
    if a[0] == b[0]:
        seg_len = abs(b[1] - a[1])
        iteration = int(b[1] - a[1]) / abs(b[1] - a[1])
        entry = (a[0], a[1])
        i = 0
        while i <= seg_len:
            segment_list.append(entry)
            entry = (a[0], int(entry[1] + iteration))
            i += 1
    else:
        seg_len = abs(b[0] - a[0])
        iteration = int(b[0] - a[0]) / abs(b[0] - a[0])
        entry = (a[0], a[1])
        i = 0
        while i <= seg_len:
            segment_list.append(entry)
            entry = (int(entry[0] + iteration), a[1])
            i += 1
    return segment_list

# Parsing data into a list of cells to solidify
data_parsed = list()
for line in data:
    string_coords = line.split(' -> ')
    coord_list = list()
    for coord in string_coords:
        real = ast.literal_eval(coord)
        coord_list.append(real)
    data_parsed.append(coord_list)

solid_coords = list()
for row in data_parsed:
    segments = len(row) - 1
    i = 0
    while i < segments:
        solid_coords.append(get_segment(row[i], row[i+1]))
        i += 1

solid_coords_unique = set([item for sublist in solid_coords for item in sublist])

# Okay, now time to set up the grid itself
x_list = list()
y_list = list()
for entry in solid_coords_unique:
    x_list.append(entry[0])
    y_list.append(entry[1])

x_range = np.arange(min(x_list), max(x_list)+1)
y_dim = max(y_list)

grid = pd.DataFrame(columns = x_range)
grid = grid.reindex(list(range(y_dim+1))).reset_index(drop = True).fillna('.')

for cell in solid_coords_unique:
    grid.loc[cell[1],cell[0]] = '#'


# Now a function to simulate one unit of sand
def simulate_sand(start):
    df = start.copy()
    sand = (500,0)
    df[sand[0]][sand[1]] = 'o'
    settled = 0
    while settled == 0:
        if df[sand[0]][sand[1]+1] == '.':
            df[sand[0]][sand[1]] = '.'
            sand = (sand[0],sand[1]+1)
            df[sand[0]][sand[1]] = 'o'
        elif df[sand[0]-1][sand[1]+1] == '.':
            df[sand[0]][sand[1]] = '.'
            sand = (sand[0]-1,sand[1]+1)
            df[sand[0]][sand[1]] = 'o'
        elif df[sand[0]+1][sand[1]+1] == '.':
            df[sand[0]][sand[1]] = '.'
            sand = (sand[0]+1,sand[1]+1)
            df[sand[0]][sand[1]] = 'o'
        else:
            settled = 1
    return df

# A function to keep simulating sand until we can't anymore. This returns the number of sand units we could run.
def try_sand(start_df):
    i = 0
    status = start_df.copy()
    while True:
        try:
            status = simulate_sand(status)
            i += 1
        except:
            return i

print(try_sand(grid))
