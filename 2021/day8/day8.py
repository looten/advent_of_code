
filename = "/home/looten/workspace/advent_of_code/2021/day8/test_data2.txt"
filename = "/home/looten/workspace/advent_of_code/2021/day8/input.txt"
SEVEN_DIGIT_MAPPING = {"zero": "abcefg",
                       "one": "cf",
                       "two": "acdeg",
                       "three": "acdfg",
                       "four": "bcdf",
                       "five": "abdfg",
                       "six": "abdefg",
                       "seven": "acf",
                       "eight": "abcdefg",
                       "nine": "abcdfg"}


def read_input():
    input_data = []
    output_data = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            test = line.split("|")
            tmp0 = test[0].split(" ")
            tmp1 = test[1].split(" ")
            tmp0 = [val for val in tmp0 if val]
            tmp1 = [val for val in tmp1 if val]
            input_data.append(tmp0)
            output_data.append(tmp1)
    return input_data, output_data


def decode(input_data: list, output_data: list):
    mapping = {"1": {"one": SEVEN_DIGIT_MAPPING["one"], "cnt": 0},
               "4": {"four": SEVEN_DIGIT_MAPPING["four"], "cnt": 0},
               "7": {"seven": SEVEN_DIGIT_MAPPING["seven"], "cnt": 0},
               "8": {"eight": SEVEN_DIGIT_MAPPING["eight"], "cnt": 0}}
    row = 0
    cnt_curr = 0
    for input_d, output_d in zip(input_data, output_data):
        
        row += 1
        #print(f"Row: {row}")
        for o in output_d:
            o = "".join(sorted(o))
            if len(o) != 2 and len(o) != 4 and len(o) != 3 and len(o) != 7:
                continue

            for i in input_d:
                i = "".join(sorted(i))

                if o == i:
                   # print("output", o)
                    #print("input", i)
                    if len(i) == 2:
                        cnt_curr += 1
                        mapping["1"]["cnt"] += 1
                    elif len(i) == 4:
                        cnt_curr += 1
                        mapping["4"]["cnt"] += 1
                    elif len(i) == 3:
                        cnt_curr += 1
                        mapping["7"]["cnt"] += 1
                    elif len(i) == 7:
                        cnt_curr += 1
                        mapping["8"]["cnt"] += 1
        #if cnt_curr > 0:
            #print(f"ror cnt {cnt_curr}\n")

    tot = mapping["1"]["cnt"] +  mapping["4"]["cnt"] + mapping["7"]["cnt"] + mapping["8"]["cnt"]

    #print(mapping)

    print(f"Instances: {tot}")


if __name__ == "__main__":
    input_data, output_data = read_input()
    decode(input_data, output_data)
