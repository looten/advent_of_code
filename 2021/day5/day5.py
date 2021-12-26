
#filename= "/home/looten/workspace/advent_of_code/day5/input.txt"
filename = "/home/looten/workspace/advent_of_code/2021/day5/input.txt"
#filename = "/home/looten/workspace/advent_of_code/2021/day5/test_data.txt"


def split_xy(val):
    x, y = val.split(",")
    return int(x.replace(" ", "")), int(y.replace(" ", ""))


def read_input():
    data_list = []
    x_max = -1
    y_max = -1
    with open(filename) as f:
        lines = f.readlines()
        for data in lines:
            start, end = data.split("->")
            x_start, y_start = split_xy(start)
            x_end, y_end = split_xy(end)
            x_max = max(x_max, max(x_start, x_end))
            y_max = max(y_max, max(y_start, y_end))
            data_list.append(
                {"start": {"x": x_start, "y": y_start}, "stop": {"x": x_end, "y": y_end}})
    print(f"xm {x_max}")
    print(f"ym {y_max}")
    return data_list


def print_data(data_list):
    data = ""
    for x in range(10):
        for y in range(10):
            if data_list[y][x] == 0:
                data += "."
            else:
                data += str(data_list[y][x])
        print(data)
        data = ""


def get_min_max(val1, val2):
    return min(val1, val2), max(val1, val2)


def determine_range(start, stop):
    if start < stop:
        return range(start, stop + 1)
    else:
        return range(start, stop-1, -1)


def draw(data_list):
    res = [[0 for i in range(1000)] for j in range(1000)]
    for pos in data_list:
        if pos['start']['x'] == pos['stop']['x']:
            start, stop = get_min_max(pos['start']['y'], pos['stop']['y'])
            for i in range(start, stop + 1):
                res[pos['start']['x']][i] += 1
        elif pos['start']['y'] == pos['stop']['y']:
            start, stop = get_min_max(pos['start']['x'], pos['stop']['x'])
            for i in range(start, stop + 1):
                res[i][pos['start']['y']] += 1
        else:
            start_x = pos['start']['x']
            stop_x = pos['stop']['x']
            range1 = determine_range(start_x, stop_x)
            start_y = pos['start']['y']
            stop_y = pos['stop']['y']
            range2 = determine_range(start_y, stop_y)

            for x, y in zip(range1, range2):
                res[x][y] += 1
    return res


def count(res):
    count = 0
    for x in range(1000):
        for y in range(1000):
            if res[x][y] >= 2:
                count += 1
    print("nr of 2 cross: ", count)


def main():
    data_list = read_input()
    res = draw(data_list)
    # print_data(res)
    count(res)


if __name__ == "__main__":
    main()
