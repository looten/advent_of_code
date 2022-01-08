
input_file = "/home/looten/workspace/advent_of_code/2021/day11/test_data.txt"
input_file = "/home/looten/workspace/advent_of_code/2021/day11/test_data2.txt"
input_file = "/home/looten/workspace/advent_of_code/2021/day11/input.txt"


def read_input():
    data = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            row = []
            for d in line:
                row.append(int(d))
            data.append(row)
    return data


def run_steps(steps: int, data: list):
    flashes = 0
    for step in range(steps):
        data = calc_flash(data)
        data = check_data(data)
        data = check_again(data)
        print(f"After step {step+1}:")
        flashes = print_data(data, flashes)
    print(f"Flashes: {flashes}")


def print_data(data: list, flashes: int):
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    END = '\033[0m'

    curr_flashes = 0
    for row in data:
        #tmp = [BOLD + GREEN + str(i)+ END if i == 0 else str(i) for i in row]
        tmp = [str(i) for i in row]
        curr_flashes += tmp.count('0')
        print(''.join(tmp))
    print(f"")

    flashes += curr_flashes

    if curr_flashes == len(data) * len(data[0]):
        print("ALL FLASH", curr_flashes)
        input()

    return flashes


def calc_flash(data: list):
    return [[d + 1 for d in row] for row in data]


def calc(data: list, row: int, col: int):
    if row < 0 or col < 0:
        print("hmm")
        exit()
    if data[row][col] != 0:
        data[row][col] += 1
    if data[row][col] > 9:
        data[row][col] = 0
        flash_eval(data, row, col)


def flash_eval(data: list, row: int, col: int):
    # North west
    if row == 0 and col == 0:
        calc(data, row, col+1)
        calc(data, row+1, col+1)
        calc(data, row+1, col)

    # North east
    if row == 0 and col == len(data[0])-1:
        calc(data, row+1, col)
        calc(data, row+1, col-1)
        calc(data, row, col-1)

    # South east
    if row == len(data)-1 and col == len(data[0])-1:
        calc(data, row-1, col)
        calc(data, row, col-1)
        calc(data, row-1, col-1)

    # South west
    if row == len(data)-1 and col == 0:
        calc(data, row-1, col)
        calc(data, row-1, col+1)
        calc(data, row, col+1)

    # Top row
    if row == 0 and (col > 0 and col < len(data[0])-1):
        calc(data, row, col+1)
        calc(data, row+1, col+1)
        calc(data, row+1, col)
        calc(data, row+1, col-1)
        calc(data, row, col-1)

    # Bottom row
    if row == len(data)-1 and (col > 0 and col < len(data[0])-1):
        calc(data, row-1, col)
        calc(data, row-1, col+1)
        calc(data, row, col+1)
        calc(data, row, col-1)
        calc(data, row-1, col-1)

    # First col
    if (row > 0 and row < len(data)-1) and col == 0:
        calc(data, row-1, col)
        calc(data, row-1, col+1)
        calc(data, row, col+1)
        calc(data, row+1, col+1)
        calc(data, row+1, col)

    # Last col
    if (row > 0 and row < len(data)-1) and col == len(data[0])-1:
        calc(data, row-1, col)
        calc(data, row+1, col)
        calc(data, row+1, col-1)
        calc(data, row, col-1)
        calc(data, row-1, col-1)

    # The rest
    if (row > 0 and row < len(data)-1) and (col > 0 and col < len(data[0])-1):
        calc(data, row-1, col)
        calc(data, row-1, col+1)
        calc(data, row, col+1)
        calc(data, row+1, col+1)
        calc(data, row+1, col)
        calc(data, row+1, col-1)
        calc(data, row, col-1)
        calc(data, row-1, col-1)


def check_data(data: list):
    for row, d in enumerate(data):
        for col, val in enumerate(d):
            if val > 9:
                data[row][col] = 0
                flash_eval(data, row, col)
    return data


def check_again(data: list):
    for row, d in enumerate(data):
        for col, val in enumerate(d):
            if val > 9:
                data[row][col] = 0
    return data


if __name__ == "__main__":
    data = read_input()
    print(f"Before any steps:")
    print_data(data, 0)
    run_steps(1000, data)
