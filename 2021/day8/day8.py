
#filename = "/home/looten/workspace/advent_of_code/2021/day8/test_data2.txt"
filename = "/home/looten/workspace/advent_of_code/2021/day8/input.txt"
SEVEN_DIGIT_MAPPING = {"zero": "0",
                       "one": "1",
                       "two": "2",
                       "three": "3",
                       "four": "4",
                       "five": "5",
                       "six": "6",
                       "seven": "7",
                       "eight": "8",
                       "nine": "9"}


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
    mapping = {"complete": False,
               "0": {"zero": ""},
               "1": {"one": ""},
               "2": {"two": ""},
               "3": {"three": ""},
               "4": {"four": ""},
               "5": {"five": ""},
               "6": {"six": ""},
               "7": {"seven": ""},
               "8": {"eight": ""},
               "9": {"nine": ""}, }
    undecoded_data = []
    tot = 0
    for input_d, output_d in zip(input_data, output_data):
        for o in output_d:
            o = "".join(sorted(o))
            for i in input_d:
                i = "".join(sorted(i))
                added = easy_decode(mapping, i)
                if not added and o == i:
                    undecoded_data.append(i)

        for undec in undecoded_data:
            map_the_rest(mapping, undec)

        value = ""
        for o in output_d:
            o = "".join(sorted(o))
            tmp = final_dec(mapping, o).keys()
            for key in tmp:
                tmp = str(key)
            value += SEVEN_DIGIT_MAPPING[tmp]
        tot += int(value)
        #print(value + "\n")

        undecoded_data.clear()
        reset(mapping)
    return mapping, tot


def reset(data: dict):
    data["0"]["zero"] = ""
    data["1"]["one"] = ""
    data["2"]["two"] = ""
    data["3"]["three"] = ""
    data["4"]["four"] = ""
    data["5"]["five"] = ""
    data["6"]["six"] = ""
    data["7"]["seven"] = ""
    data["8"]["eight"] = ""
    data["9"]["nine"] = ""


def final_dec(mapping: dict, i: str):
    if mapping["1"]["one"] == i:
        return mapping["1"]
    elif mapping["4"]["four"] == i:
        return mapping["4"]
    elif mapping["7"]["seven"] == i:
        return mapping["7"]
    elif mapping["8"]["eight"] == i:
        return mapping["8"]
    elif mapping["0"]["zero"] == i:
        return mapping["0"]
    elif mapping["2"]["two"] == i:
        return mapping["2"]
    elif mapping["3"]["three"] == i:
        return mapping["3"]
    elif mapping["5"]["five"] == i:
        return mapping["5"]
    elif mapping["6"]["six"] == i:
        return mapping["6"]
    elif mapping["9"]["nine"] == i:
        return mapping["9"]
    else:
        print("final decode error")
        print_mappning(mapping)
        print(f"input {i}")
        exit(0)


def print_mappning(mapping):
    for k in mapping:
        print(f" {k} : {mapping[k]}")


def easy_decode(mapping: dict, i: str):
    if len(i) == 2:
        mapping["1"]["one"] = i
        return True
    elif len(i) == 4:
        mapping["4"]["four"] = i
        return True
    elif len(i) == 3:
        mapping["7"]["seven"] = i
        return True
    elif len(i) == 7:
        mapping["8"]["eight"] = i
        return True
    return False


def map_the_rest(data: dict, i: str):
    # 9
    nine = get_rest(i, data["8"]["eight"])
    nine_2 = get_rest(data["4"]["four"], i)
    if len(nine) == 1 and len(nine_2) == 2:
        data["9"]["nine"] = i

    # 3
    three = get_rest(data["4"]["four"], i)
    three_2 = get_rest(data["7"]["seven"], i)
    if len(three) == 2 and len(three_2) == 2:
        data["3"]["three"] = i

    # 6
    six = get_rest(i, data["8"]["eight"])
    six_2 = get_rest(data["7"]["seven"], i)
    six_3 = get_rest(data["1"]["one"], i)
    if len(six) == 1 and len(six_2) == 4 and len(six_3) == 5:
        data["6"]["six"] = i

    # 0
    zero = get_rest(data["1"]["one"], i)
    zero_2 = get_rest(data["4"]["four"], i)
    zero_3 = get_rest(i, data["8"]["eight"])
    if len(zero) == 4 and len(zero_2) == 3 and len(zero_3) == 1:
        data["0"]["zero"] = i

    # 5
    five = get_rest(data["1"]["one"], i)
    five_2 = get_rest(data["4"]["four"], i)
    five_3 = get_rest(i, data["8"]["eight"])
    if len(five) == 4 and len(five_2) == 2 and len(five_3) == 2:
        data["5"]["five"] = i

    # 2
    two = get_rest(data["7"]["seven"], i)
    two_2 = get_rest(data["4"]["four"], i)
    two_3 = get_rest(data["1"]["one"], i)
    two_4 = get_rest(i, data["8"]["eight"])
    if len(two) == 3 and len(two_2) == 3 and len(two_3) == 4 and len(two_4) == 2:
        data["2"]["two"] = i


def get_rest(sub_str: str, res: str):
    for c in sub_str:
        res = res.replace(c, "")
    return res


if __name__ == "__main__":
    input_data, output_data = read_input()
    decoded_data, tot = decode(input_data, output_data)
    print(tot)
