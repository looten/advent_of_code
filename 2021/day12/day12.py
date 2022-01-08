
filename = "/home/looten/workspace/advent_of_code/2021/day12/test_data.txt"
filename = "/home/looten/workspace/advent_of_code/2021/day12/test_data2.txt"
filename = "/home/looten/workspace/advent_of_code/2021/day12/input.txt"


def readinput() -> dict:
    nodes = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            a, b = line.split("-")
            if a in nodes:
                nodes[a].append(b)
            else:
                nodes[a] = [b]
            if b in nodes:
                nodes[b].append(a)
            else:
                nodes[b] = [a]
    return nodes


def create_paths(nodes: dict):
    paths = []
    print("nodes", nodes)
    for start_neighbor in nodes["start"]:
        path = ["start", start_neighbor]
        path_search(nodes, path, paths)
    return paths


def print_paths(paths: list):
    print("length", len(paths))
    #for i in range(len(paths)):
        #print(f"{i+1} {paths[i]}")
        #print(f"{paths[i]}")


def path_search(nodes: dict, path: list, paths: list):
    curr_node = path[-1]
    neighbours = nodes[curr_node]
    for neighbour in neighbours:
        if neighbour == "start":
            continue

        if not "start" in path:
            return

        #print("\ncurr", curr_node)
        #print("path", path)
        #print("neighbour", neighbour)
        #print("neighbours", neighbours)

        # found path
        if "start" in path and "end" in path:
            path_str = ','.join(path)

            if not path_str in paths:
                paths.append(path_str)
                #print(f"  {len(paths)} FOUND PATH {path_str}" )
                del path[-1:]
                #print(f"  restart from {path}" )
                return

        # skip mutiple small caves
        #if neighbour in path and (len(neighbour) == 2 and neighbour.islower()):
        if neighbour in path and (len(neighbour) == 2 and neighbour.islower()):
            #print(f"  no good, continue" )
            continue
        elif curr_node in nodes[neighbour] and not "end" in path:
            #print("  go down to ", neighbour)
            #print("  curr_node", curr_node)
            #print("  nodes[neighbour]", nodes[neighbour])
            path.append(neighbour)
            path_search(nodes, path, paths)
        else:
            #print(f"  we are stuck" )
            del path[-2:]
            #print(f"  retart from{path}" )
            return
    del path[-1:]
    #print("going back ...")


if __name__ == "__main__":
    nodes = readinput()
    paths = create_paths(nodes)
    print_paths(paths)
