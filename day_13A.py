# Import two useful packages and the data
import ast
import itertools

with open('data/day13.txt') as file:
    data = file.read().splitlines()

# Clean data up
data_cleaned = []
left = []
right = []

for line in data:
    if line == '':
        pass
    else:
        data_cleaned.append(ast.literal_eval(line))

while len(data_cleaned) > 0:
    left.append(data_cleaned.pop(0))
    right.append(data_cleaned.pop(0))

# Big function here to evaluate things - recursive!
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

# Store the outcomes here
outcomes = []
for i in range(len(left)):
    left_check = left.pop(0)
    right_check = right.pop(0)
    outcomes.append(compare_codes(left_check, right_check))

#
outcome_sum = 0
for i in range(len(outcomes)):
    if outcomes[i] == True:
        outcome_sum += (i+1)

print(outcome_sum)
