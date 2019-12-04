import numpy as np

LBOUND = '138241'
UBOUND = '674034'

def has_adj_digits(p):
    for i in range(0, len(p)-1):
        if p[i] == p[i+1]:
            return True
    return False


def has_incr_digits(p):
    for i in range(0, len(p)-1):
        if int(p[i]) > int(p[i+1]):
            return False
    return True


def bolt_cutter():
    possible_pwds = []
    for pw in range(int(LBOUND), int(UBOUND)+1):
        possible_pwds.append(pw)
    narrowed_pwds = []
    for pw in possible_pwds:
        if has_adj_digits(str(pw)) and has_incr_digits(str(pw)):
            narrowed_pwds.append(pw)

    # print(narrowed_pwds)
    print(f"PART 1: {len(narrowed_pwds)}")

    final_pwds = []
    for pw in narrowed_pwds:
        p_arr = []
        for n in str(pw):
            p_arr.append(int(n))
        unique = np.unique(p_arr)
        counts = []
        for u in unique:
            counts.append(p_arr.count(u))
        if 2 in counts:
            final_pwds.append(pw)    

    # print(final_pwds)
    print(f"PART 2: {len(final_pwds)}")

if __name__ == '__main__':
    bolt_cutter()
