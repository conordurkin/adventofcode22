import pandas as pd
with open('data/day5.csv') as file:
    data = file.readlines()

# Divide the data into two sets - the starting grid and the set of moves.
start_boxes = data[:9]
moves = data[10:]

# Okay, now clean up the starting grid. Lot of work here!
# I turn it into a df, then turn the df into a series of lists (one per column) which keep only the letters.
parsed_boxes = [list(box) for box in start_boxes]
columns_to_keep = [i*4+1 for i in range(9)]

boxes_df = pd.DataFrame(parsed_boxes)
boxes_df = boxes_df[columns_to_keep]
boxes_df = boxes_df.loc[0:7]
boxes_df.columns = range(1,10)

boxes_df = boxes_df.replace({' ': None})

stack_list = list()
for column in boxes_df.columns:
    stack = list()
    for entry in boxes_df[column]:
        if entry is None:
            pass
        else:
            stack.insert(0, entry)
    stack_list.append(stack)


# Now working on the moves. Keep only the number of boxes we move, and the start/end points of those boxes.
# Note I turn the start/end points into indeces rather than their 'names' (e.g. 0,1,2,3... instead of 1,2,3,4...)
move_list = list()
for line in moves:
    line = line.rstrip('\n')
    a,b,c,d,e,f = line.split(' ')
    move_list.append([int(b),int(d)-1,int(f)-1])

# Then make all the moves. Kinda hacky use of a counter here, and a lot of popping.
for move in move_list:
    boxes = move[0]
    pickup = move[1]
    dropoff = move[2]
    counter = 0
    while counter < boxes:
        box_to_move = stack_list[pickup].pop()
        stack_list[dropoff].append(box_to_move)
        counter += 1

# Find the top boxes, join them as a string. 
top_boxes = [stack.pop() for stack in stack_list]
print(''.join(top_boxes))
