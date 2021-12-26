
filename= "/home/looten/workspace/advent_of_code/day5/input.txt"

def split_xy(val):
    x, y = val.split(",")
    return int(x.replace(" ","")), int(y.replace(" ",""))

def read_input():
    data_list = []
    x_max = -1
    y_max = -1
    with open(filename) as f:
        lines = f.readlines()    
        for data in lines:
            start,end = data.split("->")
            x_start, y_start = split_xy(start)
            x_end, y_end = split_xy(end)
            x_max = max(x_max,max(x_start, x_end))
            y_max = max(y_max,max(y_start, y_end))
            if x_start == x_end or y_start == y_end:
                #print(f"{x_start},{y_start}")
                #print(f"{x_end},{y_end}")
                data_list.append({"start" : {"x": x_start, "y": y_start}, "stop":{"x":x_end, "y":y_end}})
    print(f"xm {x_max}")
    print(f"ym {y_max}")
    return data_list
        
def draw(data_list):
    #res = [1000][1000]
    #res = []
    
    res = [[0 for i in range(1000)] for j in range(1000)]
    #print(res)
    for pos in data_list:
        if pos['start']['x'] == pos['stop']['x']:
            start = min(pos['start']['y'], pos['stop']['y'])
            stop = max(pos['start']['y'], pos['stop']['y'])
            for i in range(start, stop): 
                #res[pos['start']['x']][i] += 1
                res[pos['start']['x']][i] += 1
        elif pos['start']['y'] == pos['stop']['y']:
            start = min(pos['start']['x'], pos['stop']['x'])
            stop = max(pos['start']['x'], pos['stop']['x'])
            print("start", start)
            print("stop", stop)
            for i in range(start, stop):
                #print(res[731][828])
                res[i][pos['start']['y']] += 1
        else:
            print("what?")
            exit(1)
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
    print(data_list)
    res = draw(data_list)
    count(res)
if __name__ == "__main__":
    main()
