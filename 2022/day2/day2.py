#input_file = "/home/looten/workspace/advent_of_code/2022/day2/test_input.txt"
input_file = "/home/looten/workspace/advent_of_code/2022/day2/input_data.txt"
win = 6
draw = 3
loss = 0

rock = 1
paper = 2
scissors = 3

def readinput():
    tot_me = 0
    with open(input_file, "r") as f:
        data = f.readlines()
        #print(data)
        for line in data:
            opp, me = line.split(" ")
            me_score = calc(opp, me)
            #print("give me: ", me_score)    
            tot_me += me_score
    print("me: ", tot_me)

def calc(opp, me):
    # rock
    if "A" in opp:
        # need to lose 
        if "X" in me:
            return loss + scissors
        # need to draw
        if "Y" in me:
            return draw + rock
        # need to win
        if "Z" in me:
            return win + paper
    # paper
    if "B" in opp:
        # need to lose 
        if "X" in me:
            return loss + rock
        # need to draw
        if "Y" in me:
            return draw + paper
        # need to win
        if "Z" in me:
            return win + scissors

    # scissors
    if "C" in opp:
        # need to lose 
        if "X" in me:
            return loss + paper
        # need to draw
        if "Y" in me:
            return draw + scissors
        # need to win
        if "Z" in me:
            return win + rock
        
    print("ERROR: Should not be here: opp", opp)
    print("ERROR: Should not be here: me", me)
    exit(1)

if __name__ == "__main__":
    readinput()
