X_RBOUND = 4
X_LBOUND = 0
Y_RBOUND = 4
Y_LBOUND = 0
directions = 4


def get_neighbors(point, bdict):
    neighbors = 0
    up = (point[0], point[1]-1)
    down = (point[0], point[1]+1)
    right = (point[0]+1, point[1])
    left = (point[0]-1, point[1])
    adj_points = [up, down, left, right]

    for ap in adj_points:
        if (ap[0] >= X_LBOUND and ap[0] <= X_RBOUND) and (ap[1] >= Y_LBOUND and ap[1] <= Y_RBOUND):
            if bdict[ap] == '#':
                neighbors += 1

    return neighbors


if __name__ == '__main__':
    input_24 = ''
    with open('input.txt') as f:
        input_24 = f.read()
    rows = input_24.split('\n')
    print(rows)
    bug_dict = {}

    x = 0
    for r in rows:
        for y in range(Y_RBOUND+1):
            bug_dict[(x, y)] = r[y]
        x += 1

    print(bug_dict)

    print(get_neighbors((3, 3), bug_dict))
