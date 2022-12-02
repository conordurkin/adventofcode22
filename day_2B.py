# The usual imports
import pandas as pd
data = pd.read_csv('data/day2.csv', header = None, skip_blank_lines = False, sep = ' ')
data.columns = ['Play', 'Response']

# New function to calculate scores
def score_calc(df):
    play = df.Play
    outcome = df.Outcome

    if ((play == 'A' and outcome == 'X') or (play == 'B' and outcome == 'Z') or (play == 'C' and outcome == 'Y')):
        shape = 3
    elif ((play == 'A' and outcome == 'Y') or (play == 'B' and outcome == 'X') or (play == 'C' and outcome == 'Z')):
        shape = 1
    elif ((play == 'A' and outcome == 'Z') or (play == 'B' and outcome == 'Y') or (play == 'C' and outcome == 'X')):
        shape = 2
    else:
        outcome = 'Error'

    if outcome == 'X':
        result = 0
    elif outcome == 'Y':
        result = 3
    elif outcome == 'Z':
        result = 6
    else:
        shape = 'Error'

    score = shape + result
    return score

# ...And return the same kinda output
scores = data.apply(score_calc, axis = 1)
print(scores.sum())
