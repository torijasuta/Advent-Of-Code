import pandas as pd

dict_list = []
count = 0
tmp_dict = {}

file1 = open('2020/day4_input.txt', 'r')

while True:
    count += 1

    line = file1.readline()

    if line.rstrip():
        line_split = line.split(' ')
        for i in line_split:
            tmp_key = i.split(':')[0].strip()
            tmp_value = i.split(':')[1].strip()
            tmp_dict[tmp_key] = tmp_value

    if not line.rstrip():
        dict_list.append(tmp_dict)
        tmp_dict = {}

    if not line:
        break

file1.close()

df = pd.DataFrame(dict_list)

pt1_df = df[['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']].copy()
pt1_df.dropna(how='any', inplace=True)

# part one answer:
print(pt1_df.shape[0])

pt1_df['byr'] = pt1_df['byr'].astype(int)
pt1_df['iyr'] = pt1_df['iyr'].astype(int)
pt1_df['eyr'] = pt1_df['eyr'].astype(int)

# part two
pt2_df = pt1_df[pt1_df['byr']<=2002]
pt2_df = pt2_df[pt2_df['byr']>=1920]

pt2_df = pt2_df[pt2_df['iyr']>=2010]
pt2_df = pt2_df[pt2_df['iyr']<=2020]

pt2_df = pt2_df[pt2_df['eyr']>=2020]
pt2_df = pt2_df[pt2_df['eyr']<=2030]

# height #150-193cm or #59-76in
pt2_df = pt2_df[pt2_df['hgt'].str.contains('^1[5-8][0-9]cm$|^1[9][0-3]cm$|^59in$|^6[0-9]in$|^7[0-6]in$')]
pt2_df = pt2_df[pt2_df['hcl'].str.contains('^#[a-f0-9]{6,6}$')]  # only these chars
pt2_df = pt2_df[pt2_df['hcl'].str.len()==7]  # exactly 7 chars

pt2_df = pt2_df[pt2_df['ecl'].isin(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])]

pt2_df = pt2_df[pt2_df['pid'].str.contains('^[0-9]{9,9}$')]  # only these digits
pt2_df = pt2_df[pt2_df['pid'].str.len()==9]  # exactly 9 chars

# part two answer
print(pt2_df.shape[0])
