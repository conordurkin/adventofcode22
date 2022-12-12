# Import data and packages
import pandas as pd
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

# Get the signal strength from the "interesting signals" and sum them. 
signal_sum = 0
for i in range(6):
    cycle = 20 + 40 * i
    signal_sum += values_during_cycle[cycle] * cycle

print(signal_sum)
