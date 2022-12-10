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

# Now we find all the visible trees. Step 1 - all trees on the border are visible.
# Step 2 - all trees taller in any direction than the others are visible.

for row in np.arange(rows):
    for column in np.arange(cols):
        if (row == 0) or (column == 0):
            visibilities[column][row] = 1
        elif (row == max(np.arange(rows))) or (column == max(np.arange(cols))):
            visibilities[column][row] = 1
        else:
            if data.iloc[row, column] > data.iloc[0:row, column].max():
                visibilities.iloc[row,column] = 1

            elif data.iloc[row, column] > data.iloc[row+1:, column].max():
                visibilities.iloc[row,column] = 1

            elif data.iloc[row, column] > data.iloc[row, 0:column].max():
                visibilities.iloc[row,column] = 1

            elif data.iloc[row, column] > data.iloc[row, column+1:].max():
                visibilities.iloc[row,column] = 1
            else:
                pass

# Sum the total number of visible trees.
print(int(visibilities.sum().sum()))
