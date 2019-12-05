# the program 1002,4,3,4,33.

def store(instr, ind):
    print('IN STORE')
    i = input()
    instr[int(instr[ind])] = i
    return instr

def retrieve(instr, ind):
    print('RET')
    print(instr[ind])

def decode(instr):
    print("INST", instr)
    modes = []
    mode = ''
    if len(instr) == 1:
        opcode = instr
    else:
        opcode = str(int(instr[-2:]))
    
    print("OPCODEMODE", opcode, mode)
    while len(mode) < len(instr):
        mode = '0' + mode
    for m in reversed(mode):
        modes.append(m)

    return (str(int(opcode)), modes)

    
def compute(instr, sta, end, opcode, modes):
    if int(opcode) == 1:
        print(modes)
        print(instr[ip])
        i_plus_one_imm = instr[ip+1]
        i_plus_two_imm = instr[ip+2]
        i_plus_one, i_plus_two = (i_plus_one_imm, i_plus_two_imm)

        if modes[0] == '0':
            i_plus_one = instr[int(instr[ip+1])]
        if len(modes) == 2:
            if modes[1] == '0':
                i_plus_two = instr[int(instr[ip+2])]

        res = int(i_plus_one) + int(i_plus_two)
        instr[int(instr[ip+3])] = str(res)

        return instr

    elif int(opcode) == 2:
        i_plus_one_imm = instr[ip+1]
        i_plus_two_imm = instr[ip+2]
        i_plus_one, i_plus_two = (i_plus_one_imm, i_plus_two_imm)

        if modes[0] == '0':
            i_plus_one = instr[int(instr[ip+1])]
        if len(modes) == 2:
            if modes[1] == '0':
                i_plus_two = instr[int(instr[ip+2])]

        res = int(i_plus_one) * int(i_plus_two)
        
        # if modes[2] == 0:
        #     instr[int(instr[ip+3])] = str(res)
        # else:
        #     instr[ip+3] = str(res)
        instr[int(instr[ip+3])] = str(res)

        return instr

    elif int(opcode) == 3:
        instr = store(instr, ip+1)
        return instr

    elif int(opcode) == 4:
        retrieve(instr, ip+1)
        return instr
    else:
        return instr


if __name__ == '__main__':
    with open('intcode_v2.txt') as f:
        intcode = f.read()
    instr = intcode.split(',')
    # instr = [int(n) for n in ic_arr]
    # print(instr)
    ip = 0
    while ip < len(instr):
        code = instr[ip]
        hop = len(code)
        opcode, modes = decode(code)

        if opcode == '99':
            print('END')
            exit()
        # if opcode not in ['1', '2', '3', '4']:
        #     i = i + hop + 1
        #     continue
        else:
            instr = compute(instr, ip, hop, opcode, modes)
            ip += hop + 1

        # print(opcode, modes)


    # opcode, mode = decode('1002')
    # print(opcode, mode)
    # compute_intcode_part1()
    # compute_intcode_part2()
