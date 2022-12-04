# Import data and packages
import pandas as pd
data = pd.read_csv('data/day4.csv', header = None, skip_blank_lines = False)
data.columns = ['first', 'second']

# Function to turn data into lists, then compare the lists for a perfect overlap.
def check_assignment_overlaps(df):
    elf_a = df['first']
    elf_a_start = int(elf_a.split('-')[0])
    elf_a_finish = int(elf_a.split('-')[1])
    elf_a_range = list(range(elf_a_start, elf_a_finish+1))

    elf_b = df['second']
    elf_b_start = int(elf_b.split('-')[0])
    elf_b_finish = int(elf_b.split('-')[1])
    elf_b_range = list(range(elf_b_start, elf_b_finish+1))

    check_a = all(assignment in elf_a_range for assignment in elf_b_range)
    check_b = all(assignment in elf_b_range for assignment in elf_a_range)

    if (check_a or check_b):
        out = 1
    else:
        out = 0
    return out

# Print number of perfect overlaps.
print(sum(data.apply(check_assignment_overlaps, axis = 1)))
