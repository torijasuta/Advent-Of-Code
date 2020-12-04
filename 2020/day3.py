import pandas as pd

input_df = pd.read_csv('2020/day3_input.txt', header=None)
input_df.columns=['input']
input_list = input_df['input'].tolist()

print('input read in. there are {len} items in input'.format(len=len(input_list)))

input_list_expanded = []

# expand the input rows to many times their size
for i in input_list:
    i_new = i * 200
    input_list_expanded.append(i_new)
# modulo would be not require this oh well

# part one
tree_count = 0
line_count = 0

for i in input_list_expanded:
    print(i)
    if i[line_count*3] == '#':
        tree_count += 1
    line_count += 1

print(tree_count)


# part_two
saved_routes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
saved_route_trees = []

for r in saved_routes:
    tree_count = 0
    print(r)

    i = 0
    while i < len(input_list_expanded):
        print(i)
        if i == 0:
            if input_list_expanded[i][0] == '#':
                tree_count += 1
        else:
            if input_list_expanded[i][int((i/2)*r[0])] == '#':
                tree_count += 1
        i += r[1]

    saved_route_trees.append(tree_count)
    print(tree_count)

print(saved_route_trees[0]*saved_route_trees[1]*saved_route_trees[2]*saved_route_trees[3]*saved_route_trees[4])