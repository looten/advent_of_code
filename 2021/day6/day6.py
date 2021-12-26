

input_file = "/home/looten/workspace/advent_of_code/2021/day6/input.txt"
#input_file = "/home/looten/workspace/advent_of_code/2021/day6/test_data.txt"


def create_lanterns(init_state):
    list_lanterns = []
    for i in range(9):
        list_lanterns.append({i: init_state.count(i)})
    return list_lanterns


def pass_day(list_lanterns):
    prev = list_lanterns[0][0]
    tmp = -1
    for i in range(8, 0, -1):
        if tmp == -1:
            tmp = list_lanterns[i-1][i-1]
            list_lanterns[i-1][i-1] = list_lanterns[i][i]
            list_lanterns[i][i] = 0
        else:
            bckp = tmp
            tmp = list_lanterns[i-1][i-1]
            list_lanterns[i-1][i-1] = bckp

    if prev > 0:
        list_lanterns[8][8] += prev
        list_lanterns[6][6] += prev

    return list_lanterns


def read_input():
    init_state = []
    with open(input_file) as f:
        lines = f.readlines()
        lines = lines[0].split(",")
        for line in lines:
            init_state.append(int(line))
    return init_state


def print_status(list_lanterns):
    tmp = 0
    for i in range(0, 9):
        tmp += list_lanterns[i][i]
    print("Amount of fish", tmp, "\n")


if __name__ == "__main__":
    init_state = read_input()
    days = 256
    list_lanterns = create_lanterns(init_state)
    print(list_lanterns)
    for day in range(1, days+1):
        list_lanterns = pass_day(list_lanterns)
        print(f"After Day {day}")
        print_status(list_lanterns)
