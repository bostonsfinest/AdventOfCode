import sys
# from matplotlib import pyplot as plt

central_port = (0, 0)

def right(p):
    return (p[0]+1, p[1])

def left(p):
    return (p[0]-1, p[1])

def up(p):
    return (p[0], p[1]+1)

def down(p):
    return (p[0], p[1]-1)

def get_move(d):
    if d is 'R':
        return right
    if d is 'L':
        return left
    if d is 'U':
        return up
    if d is 'D':
        return down

def is_intersection(p1, p2):
    if p1 == p2:
        return True
    else:
        return False

def manhattan_dist(p):
    return abs(p[0]) + abs(p[1])


def day3_winner(file='moves.txt'):
    with open(file) as f:
        red = f.readline().strip()
        blue = f.readline().strip()

    red_path = red.split(',')
    blue_path = blue.split(',')
    red_points = [central_port]
    blue_points = [central_port]

    i = 1
    for move in red_path:
        direction = move[0]
        move_func = get_move(direction)
        steps = int(move[1:])
        for _ in range(steps):
            next_point = move_func(red_points[i-1])
            red_points.append(next_point)
            i += 1
    
    j = 1
    for move in blue_path:
        direction = move[0]
        move_func = get_move(direction)
        steps = int(move[1:])
        for _ in range(steps):
            next_point = move_func(blue_points[j-1])
            blue_points.append(next_point)
            j += 1

    md = sys.maxsize
    common_points = list(set(red_points).intersection(blue_points))
    
    for p in common_points:
        tmp_md = manhattan_dist(p)
        if tmp_md < md and tmp_md != 0:
            md = tmp_md

    print(md)

    # PART2
    print("PART2")
    red_steps = []
    blue_steps = []
    rsteps = 0
    bsteps = 0
    common_points.remove((0, 0))
    for cp in common_points:
        for rp in red_points[1:]:
            rsteps += 1
            if rp == cp:
                red_steps.append(rsteps)
                rsteps = 0
                break
        
        for bp in blue_points[1:]:
            bsteps += 1
            if bp == cp:
                blue_steps.append(bsteps)
                bsteps = 0
                break


    wire_lengths = []
    for i in range(len(red_steps)):
        wire_lengths.append(red_steps[i]+blue_steps[i])

    print(min(wire_lengths))

    # x1 = [x[0] for x in red_points]
    # y1 = [x[1] for x in red_points]
    # x2 = [x[0] for x in blue_points]
    # y2 = [x[1] for x in blue_points]

    # plt.plot(x1, y1)
    # plt.plot(x2, y2)
    # plt.show()
        
if __name__ == '__main__':
    day3_winner('moves.txt')


            

