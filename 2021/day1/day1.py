import os

filename = "/home/looten/workspace/advent_of_code/2021/day1_input.txt"

def readfile():
    prev_val = -1
    cnt = 0

    with open(filename) as f:
        lines = f.readlines()
        array = []

        for i in lines:
            if type(i):
                array.append(i)

        n = len(array)
        k = 3

        for i in range(n-k+1):
            current_sum = 0

            for j in range(k):
                current_sum = current_sum + int(array[i + j])

            if prev_val == -1:
                prev_val = current_sum
                continue

            if current_sum > prev_val:
                cnt = cnt + 1

            prev_val = current_sum

    print(cnt)

if __name__ == "__main__":
    readfile()
