PATTERN = [0, 1, 0, -1]
STEP_PATTERN = []


def repeat(num, times):
    out = []
    for _ in range(times):
        out.append(num)
    return out


def pattern_genny(step):
    pattern = []
    for p in PATTERN:
        pattern.extend(repeat(p, step))
    return pattern


def calc_step(signal):
    total = 0
    pat_i = 1
    for s in signal:
        if pat_i == len(STEP_PATTERN):
            pat_i = 0
        total += int(s)*STEP_PATTERN[pat_i]
        pat_i += 1
    return total


if __name__ == '__main__':
    input_16 = ''
    with open('input.txt') as f:
        input_16 = f.read()

    signal_i = 0
    output = ''
    for i in range(100):
        while signal_i < len(input_16):
            STEP_PATTERN = pattern_genny(signal_i+1)
            output += str(calc_step(input_16))[-1]
            signal_i += 1
        if i == 99:
            break
        else:
            input_16 = output
            signal_i = 0
            output = ''

    print(output)
