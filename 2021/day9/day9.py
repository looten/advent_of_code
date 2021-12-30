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
        #print(data[i])
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
                    if i == 5:
                        print("i", i)
                        print("j", j)
                        print("prev_low ", prev_low)
                        print("data[i][j-1] ", data[i][j-1])
                        print("data[i][j] ", data[i][j])
                        print("HASSE", curr_dict)
                        input()
                        continue
                else:
                    #print(f"Add last {data[i][j]} @ {j}")
                    curr_dict[j] = data[i][j]
            #elif j - 1 >= 0 and data[i][j] > data[i][j-1]:
            #    print(f"SKIP {data[i][j]} SINCE PREV")
            else:
                #print("check...")
                
                #if i - 1 >= 0:
                   # print("above row", data[i - 1])
                    #print("i - 1", i - 1)
                    #print("above", data[i - 1][j-1])
                #print("prev", prev_low)
                if i - 1 >= 0 and data[i - 1][j-1] < prev_low:
                    if i == 5:
                        print("i", i)
                        print("j", j)
                        print("got here0", curr_dict)
                        input()
                    #print(f"SKIP {prev_low} SINCE ABOVE ROW")
                    prev_low = data[i][j]
                else:
                    # potential low point
                    # store prev correctly
                    if i == 5:
                        print("i", i)
                        print("j", j)
                        print("prev_low ", prev_low)
                        print("got here1", curr_dict)
                        input()
                    index = j - 1
                    #print(f"checking val before {data[i][index-1]} < {prev_low} ?")
                    if index-1 >= 0 and data[i][index-1] < prev_low:
                        #print(f"SKIP SINCE PREV {data[i][index-1]} < {prev_low} ")
                        pass
                    else:
                        curr_dict[index] = prev_low
                        #print(f"ADDED {curr_dict[index]} @ {index} ")
                        try:
                            #print("check prev.. ")
                            #print("prev_dict", prev_dict)
                            #print("index", j)
                            prev_value = prev_dict[j]
                            #print("prev_value", prev_value)
                            if prev_value > data[i][j]:
                             #   print(f"REMOVE {prev_value} @ {j} ")
                                prev_dict.pop(j)
                        except KeyError:
                            pass

                        try:
                            #print("check vs prev.. ")
                            #print("prev_dict", prev_dict)
                            #print("index", index)
                            prev_value = prev_dict[index]
                            #print("prev_value", prev_value)
                            if prev_value > data[i][index]:
                                #print(f"REMOVE {prev_value} @ {j} ")
                                prev_dict.pop(index)
                        except KeyError:
                            pass
                    # reset
                    prev_low = 10
                    
        #if len(prev_dict) > 0:
         #   print(f"prev dict is not empty, ADD", prev_dict)
        #prev_index = i - 1
       #kept_last = prev_index
        if i == 5:
            print("i", i)
            print("got here", curr_dict)
            input()

        low_points.append(prev_dict)

        prev_dict = copy.deepcopy(curr_dict)
        #print("\nPREV", prev_dict)
        #print_low_points(data, low_points)    
        #input("")
        #prev_dict = curr_dict
        #print("\n")
        curr_dict.clear()
    
    #if len(prev_dict) > 0:
     #   print(f"last, ADD", prev_dict)
    low_points.append(prev_dict)

    
    return low_points


def print_low_points(data : list, low_points: list):
    low_points.pop(0)

    #print(data)
    #print("low points:", low_points)
    #print("len:", len(low_points))
    #print("data len:", len(data))
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    END = '\033[0m'
    #row = ""
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
        #print(row)
        print(f"{start:<4}{row:>100}")
        sum_list.append(sum_row)
        #row = ""
    #for i in sum_list:
     #   print(i)

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

