import os
import copy
import time
import pandas as pd
from functools import cache

def read_input(filename):
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, filename)
    with open(file_path, "r") as f:
        input_data = []
        for line in f:
            for u in line.split(" "):
                input_data.append(int(u))
    return input_data


def check_mult(d, temp_res, num_zeroes, num_ones, num_mults):
    #print("split")
    q, r = divmod(len(str(d)), 2)
    d_st = str(d)
    first, sec = d_st[:q + r], d_st[q + r:]
    #print("first ", int(first))
    #print("sec ", int(sec))
    if int(first) == 0:
        num_zeroes += 1
    elif int(first) == 1:
        num_ones += 1
    else:
        temp_res.append(int(first))

    if int(sec) == 0:
        num_zeroes += 1
    elif int(sec) == 1:
        num_ones += 1
    else:
        temp_res.append(int(sec))
    
    return temp_res, num_zeroes, num_ones, num_mults

@cache
def count(stone, steps):
    # end of recurs
    print("call for stone ", stone)
    if steps == 0:
        print(" bottom! for stone ", stone)
        return 1

    if stone == 0:
        return count(1, steps-1)

    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length // 2]), steps-1) + count(int(string[length // 2:]), steps-1)

    return count(stone*2024, steps-1)
    

def stone_rule_exec(input_data, blinks):
    print("Initial arrangement:")
    print(input_data)

    blink_results = input_data
    temp_res = []

    num_zeroes = blink_results.count(0)
    num_ones = blink_results.count(1)
    num_mults = blink_results.count(2024)

    blink_results  = [i for i in blink_results if i != 0 or i != 1 or i != 2024]

    start = time.time()
    for blink in range(blinks):
        temp_res = []
        for _ in range(num_mults):
            temp_res, num_zeroes, num_ones, num_mults = check_mult(2024, temp_res, num_zeroes, num_ones, num_mults)
        for d in blink_results:
            d = int(d)
            if d == 0:
                #print("zero")
                num_zeroes += 1
            elif d == 1:
                #print("one")
                num_ones += 1
            elif len(str(d)) % 2 == 0:
                #print("mult")
                temp_res, num_zeroes, num_ones, num_mults = check_mult(d, temp_res, num_zeroes, num_ones, num_mults)
            else:
                #print("mult")
                d *= 2024
                temp_res.append(int(d))
        #print("zeroes ", num_zeroes)

        print(f"After {blink+1} blink/s: {time.time()-start} ")
        blink_results = copy.deepcopy(temp_res)
        #print(blink_results)
        num_ones = num_zeroes
        #print("0 ", num_zeroes)
        #print("1 ", num_ones)
        #print("mult ", num_mults)
        num_mults = num_ones
        num_zeroes = 0

        #input()

        
        
    
    print(blink_results)
    print(len(blink_results) + num_zeroes + num_ones + num_mults)

if __name__ == "__main__":
    filename = "sample_input1.txt"
    blinks = 1

    filename = "sample_input2.txt"
    blinks = 6
#
    filename = "input.txt"
    blinks = 75

    input_data = read_input(filename)
    print(sum(count(stone, blinks) for stone in input_data))
