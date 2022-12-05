import pandas as pd
with open('adventofcode22/data/day5.csv') as file:
    data = file.readlines()

# Again, two sets in the data - grid and moves
start_boxes = data[:9]
moves = data[10:]

# Same cleaning up the starting grid.
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

# Same function to get a nice list of moves
move_list = list()
for line in moves:
    line = line.rstrip('\n')
    a,b,c,d,e,f = line.split(' ')
    move_list.append([int(b),int(d)-1,int(f)-1])

# Okay, now it's trickier. Basically, we need to insert the boxes in reverse order.
# So the first popped box is at the end, second is penultimate, etc.
# We can use the counter as a reverse index of where the boxes go!
for move in move_list:
    boxes = move[0]
    pickup = move[1]
    dropoff = move[2]
    counter = 0
    while counter < boxes:
        box_to_move = stack_list[pickup].pop()
        if counter == 0:
            stack_list[dropoff].append(box_to_move)
        else:
            stack_list[dropoff].insert(-counter, box_to_move)
        counter += 1

# Then we again find the top boxes and join the string. 
top_boxes = [stack.pop() for stack in stack_list]
print(''.join(top_boxes))
