


def test_for_output(noun, verb):

    # reset_memory every loop
    intcode = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 2, 19, 6, 23, 2, 13, 23, 27, 1, 9, 27, 31,
               2, 31, 9, 35, 1, 6, 35, 39, 2, 10, 39, 43, 1, 5, 43, 47, 1, 5, 47, 51, 2, 51, 6, 55, 2, 10, 55, 59, 1,
               59, 9, 63, 2, 13, 63, 67, 1, 10, 67, 71, 1, 71, 5, 75, 1, 75, 6, 79, 1, 10, 79, 83, 1, 5, 83, 87, 1, 5,
               87, 91, 2, 91, 6, 95, 2, 6, 95, 99, 2, 10, 99, 103, 1, 103, 5, 107, 1, 2, 107, 111, 1, 6, 111, 0, 99,
               2, 14, 0, 0]

    intcode[1] = noun
    intcode[2] = verb

    for i in range(0, len(intcode), 4):
        opcode = intcode[i]

        if opcode == 1:
            intcode[intcode[i+3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
        elif opcode == 2:
            intcode[intcode[i+3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
        elif opcode == 99:
            # print('ending')
            break
        else:
            # print('bad opcode')
            break

    return intcode[0]


for noun in range(0,100):
    for verb in range(0,100):
        return_val = test_for_output(noun, verb)
        if return_val == 19690720:
        # if return_val == 3716293:
            print('Noun: ', noun)
            print('Verb: ', verb)

            # print the answer
            print(100 * noun + verb)
