
filename = "/home/looten/workspace/advent_of_code/2021/day2/input.txt"
def readfile():
    array = []
    with open(filename) as f:
        lines = f.readlines()
        

        for line in lines:
            command, value = line.split(" ")
            array.append({command : int(value)})
    return array
    
def navigate(instructions):
    keys = ["forward", "down", "up"]
    hor_pos = 0
    depth = 0
    aim = 0
    for data in instructions:
        #print(data)

        for k in keys:
            try:
                value = data[k]

                if k == "forward":
                    hor_pos += value
                    #if not (depth == 0 and aim > 0):
                    depth += value * aim
                    depth = max(0, depth)
                elif k == "down":
                    aim += value
                elif k == "up":
                    aim -= value
                else:
                    print(f"Unknown cmd {k}")
                    exit(1)

            except KeyError:
                continue

    print(f"Hor pos {hor_pos}")
    print(f"Depth {depth}")
    answer = hor_pos * depth
    print(f"Answer {answer}")



if __name__ == "__main__":
    instructions = readfile()
    #print(instructions)
    navigate(instructions)