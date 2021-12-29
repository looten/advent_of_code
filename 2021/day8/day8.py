
filename = "/home/looten/workspace/advent_of_code/2021/day8/test_data2.txt"
#filename = "/home/looten/workspace/advent_of_code/2021/day8/input.txt"
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
    mapping = {"complete": False,
               "0": {"zero": "", "cnt": 0},
               "1": {"one": "", "cnt": 0},
               "2": {"two": "", "cnt": 0},
               "3": {"three": "", "cnt": 0},
               "4": {"four": "", "cnt": 0},
               "5": {"five": "", "cnt": 0},
               "6": {"six": "", "cnt": 0},
               "7": {"seven": "", "cnt": 0},
               "8": {"eight": "", "cnt": 0},
               "9": {"nine": "", "cnt": 0}, }
    #decoded_data = [mapping, mapping, mapping, mapping]
    undecoded_data = []
    print(len(undecoded_data))
    row = 0
    for input_d, output_d in zip(input_data, output_data):
        row += 1
        print("row", row)
        for o in output_d:
            o = "".join(sorted(o))
            for i in input_d:
                i = "".join(sorted(i))
                #print("in", i)
                added = easy_decode(mapping, i)
                if not added and o == i:
                    undecoded_data.append(i)
    
        for undec in undecoded_data:
            map_the_rest(mapping, undec)

        for o in output_d:
            o = "".join(sorted(o))
            print(final_dec(mapping, o))

        #for undec in undecoded_data:
            #count_other(mapping, undec)
        undecoded_data.clear()
        reset(mapping)
    return mapping


def reset(data : dict):
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
        mapping["1"]["cnt"] += 1
        return True
    elif len(i) == 4:
        mapping["4"]["four"] = i
        mapping["4"]["cnt"] += 1
        return True
    elif len(i) == 3:
        mapping["7"]["seven"] = i
        mapping["7"]["cnt"] += 1
        return True
    elif len(i) == 7:
        mapping["8"]["eight"] = i
        mapping["8"]["cnt"] += 1
        return True
    return False


def count_other(mapping: dict, i: str):
    if mapping["0"]["zero"] == i:
        mapping["0"]["cnt"] += 1

    elif mapping["2"]["two"] == i:
        mapping["2"]["cnt"] += 1

    elif mapping["3"]["three"] == i:
        mapping["3"]["cnt"] += 1

    elif mapping["5"]["five"] == i:
        mapping["5"]["cnt"] += 1

    elif mapping["6"]["six"] == i:
        mapping["6"]["cnt"] += 1

    elif mapping["9"]["nine"] == i:
        mapping["9"]["cnt"] += 1

    else:
        print("what?")
        exit(0)


def map_the_rest(data: dict, i: str):
    # 9
    #if not data["9"]["nine"]:
    tmp = data["4"]["four"] + data["7"]["seven"]
    tmp = "".join(sorted(set(tmp)))
    data["9"]["nine"] = tmp

    # 3
    three = get_rest(data["4"]["four"], i)
    three_2 = get_rest(data["7"]["seven"], i)
    if len(three) == 2 and len(three_2) == 2:
        data["3"]["three"] = i

    six = get_rest(data["8"]["eight"], i)
    # 6
    if len(six)== 1:
        data["6"]["six"] = i

    zero = get_rest(data["9"]["nine"], i)
    # 0
    if len(zero) == 2:
        data["0"]["zero"] = i
    
    five = get_rest(data["9"]["nine"], i)
    five_2 = get_rest(data["4"]["four"], i)
    # 5
    if len(five) == 1 and len(five_2) == 2:
        data["5"]["five"] = i

   
    two = get_rest(data["9"]["nine"], i)
    two_2 = get_rest(data["4"]["four"], i)
     # 2
    if len(two) == 1 and len(two_2) == 3:
        data["2"]["two"] = i

    if False:
        if data["6"]["six"]:
            data["0"]["zero"] = i
            # 3
            print("found a 3")
            a = get_rest(data["4"]["four"], data["5"]["five"])
            b = get_rest(data["0"]["zero"], data["8"]["eight"])
            data["3"]["three"] = ''.join(sorted(set(a + b + data["1"]["one"])))
            
            # 5
            a = get_rest(data["6"]["six"], data["3"]["three"])
            print(data["3"]["three"])
            print(data["6"]["six"])
            b = get_rest(a, data["4"]["four"])
            data["5"]["five"] = ''.join(sorted(set(a + b)))
            print(a)
            print(b)
            print("five", data["5"]["five"])
            input()


            print("found a 2")
            # 2
            a = get_rest(data["9"]["nine"], data["6"]["six"])
            b = get_rest(data["0"]["zero"], data["8"]["eight"])
            print("found a 2 a)")
            c = get_rest(data["1"]["one"], data["7"]["seven"])
            d = get_rest(data["3"]["three"], data["5"]["five"])
            data["2"]["two"] = ''.join(sorted(set(a + b + c + d)))


def get_rest(sub_str: str, res: str):
    #if len(sub_str) > len(res):
     #   print("Error: sub str longer that res")
      #  exit(0)
    for c in sub_str:
        res = res.replace(c, "")
    return res


def count(data: dict):
    tot = 0
    #for data in decoded_data:
    tot += data["0"]["cnt"] + data["1"]["cnt"] + \
        data["2"]["cnt"] + data["3"]["cnt"] + \
        data["4"]["cnt"] + data["5"]["cnt"] + \
        data["6"]["cnt"] + data["7"]["cnt"] + \
        data["8"]["cnt"] + data["9"]["cnt"]
    print(f"Instances: {tot}")


if __name__ == "__main__":
    input_data, output_data = read_input()
    decoded_data = decode(input_data, output_data)
    count(decoded_data)
