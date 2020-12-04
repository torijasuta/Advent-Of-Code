import pandas as pd

input_df = pd.read_csv('day1_input.txt', header=None)
input_df.columns=['input']
input_list = input_df['input'].tolist()

print('input read in. there are {len} items in input'.format(len=len(input_list)))

# part 1
for i in input_list:
    if 2020-i in input_list:
        print(i)
        print(2020-i)
        print(i*(2020-i))
        print('')
        
# part 2
for i in range(0,len(input_list)):
    num1 = input_list[i]
    for j in range(0, len(input_list)):
        num2 = input_list[j]
        for k in range(0, len(input_list)):
            num3 = input_list[k]
            if num1 + num2 + num3 == 2020:
                print(num1, ',', num2, ',', num3)
                print(num1*num2*num3)
            k+=1
        j+=1
    i+=1
        
# could add a stop mechanism; all combos print
