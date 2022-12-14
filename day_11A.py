# Load data
with open('data/day11.txt') as file:
    data = file.read().splitlines()

# Initialize a bunch of empty lists plus the round count
monkey_items = []
monkey_counter = []
operations = []
tests = []
test_true = []
test_false = []
rounds = 20

# Parse the raw data, allocating elements to the appropriate list.
for line in data:
    line_parsed = line.strip().split(':')
    if line_parsed[0][0:6] ==  'Monkey':
        monkey_counter.append(0)
    elif line_parsed[0] == 'Starting items':
        items = line_parsed[1].strip().split(', ')
        integer_items = [eval(item) for item in items]
        monkey_items.append(integer_items)
    elif line_parsed[0] == 'Operation':
        operation_parsed = line_parsed[1].split(' new = ')[1]
        operations.append(operation_parsed)
    elif line_parsed[0] == 'Test':
        divisor = int(line_parsed[1].strip().split(' ')[2])
        tests.append(divisor)
    elif line_parsed[0] == 'If true':
        new_monkey = int(line_parsed[1].strip().split(' ')[3])
        test_true.append(new_monkey)
    elif line_parsed[0] == 'If false':
        new_monkey = int(line_parsed[1].strip().split(' ')[3])
        test_false.append(new_monkey)
    else:
        pass

# Run through round by round.
for round in range(rounds):
    for monkey in range(len(monkey_counter)):
        for item in range(len(monkey_items[monkey])):
            monkey_counter[monkey] += 1
            old = monkey_items[monkey].pop(0)
            new = eval(operations[monkey])
            new = int(new / 3)
            if (new % tests[monkey] == 0):
                monkey_items[test_true[monkey]].append(new)
            else:
                monkey_items[test_false[monkey]].append(new)

# Sort the inspection count list, then print product of top 2
monkey_counter.sort(reverse=True)
print(monkey_counter[0] * monkey_counter[1])
