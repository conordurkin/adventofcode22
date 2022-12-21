# Import two useful packages and the data
import ast
import itertools

with open('data/day13.txt') as file:
    data = file.read().splitlines()

# Clean data up
data_cleaned = []
for line in data:
    if line != '':
        data_cleaned.append(ast.literal_eval(line))
data_cleaned.append([[2]])
data_cleaned.append([[6]])

# Big function here to identify right or wrong, recursively
def compare_codes(entry_a, entry_b):
    for (a, b) in itertools.zip_longest(entry_a, entry_b):
        if (type(a) == int) and (type(b) == int):
            if a < b:
                return True
            elif b < a:
                return False
        if a is None and b is not None:
            return True
        if a is not None and b is None:
            return False
        conclusion = None
        if (type(a) == list) and (type(b) == list):
            conclusion = compare_codes(a, b)
        if (type(a) == int) and (type(b) == list):
            conclusion = compare_codes([a], b)
        if (type(a) == list) and (type(b) == int):
            conclusion = compare_codes(a, [b])
        if conclusion == True or conclusion == False:
            return conclusion

data_sorted = []
data_sorted.append(data_cleaned.pop(0))

for a in data_cleaned:
    for i in range(len(data_sorted)):
        if compare_codes(a,data_sorted[i]) == True:
            data_sorted.insert(i, a)
            break
        elif i+1 == len(data_sorted):
            data_sorted.append(a)
        else:
            continue

print((data_sorted.index([[2]])+1)*((data_sorted.index([[6]])+1)))
