input_val_min = 193651
output_val_max = 649729

part_two = True

def has_double_digit(digit_list):
    truth = False
    for i in range(0, len(digit_list) - 1):
        if digit_list[i] == digit_list[i + 1]:

            if part_two is True:
                if digit_list.count(digit_list[i]) == 2:
                    truth = True
            else:
                truth = True

    return truth


def check_ascending(digit_list):
    truth = True
    for i in range(0, len(digit_list) - 1):
        if digit_list[i] > digit_list[i + 1]:
            truth = False
    return truth

counter = 0

for i in range(input_val_min, output_val_max+1):

    # puts digits into a list
    tmp_digit_list = []
    for d in str(i):
        tmp_digit_list.append(d)

    # check that is 6-digit number
    if len(tmp_digit_list) == 6:
        if has_double_digit(tmp_digit_list):
            if check_ascending(tmp_digit_list):
                counter += 1

print(counter)
