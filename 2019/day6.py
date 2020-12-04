import pandas as pd
from anytree import Node, RenderTree

# u-g-l-y
# part 1 only

def loop_through_inputs(input_list):
    for i in input_list:
        parent = i.split(')')[0]
        child = i.split(')')[1]
        try:
            globals()[child] = Node(child, parent=globals()[parent])
            nodes.append(globals()[child])
            completed_inputs.append(i)
            input_list.remove(i)
        except:
            pass
    return input_list, completed_inputs, nodes


input_df = pd.read_csv('day6_input.txt', header=None)
input_df.columns=['input']
input_list = input_df['input'].tolist()
# input_list = ['J)K', 'K)L', 'COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', ]

completed_inputs = []
nodes = []

COM = Node('COM')

while len(input_list) > 0:
    input_list, completed_inputs, nodes = loop_through_inputs(input_list)
    # print(len(input_list))

counter = 0
for i in nodes:
    tmp_count = str(i).count('/') - 1
    counter += tmp_count

print(counter)