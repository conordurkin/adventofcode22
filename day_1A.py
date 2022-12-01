# Read in packages I need, then data, then name the data column
import pandas as pd
import numpy as np
import math

data = pd.read_csv('data/day1.csv', header = None, skip_blank_lines = False)
data.columns = ['food']

# Initialize a counter and a list
counter = 0
list_of_calories = [0]

# Cycle through the data. If it's a null, we create a new entry in the list (since we're onto a new elf)
# If not null, then add the calorie value to the existing calorie value in that entry.
for entry in data.food:
    if math.isnan(entry):
        counter += 1
        list_of_calories.append(0)
    else:
        list_of_calories[counter] += entry

# Print the largest calorie value (note: has to be integer, not a float!)
print(int(max(list_of_calories)))
