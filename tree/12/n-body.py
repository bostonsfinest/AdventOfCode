import re
import numpy as np


class nBody:
    moon_pos = []
    moon_vel = []

    def __init__(self):
        with open('input.txt') as f:
            line = f.readline()
            while line:
                pos = [int(d) for d in re.findall(r'-?\d+', line)]
                vel = [0, 0, 0]
                self.moon_pos.append(pos)
                self.moon_vel.append(vel)
                line = f.readline()

    def gravitate(self):
        for w, mp1 in enumerate(self.moon_pos):
            for r, mp2 in enumerate(self.moon_pos):
                if r != w:
                    self.apply_gravity(w, mp1, mp2)
        self.update_positions()

    def apply_gravity(self, i, mp1, mp2):
        for j in range(len(mp1)):
            if mp1[j] < mp2[j]:
                self.moon_vel[i][j] += 1
            if mp1[j] > mp2[j]:
                self.moon_vel[i][j] -= 1

    def update_positions(self):
        for i in range(len(self.moon_pos)):
            self.moon_pos[i][0] += self.moon_vel[i][0]
            self.moon_pos[i][1] += self.moon_vel[i][1]
            self.moon_pos[i][2] += self.moon_vel[i][2]

    def total_energy(self):
        total_energy = 0
        for i in range(len(self.moon_pos)):
            total_energy += np.sum(np.abs(self.moon_pos[i])) * \
                np.sum(np.abs(self.moon_vel[i]))
        return total_energy

    def reset(self):
        self.moon_pos = []
        self.moon_vel = []
        self.__init__()

    def part1(self):
        for _ in range(1000):
            self.gravitate()
        print(self.total_energy())
        self.reset()

    def part2(self):
        pass


if __name__ == '__main__':
    nb = nBody()
    nb.part1()
    nb.part2()
