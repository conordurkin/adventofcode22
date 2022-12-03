import pandas as pd
data = pd.read_csv('data/day3.csv', header = None, skip_blank_lines = False)[0]

# Function to return the doubled item, for a given entry
def find_item(entry):
    total = len(entry)
    half = int(total / 2)
    compartment_1 = entry[:half]
    compartment_2 = entry[half:]
    for item in compartment_1:
        if compartment_2.find(item) != -1:
            return item
            break
        else:
            pass

# Apply this function over the full list of entries
items = data.apply(find_item)

# Function to convert letters to their numerical values
def alpha_converter(letter):
    if ord(letter) < 97:
        value = ord(letter) - 38
    else:
        value = ord(letter) - 96
    return value

# Apply function over list with a list comprehension
item_values = [alpha_converter(letter) for letter in items]

# Print the total!
print(sum(item_values))
