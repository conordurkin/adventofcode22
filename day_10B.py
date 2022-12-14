# Import data and packages
import pandas as pd
import numpy as np
data = pd.read_csv('data/day10.csv', header = None)[0]

# Set value to 1, and initialize list of values during each cycle
values_during_cycle = list([1])
value = 1

# Go through the data, processing one cycle at a time.
for instruction in data:
    if instruction == 'noop':
        values_during_cycle.append(value)
    else:
        instruction_parsed = instruction.split(' ')
        values_during_cycle.append(value)
        values_during_cycle.append(value)
        value = value + int(instruction_parsed[1])

# For Part B, I filter out that 'zeroeth' value from Part A
values_to_use = values_during_cycle[1:]

# Then compare the value to the location of the cursor (modulo 40)
list_of_outputs = []
for i in range(len(values_to_use)):
    j = i % 40
    if abs(values_to_use[i] - j) <= 1:
        value = 1
    else:
        value = 0
    list_of_outputs.append(value)

# Convert this list into six lists, then that into a dataframe
divided_output = [list_of_outputs[i:i + 40] for i in range(0, len(list_of_outputs), 40)]
final_output = pd.DataFrame(divided_output)

# Print that dataframe in a handy way
visual = pd.DataFrame((np.where(final_output > 0, u"\u2588", '')))
print(visual)
