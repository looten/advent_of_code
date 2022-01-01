import copy
filename = "/home/looten/workspace/advent_of_code/2021/day9/test_data.txt"
filename = "/home/looten/workspace/advent_of_code/2021/day9/input.txt"


def read_file():
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            row = []
            line = line.rstrip("\n")
            for digit in line:
                row.append(int(digit))
            data.append(row)
    return data


def calc_adjacent(data: list):
    low_points = []
    # indexes from prev
    curr_dict = {}
    prev_dict = {}
    kept_last = 0
    for i in range(len(data)):
        #print(f"----------ROW {i}---------------")
        prev_low = 10
        for j in range(len(data[i])):
            #print("\nVALUE", data[i][j], "",j)

            # Needed if for the case:
            # 4343 <- first 3 added to prev
            # 9212 <- 1 added, so the first 3 needs to be removed
            try:
                if i-1 >= 0 and data[i][j] < data[i-1][j]:
                    #print(f"REMOVE {prev_value} @ {j} ")
                    prev_dict.pop(j)
            except KeyError:
                pass
         
            if data[i][j] <= prev_low and j+1 != len(data[i]):
                prev_low = data[i][j]
            elif data[i][j] <= prev_low and j+1 == len(data[i]):
                #print(f"last element...")
                if i - 1 >= 0 and data[i - 1][j] < data[i][j]:
                    #print(f"SKIP {data[i][j]} SINCE ABOVE ROW")
                    continue
                elif data[i][j-1] == data[i][j]:
                    #print(f"SKIP prev {data[i][j]} == {data[i][j-1]}")
                    continue
                elif data[i][j-1] < data[i][j]:
                    continue
                else:
                    curr_dict[j] = data[i][j]
            else:
                if i - 1 >= 0 and data[i - 1][j-1] < prev_low:
                    prev_low = data[i][j]
                else:
                    # potential low point
                    # store prev correctly
                    index = j - 1
                    if index-1 >= 0 and data[i][index-1] < prev_low:
                        pass
                    else:
                        curr_dict[index] = prev_low
                        try:
                            prev_value = prev_dict[j]
                            if prev_value > data[i][j]:
                                prev_dict.pop(j)
                        except KeyError:
                            pass

                        try:
                            prev_value = prev_dict[index]
                            if prev_value > data[i][index]:
                                prev_dict.pop(index)
                        except KeyError:
                            pass
                    # reset
                    prev_low = 10

        low_points.append(prev_dict)
        prev_dict = copy.deepcopy(curr_dict)
        curr_dict.clear()

    low_points.append(prev_dict)

    return low_points


def print_low_points(data : list, low_points: list):
    low_points.pop(0)
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    END = '\033[0m'
    sum_list = []
    for i in range(len(data)):
        sum_row = 0
        start = str(i) + ": "
        row = ""
        for j in range(100):
            if j in low_points[i]:
                sum_row +=1
                row += GREEN + BOLD + str(low_points[i][j]) + END
            else:
                row += str(data[i][j])
        print(f"{start:<4}{row:>100}")
        sum_list.append(sum_row)

def calc(low_points: list):
    tot = 0
    for data in low_points:
        #print(data)
        for k, v in data.items():
            tot += v + 1
    print("final sum", tot)



if __name__ == "__main__":
    data = read_file()
    low_points = calc_adjacent(data)
    print_low_points(data, low_points)
    calc(low_points)

