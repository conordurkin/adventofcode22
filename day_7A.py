# Import package and data
from collections import defaultdict
with open('data/day7.txt') as file:
    data = file.read().splitlines()

# Initialize our current location and an empty list we'll use here.
current_location = ''
data_with_abs_dir = list()

# We work our way through the data line by line. Every time a directory changes, we update our 'current location'.
# We then replace every directory reference in the data with a reference to the absolute path, rather than the local path.
for line in data:
    line_parsed = line.split(' ')
    if line_parsed[0].isdigit():
        data_with_abs_dir.append(line)
    elif line_parsed[0] == 'dir':
        new_dir = current_location + '-' + line_parsed[1]
        new_line = ' '.join([line_parsed[0], new_dir])
        data_with_abs_dir.append(new_line)
    else:
        if line_parsed[0] == '$':
            if line_parsed[1] == 'ls':
                data_with_abs_dir.append(line)
            elif line_parsed[1] == 'cd':
                if line_parsed[2] != '..':
                    current_location = current_location + '-' + line_parsed[2]
                    new_line = ' '.join([line_parsed[0], line_parsed[1], current_location])
                    data_with_abs_dir.append(new_line)
                else:
                    current_location = '-'.join(current_location.rsplit('-')[:-1])
                    data_with_abs_dir.append(line)
            else:
                print('You have missed a line! This one:' + str(line))
                break
        else:
            print('You have missed a line! This one:' + str(line))

# Now initialize a few values again.
dictionary_data_value = 0
dir_dict = defaultdict(int)

# Work our way backwards through the data. If a data file, update our current directory's memory value.
# If a directory, store that directory's total memory and reset the current directory's memory to zero.
# Keep going all the way up until we know every directory's value.
while len(data_with_abs_dir) > 0:
    entry = data_with_abs_dir.pop()
    entry_parsed = entry.split(' ')
    if entry_parsed[0].isdigit():
        dictionary_data_value += int(entry_parsed[0])
    elif entry_parsed[0] == 'dir':
        dictionary_data_value += dir_dict[entry_parsed[1]]
    else:
        if entry_parsed[0] == '$':
            if entry_parsed[1] == 'cd':
                if entry_parsed[2] == '..':
                    pass
                else:
                    dir_dict[entry_parsed[2]] += dictionary_data_value
                    dictionary_data_value = 0
            else:
                pass

# Voila, print the total data for those directories with under 100k 
total_data = 0
for dir in dir_dict:
    if dir_dict[dir] <= 100000:
        total_data += dir_dict[dir]
    else:
        pass
print(total_data)
