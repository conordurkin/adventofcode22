# Import the data, keep just the string itself
import pandas as pd
data = pd.read_csv('data/day6.csv', header = None)[0][0]

# Loop over the string, four characters at a time. Stop once we get four unique in a row.
# Print the location of the last of those four characters.
for i in range(len(data) -13):
    segment = (data[i:i+14])
    if (len(set(segment))) == 14:
        print(i+14)
        break
