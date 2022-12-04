import pandas as pd
data = pd.read_csv('data/day4.csv', header = None, skip_blank_lines = False)
data.columns = ['first', 'second']

# First, convert the assignments to lists.
# Then, check if the sum of the lengths of each list equals the length of a combined deduped list.
# If not --> then there must be overlap.

def check_assignment_any_overlaps(df):
    elf_a = df['first']
    elf_a_start = int(elf_a.split('-')[0])
    elf_a_finish = int(elf_a.split('-')[1])
    elf_a_range = list(range(elf_a_start, elf_a_finish+1))

    elf_b = df['second']
    elf_b_start = int(elf_b.split('-')[0])
    elf_b_finish = int(elf_b.split('-')[1])
    elf_b_range = list(range(elf_b_start, elf_b_finish+1))

    combo = list(set(elf_a_range + elf_b_range))

    len_a = len(elf_a_range)
    len_b = len(elf_b_range)

    len_combo = len(combo)

    if len_combo == (len_a + len_b):
        out = 0
    else:
        out = 1
    return out

# Then apply to all rows and sum the overlap rows.
print(sum(data.apply(check_assignment_any_overlaps, axis = 1)))
