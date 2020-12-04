import pandas as pd

input_df = pd.read_csv('2020/day2_input.txt', header=None)
input_df.columns=['input']
input_list = input_df['input'].tolist()

print('input read in. there are {len} items in input'.format(len=len(input_list)))

count = 0

# part one

for i in input_list:
    split_list_hyphen = str(i).split('-',1)
    letter_min = split_list_hyphen[0]
    split_list_space = split_list_hyphen[1].split(' ')
    letter_max = split_list_space[0]
    letter = split_list_space[1].replace(':', '')
    password = split_list_space[2]

    letter_count = password.count(letter)
    if letter_count >= int(letter_min):
        if letter_count <= int(letter_max):
            count += 1
print(count)

# part two

count = 0

for i in input_list:
    split_list_hyphen = str(i).split('-',1)
    letter_pos1 = int(split_list_hyphen[0])
    split_list_space = split_list_hyphen[1].split(' ')
    letter_pos2 = int(split_list_space[0])
    letter = split_list_space[1].replace(':', '')
    password = split_list_space[2]

    if password[letter_pos1-1] == letter:
        if password[letter_pos2-1] == letter:
                continue
        else:
            count += 1  # first position correct, 2nd not

    elif password[letter_pos2-1] == letter:
            count += 1  # first position incorrect, 2nd correct

print(count)