
input_file = "/home/looten/workspace/advent_of_code/2021/day7/input.txt"

import math

def read_input():
    data = []
    with open(input_file) as f:
        lines = f.readlines()
        
        for line in lines:
            split_data = line.split(",")
            for d in split_data:
                data.append(int(d))
    data.sort()
    return data


def calc_cheapest(data, move):
    dists = []
    for fuel in data:
        dists.append(abs(fuel - move))
    return dists

def print_moves(data, dists):
    sum_val = 0
    for dist, first in zip(dists, data):
        sum_val += sum(list(range(1,dist+1)))
    return sum_val

if __name__ == "__main__":
    data = read_input()
    max_fuel = max(data)
    start_point = math.ceil(max_fuel/2)
    min_sum = 900000000
    print(f"max_fuel {max_fuel}")
    print(f"first {start_point}")
    input()
    while True:
        
        dists = calc_cheapest(data, start_point)
        curr_sum = print_moves(data, dists)
        
        below = start_point-1
        dists_below = calc_cheapest(data, below)
        below_sum = print_moves(data, dists_below)

        above = start_point+1
        dists_above = calc_cheapest(data, start_point+1)
        above_sum = print_moves(data, dists_above)

        if curr_sum < min_sum:
            min_sum = curr_sum
        
        if min_sum > below_sum:
            start_point = below
            print(f"down to {start_point}")
            continue
        elif min_sum > above_sum:
            start_point = above
            print(f"up to {start_point}")
            continue
        else:
            print(f"Tot fuel: {curr_sum} for {start_point}")
            break


