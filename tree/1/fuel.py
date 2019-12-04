def fuel_req(mass):
    return (mass//3) - 2


def total_fuel_part1():
    total_fuel = 0
    with open('mass.txt') as f:
        for mass in f:
            total_fuel += fuel_req(int(mass))
    print(f"PART 1: {total_fuel}")
    return total_fuel


def total_fuel_part2():
    total_fuel = 0
    with open('mass.txt') as f:
        for mass in f:
            fuel_for_rocket = fuel_req(int(mass))
            total_fuel += fuel_req(int(mass))
            while fuel_for_rocket > 0:
                fuel_for_rocket = fuel_req(fuel_for_rocket)
                if fuel_for_rocket > 0:
                    total_fuel += fuel_for_rocket
    print(f"PART 2: {total_fuel}")


if __name__ == '__main__':
    tf = total_fuel_part1()
    total_fuel_part2()
