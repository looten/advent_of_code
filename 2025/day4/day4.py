import os
import copy

def read_input(filename):
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, filename)
    with open(file_path, "r") as f:
        data = []
        for line in f:
            s = []
            line = line.replace("\n", "")
            for c in line:
                s.append(c)
            data.append(s)
    return data

def direction_to_string(direction):
    dir_map = {
        (0, 1): "S",
        (1, 1): "NE",
        (1, 0): "E",
        (1, -1): "SE",
        (0, -1): "N",
        (-1, -1): "SW",
        (-1, 0): "W",
        (-1, 1): "NW",
    }
    return dir_map.get(direction, "UNKNOWN")
def decode(data):
    directions = [
        (0, 1),     # N
        (1, 1),     # NE
        (1, 0),     # E
        (1, -1),    # SE
        (0, -1),    # S
        (-1, -1),   # SW
        (-1, 0),    # W
        (-1, 1),    # NW
        ]
    answer = 0
    sub_ans = 0
    found = True
    while found:
        res_map = copy.deepcopy(data)
        sub_ans = 0

        for row_idx, row in enumerate(data):
           # print(row)
            for col_idx, col in enumerate(row):
                if col == "@":
                    #print(f"start search ({row_idx,col_idx}) at:", )
                    #start_idx = (row_idx, col_idx)
                    num_sur_paper_rolls = 0
                    for direction in directions:
                        x, y = direction
                        in_bounds = row_idx + y >= 0 and row_idx + y < len(data) and col_idx + x >= 0 and col_idx + x < len(row)
                        if in_bounds and data[row_idx + y][col_idx + x] == "@":
                            num_sur_paper_rolls += 1
                          #  print(f"found in direction:({direction}) cords = ({row_idx + y, col_idx + x})")
                #print(f"Num surrounding paper rolls: {num_sur_paper_rolls}")
                    if num_sur_paper_rolls < 4:
                       # print(f"OK, only {num_sur_paper_rolls} surrounding")
                        res_map[row_idx][col_idx] = "x"
                        answer += 1
                        sub_ans += 1
                    #else:
                       # print(f"Too many surrounding ({num_sur_paper_rolls})")
                    #input()
        if sub_ans == 0:
            found = False
        else:
            data = copy.deepcopy(res_map)
           # print(f"Remove {sub_ans} paper rolls:")
            #for row in res_map:
            #    print("".join(row))
            #input()

    print(f"Answer: {answer}")


if __name__ == "__main__":
    filename = "sample_input.txt"
    filename = "input.txt"
    data = read_input(filename)
    decode(data)