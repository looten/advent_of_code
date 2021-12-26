
input_file = "/home/looten/workspace/advent_of_code/2021/day6/input.txt"
#input_file = "/home/looten/workspace/advent_of_code/2021/day6/test_data.txt"
import threading

class LanternFish:
    next_lantern = 0

    def __init__(self, new_fish, start_state=6):
        self.next_lantern = start_state
        if new_fish:
            self.next_lantern += 2

    def count_down(self):
        self.next_lantern -= 1

    def check_status(self):
        if self.next_lantern == 0:
            self.next_lantern = 6
            return True
        return False


def create_lanterns(init_state):
    list_lanterns = []
    for start_state in init_state:
        fish = LanternFish(False, start_state)
        list_lanterns.append(fish)
    return list_lanterns


def pass_day(list_lanterns):
    new_list = []
    import time

    start_time = time.time()
    for fish in list_lanterns:
        if fish.check_status():
            new_fish = LanternFish(True)
            new_list.append(new_fish)
            continue
        fish.count_down()

    time2 =  time.time() - start_time
    print(f"time to count {time2}" )
    
    start_time = time.time()
    for fish in new_list:
        list_lanterns.append(fish)

    time2 =  time.time() - start_time
    print(f"time to add {time2}" )

    return list_lanterns


def read_input():
    init_state = []
    with open(input_file) as f:
        lines = f.readlines()
        lines = lines[0].split(",")
        for line in lines:
            init_state.append(int(line))
    return init_state


def print_status(df):
    i, row = df.iterrows()
    print(f"Size {row.size}")


if __name__ == "__main__":
    init_state = read_input()
    days = 80
    print(f"Initial state: {init_state}")
    list_lanterns = create_lanterns(init_state)

    for day in range(1, days+1):
        print(f"After {day}")
        list_lanterns = pass_day(list_lanterns)
        print("Amount of fish",len(list_lanterns), "\n")