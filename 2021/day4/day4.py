
filename = "/home/looten/workspace/advent_of_code/2021/day4/test_data.txt"
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
        idx = 0

        for line in lines[1:]:
            line = line.replace("\n", "")
            if not line:
                continue

            data = str(line.strip()).split(" ")
            row = {}
            for d in data:
                if str(d):
                    row[int(d)] = ""

            game.append(row)
            if len(game) == 5:
                guess_list.append(game)
                game = []
                idx += 1

    return draw_order, guess_list


def draw_nr(draw_order, guess_list):
    print("Starting to draw")
    winner_cnt = 0
    winners = []
    for draw in draw_order:
        call_draw(draw, guess_list)
        winner_cnt = check_for_winner(draw, guess_list, winner_cnt, winners)


def print_guess(guess_list):
    for i in range(len(guess_list)):
        print(f"Game list {i}")
        for d in guess_list[i]:
            print(f" {d}")


def call_draw(draw, guess_list):
    for game in guess_list:
        for data in game:
            if draw in data:
                data[draw] = 'x'


def check_for_winner(draw, guess_list, winner_cnt, winners):
    for game, i in zip(guess_list, range(len(guess_list))):
        winner = check_game(game)
        if winner:
            if not (i in winners):
                winners.append(i)
                winner_cnt += 1
                if winner_cnt == len(guess_list):
                    print("\nLASTER WINNER")
                    for d in game:
                        print(f" {d}")
                    calc_score(game, draw)
                    exit(0)
                else:
                    # still need to find the rest of the winners
                    pass
            else:
                # player already won
                pass
    return winner_cnt


def calc_score(game, draw):
    tot = 0
    for data in game:
        for k, v in data.items():
            if not v:
                tot += int(k)
    print(f"Final score {tot * int(draw)}")


def check_game(game):
    col_list = ["", "", "", "", ""]
    for data in game:
        row = ""
        for k, i in zip(data, range(5)):
            row += data[k]
            col_list[i] += data[k]
            if len(row) == 5 or len(col_list[i]) == 5:
                return True
    return False


def check_col(game, idx):
    return game[idx] + game[idx] + game[idx] + game[idx] + game[idx]


if __name__ == "__main__":
    draw_order, guess_list = readfile()
    # print_guess(guess_list)
    draw_nr(draw_order, guess_list)
