pos = dict()
vel = dict()
moon_pos = []
moon_vel = []

def gravitate(moon_pos, moon_vel):
    mp_copy = moon_pos
    mv_copy = moon_vel
    for w, mp1 in enumerate(moon_pos):
        for r, mp2 in enumerate(moon_pos):
            if r != w:
                mp_copy = apply_gravity(mp1, mp2)


def apply_gravity(mp1, mp2):
    for coord in ['x', 'y', 'z']
