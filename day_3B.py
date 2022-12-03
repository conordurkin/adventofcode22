import pandas as pd

# Get list of all the rucksacks, then an empty list of badges
rucksack_list = list(pd.read_csv('data/day3.csv', header = None, skip_blank_lines = False)[0])
badge_list = []

# Function to find the badges. First, pop three rucksacks, then dedup the first one (so we don't double count badges)
# Check every item in the first to see if it's in second and third. Add to list if so.
def find_badge(list_):
    while len(list_) > 0:
        one = list_.pop()
        one_dedup = "".join(set(one))
        two = list_.pop()
        three = list_.pop()

        for item in one_dedup:
            if (two.find(item) != -1) and (three.find(item) != -1):
                badge_list.append(item)
            else:
                pass

# Run the function
find_badge(rucksack_list)

# This is our same alpha converter from Part A
def alpha_converter(letter):
    if ord(letter) < 97:
        value = ord(letter) - 38
    else:
        value = ord(letter) - 96
    return value

# And we get the badge values with a list comprehension again
badge_values = [alpha_converter(letter) for letter in badge_list]

# ... then print the sum!
print(sum(badge_values))
