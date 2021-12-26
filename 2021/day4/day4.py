
filename = "/home/looten/workspace/advent_of_code/2021/day4/input.txt"

def readfile():
    draw_order = []
    guess_list = []
    with open(filename) as f:
        lines = f.readlines()
        draw_order = lines[0].split(",")
        for i in range(len(draw_order)):
            draw_order[i] = int(draw_order[i].strip())

        games_cnt = 0
        game = []
        for line in lines[1:]:
            data = str(line.strip()).split(" ")

            row = {}
            idx = 0

            for d in data:
                if str(d):
                    row[int(d)] =idx
                    idx += 1

            if len(row) > 0:
                game.append(row)
                if len(game) == 5:
                    game.append({"draws": []})
                    guess_list.append(game)
                    game = []
                    

    return draw_order, guess_list

def draw_nr(draw_order, guess_list):
    draws = []
    for draw in draw_order:
        draws.append(draw)
        draws.sort()
        call_draw(draw, guess_list)

        #if len(draws) % 5 == 0:
        print(f"new draw {draws}")

        print_guess(guess_list)
        input("asda")

        check_for_winner(guess_list)

def print_guess(guess_list):
    for data in guess_list:
        print(f"\n")
        for d in data:
            print(f" {d}")
            #print(f"{k} : {v}")

def call_draw(draw, guess_list):
    for game in guess_list:
        for data in game[:4]:
            try:
                col = data[draw]
                game[5]['draws'].append(draw)
            except KeyError:
                pass

def check_for_winner(guess_list):
    for game in guess_list:
        winner = check_game(game)
        if winner:
            for d in game:
                print(f" {d}")
                #print(f"{k} : {v}")
            input("WINNER")
            exit(0)

def check_game(game):
    tmp = []
    #print(game[:5])
    for i in range(len(game[:5])):
        print(i)
        for j in game[5]["draws"]:
            try:
                data = game[i][j]
                #print("check_game ", game[i])
                #print("check for  ", j)
                #print("found at pos ", data)
                calc = (i * 5) + data
                tmp.append(calc)
                #print("at pos: ", calc)
                
                if len(tmp) >= 5:
                    #print("checking for win.. ", tmp)
                    #input("")
                    if check_row_win(tmp): # or check_col_win(tmp):
                        #print("win\n", game)
                        return True
                    
            except KeyError:
                pass

def check_row_win(tmp):
    tmp.sort()
    #print("check rows")
    print("check rows tmp: ", tmp)

    n = len(tmp)
    k = 5

    for i in range(n-k+1):
        current_sum = 0
        prev = -1
        for j in range(k):
            print("prev ", prev)
            print("new - 1: ", tmp[i + j]-1)
            if prev > 0 and tmp[i + j]-1 != prev:
                prev = tmp[i + j]
                current_sum = prev
                continue
            current_sum = current_sum + int(tmp[i + j])
            prev = tmp[i + j]

        #print(f"curr: {current_sum}")
        
        if current_sum >= 10 and (current_sum) % 5 == 0:
            print("ROW WIN", current_sum)
            return True
    
    return False
        
def check_col_win(tmp):
    tmp.sort()
    #print("check cols")
    #print("check cols tmp: ", tmp)

    n = len(tmp)
    k = 5

    
    for i in range(n-k+1):
        current_sum = 0
        prev = -1
        for j in range(k):    
            if prev > 0 and tmp[i + j] == prev + 5:
                current_sum = 0
                break
            current_sum = current_sum + int(tmp[i + j])
            prev = tmp[i + j]

        print(f"curr: {current_sum}")
        
        if current_sum >= 50 and (current_sum - 50) % 5 == 0:
            print("COL WIN")
            return True
    
    return False

if __name__ == "__main__":
    draw_order, guess_list = readfile()
    draw_nr(draw_order, guess_list)
    #print(draw_order)
    #print(guess_list)



