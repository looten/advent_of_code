#input_file = "/home/looten/workspace/advent_of_code/2022/day2/test_input.txt"
input_file = "/home/looten/workspace/advent_of_code/2022/day2/input_data.txt"
win = 6
draw = 3
loss = 0

rock = 1
paper = 2
scissors = 3

def readinput():
    tot_opp = 0
    tot_me = 0
    with open(input_file, "r") as f:
        data = f.readlines()
        print(data)
        for line in data:
            opp, me = line.split(" ")
            opp_score, me_score = calc(opp, me)
            print("give me: ", me_score)    
            tot_opp += opp_score
            tot_me += me_score
    print("me: ", tot_me)

def calc(opp, me):
    # rock
    if "A" in opp:
        # rock 
        if "X" in me:
            return draw + rock, draw + rock
        # paper
        if "Y" in me:
            return loss + rock, win + paper
        # scissors
        if "Z" in me:
            return win + rock, loss + scissors
    # paper
    if "B" in opp:
        # rock 
        if "X" in me:
            return win + paper, loss + rock
        # paper
        if "Y" in me:
            return draw + paper, draw + paper
        # scissors
        if "Z" in me:
            return loss + paper, win + scissors

    # scissors
    if "C" in opp:
        # rock 
        if "X" in me:
            return loss + scissors, win + rock
        # paper
        if "Y" in me:
            return win + scissors, loss + paper
        # scissors
        if "Z" in me:
            return draw + scissors, draw + scissors
        
    print("ERROR: Should not be here: opp", opp)
    print("ERROR: Should not be here: me", me)
    exit(1)

if __name__ == "__main__":
    readinput()
