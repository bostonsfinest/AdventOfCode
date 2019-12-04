def compute(arr, ind):
    if arr[ind] == 1:
        res = arr[arr[ind+1]] + arr[arr[ind+2]]
        arr[arr[ind+3]] = res
        return (0, arr)
    elif arr[ind] == 2:
        res = arr[arr[ind+1]] * arr[arr[ind+2]]
        arr[arr[ind+3]] = res
        return (0, arr)
    elif arr[ind] == 99:
        return (1, arr)
    else:
        print(f'Error: unknown opcode ({arr[ind+3]})')


def compute_intcode_part1():
    with open('intcode.txt') as f:
        intcode = f.read()
    ic_arr = intcode.split(',')
    ic_arr = (0, [int(n) for n in ic_arr])
    for ind in range(0, len(ic_arr[1]), 4):
        ic_arr = compute(ic_arr[1], ind)
        if ic_arr[0]:
            print(f"PART 1: {ic_arr[1][0]}")
            return


def compute_intcode_part2():
    for noun in range(0, 100):
        for verb in range(0, 100):
            with open('intcode.txt') as f:
                intcode = f.read()
            ic_arr = intcode.split(',')
            ic_arr = (0, [int(n) for n in ic_arr])
            ic_arr[1][1] = noun
            ic_arr[1][2] = verb
            for ind in range(0, len(ic_arr[1]), 4):
                ic_arr = compute(ic_arr[1], ind)
                if ic_arr[0] and ic_arr[1][0] == 19690720:
                    print(f"PART 2: {100 * noun + verb}")
                    return
                if ic_arr[0]:
                    break


if __name__ == '__main__':
    compute_intcode_part1()
    compute_intcode_part2()
