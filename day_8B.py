# Import data packages
import pandas as pd
import numpy as np

# Import data, convert it to a dataframe, then clean it up. End result is a square with one number per box.
data = pd.read_csv('data/day8.csv', header = None)
data = data[0].astype('str').str.split('', expand = True)
data = data.apply(pd.to_numeric)
data = data.drop([0, 100], axis = 1)
data.columns = np.arange(99)

# Store number of total rows and columns
rows = data.shape[0]
cols = data.shape[1]

# Create a dataframe of zeros the same size as the data.
visibilities = pd.DataFrame(np.zeros((rows, cols)))

for row in np.arange(rows):
    for column in np.arange(cols):
        if (row == 0) or (column == 0):
            visibilities.iloc[row,column] = 0
        elif (row == max(np.arange(rows))) or (column == max(np.arange(cols))):
            visibilities.iloc[row,column] = 0
        else:
            check_north = True
            north = 0
            for i in np.arange(1, row+1):
                if check_north == True:
                    if data.iloc[row, column] > data.iloc[row - i, column]:
                        north += 1
                    else:
                        north += 1
                        check_north = False
                else:
                    pass

            check_south = True
            south = 0
            for i in np.arange(1, rows-row):
                if check_south == True:
                    if data.iloc[row, column] > data.iloc[row + i, column]:
                        south += 1
                    else:
                        south += 1
                        check_south = False
                else:
                    pass

            check_east = True
            east = 0
            for i in np.arange(1, cols-column):
                if check_east == True:
                    if data.iloc[row, column] > data.iloc[row, column+i]:
                        east += 1
                    else:
                        east += 1
                        check_east = False
                else:
                    pass

            check_west = True
            west = 0
            for i in np.arange(1, column + 1):
                if check_west == True:
                    if data.iloc[row, column] > data.iloc[row, column - i]:
                        west += 1
                    else:
                        west += 1
                        check_west = False
                else:
                    pass
            else:
                pass
            total_vision = north * south * east * west
            visibilities.iloc[row,column] = total_vision

print(int(visibilities.max().max()))
