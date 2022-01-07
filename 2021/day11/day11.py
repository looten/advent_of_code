
input_file = "/home/looten/workspace/advent_of_code/2021/day11/test_data.txt"


def read_input():
    data = []
    with open(input_file) as f:
        lines = f.readlines()
        # print(lines)
        for line in lines:
            line = line.replace("\n", "")
            row = []
            for d in line:
                row.append(int(d))
            data.append(row)
    return data


def run_steps(steps: int, data: list):
    for step in range(steps):
        data = calc_flash(data)
        data = check_data(data)
        print(f"After step {step+1}:")
        print_data(data)


def print_data(data: list):
    for row in data:
        tmp = [str(i) for i in row]
        print(''.join(tmp))
    print(f"")


def calc_flash(data: list):
    return [[d + 1 for d in row] for row in data]


def flash_eval(data: list, row: int, col: int):
    # North west
    if row == 0 and col == 0:
        data[row][col+1] += 1
        data[row+1][col+1] += 1
        data[row+1][col] += 1

    # North east
    if row == 0 and col == len(data[0])-1:
        data[row+1][col] += 1
        data[row+1][col-1] += 1
        data[row][col-1] += 1

    # South east
    if row == len(data)-1 and col == len(data[0])-1:
        data[row-1][col] += 1
        data[row][col-1] += 1
        data[row-1][col-1] += 1

    # South west
    if row == len(data)-1 and col == 0:
        data[row-1][col] += 1
        data[row-1][col+1] += 1
        data[row][col+1] += 1

    # Top row
    if row == 0 and (col > 0 or col < len(data[0])-1):
        data[row][col+1] += 1
        data[row+1][col+1] += 1
        data[row+1][col] += 1
        data[row+1][col-1] += 1
        data[row][col-1] += 1

    # Bottom row
    if row == len(data)-1 and (col > 0 or col < len(data[0])-1):
        data[row-1][col] += 1
        data[row-1][col+1] += 1
        data[row][col+1] += 1
        data[row][col-1] += 1
        data[row-1][col-1] += 1

    # First col
    if (row > 0 or row < len(data)-1) and col == 0:
        data[row-1][col] += 1
        data[row-1][col+1] += 1
        data[row][col+1] += 1
        data[row+1][col+1] += 1
        data[row+1][col] += 1

    # Last col
    if (row > 0 or row < len(data)-1) and col == len(data[0])-1:
        data[row-1][col] += 1
        data[row+1][col] += 1
        data[row+1][col-1] += 1
        data[row][col-1] += 1
        data[row-1][col-1] += 1

    # The rest
    if (row > 0 or row < len(data)-1) and (col > 0 or col < len(data[0])-1):
        data[row-1][col] += 1
        data[row-1][col+1] += 1
        data[row][col+1] += 1
        data[row+1][col+1] += 1
        data[row+1][col] += 1
        data[row+1][col-1] += 1
        data[row][col-1] += 1
        data[row-1][col-1] += 1


def check_data(data: list):
    for row, d in enumerate(data):
        for col, val in enumerate(d):
            print("val ", val)
            #print("col", col)
            if val > 9:
                data[row][col] = 0
                flash_eval(data, row, col)

    return data


if __name__ == "__main__":
    data = read_input()
    print(f"Before any steps:")
    print_data(data)
    run_steps(2, data)
