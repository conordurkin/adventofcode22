import pandas as pd

data = pd.read_csv('data/day2.csv', header = None, skip_blank_lines = False, sep = ' ')
data.columns = ['Play', 'Response']

def score_calc(df):
    play = df.Play
    response = df.Response

    if ((play == 'A' and response == 'X') or (play == 'B' and response == 'Y') or (play == 'C' and response == 'Z')):
        outcome = 3
    elif ((play == 'A' and response == 'Y') or (play == 'B' and response == 'Z') or (play == 'C' and response == 'X')):
        outcome = 6
    elif ((play == 'A' and response == 'Z') or (play == 'B' and response == 'X') or (play == 'C' and response == 'Y')):
        outcome = 0
    else:
        outcome = 'Error'

    if response == 'X':
        shape = 1
    elif response == 'Y':
        shape = 2
    elif response == 'Z':
        shape = 3
    else:
        shape = 'Error'

    score = shape + outcome
    return score

scores = data.apply(score_calc, axis = 1)

print(scores.sum())
