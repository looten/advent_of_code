filename = "/home/looten/workspace/advent_of_code/2021/day3/input.txt"

import copy

def readfile():
    array = []
    with open(filename) as f:
        lines = f.readlines()

        for line in lines:
            array.append(str(line.strip()))
    return array

def arrange(data, cnt_dict, row):
    for i in range(len(data)):
        try:
            cnt_dict[i][data[i]]["idx"].append(row)
        except KeyError:
            tmp = {data[i] : { "idx": [row]}}
            try:
                cnt_dict[i].update(tmp)
            except KeyError:
                cnt_dict[i] = tmp

def remove(cnt_dict, remove_list):
    for i in remove_list:
        for key, val in cnt_dict.items():
            try:
                val["0"]["idx"].remove(i)
            except ValueError:
                pass

            try:
                val["1"]["idx"].remove(i)
            except ValueError:
                pass

def compare(cnt_dict, array, idx):
    print(f"cnt: {idx}")
    if len(cnt_dict[idx]['1']["idx"]) >= len(cnt_dict[idx]['0']["idx"]):
        print("zeroes shall be removed")
        remove_list = copy.deepcopy(cnt_dict[idx]['0']["idx"])
        remove(cnt_dict, remove_list)
    else:
        print("ones shall be removed")
        remove_list = copy.deepcopy(cnt_dict[idx]['1']["idx"])
        remove(cnt_dict, remove_list)

def compare_low(cnt_dict, array, idx):
    print(f"cnt: {idx}")
    if len(cnt_dict[idx]['0']["idx"]) <=  len(cnt_dict[idx]['1']["idx"]):
        print("ones shall be removed")
        remove_list = copy.deepcopy(cnt_dict[idx]['1']["idx"])
        remove(cnt_dict, remove_list)
    else:
        print("zeroes shall be removed")
        remove_list = copy.deepcopy(cnt_dict[idx]['0']["idx"])
        remove(cnt_dict, remove_list)

def parse(array, version):
    cnt_dict = {}
    
    row = 0
    for data in array:
        arrange(data, cnt_dict, row)
        row += 1
    
    while len(cnt_dict[0]['1']["idx"]) > 1:
        for idx in range(12):
            #print(cnt_dict)
            if len(cnt_dict[0]['1']["idx"]) <= 1 and len(cnt_dict[0]['0']["idx"]) <= 1:
                return cnt_dict
            if version == 0:
                compare_low(cnt_dict, array, idx)
            else:
                compare(cnt_dict, array, idx)
    return cnt_dict

def get_end_val(cnt_dict):
    index = get_corr(cnt_dict[0])
    binv = array[index]
    val = int(binv, 2)
    print(f"index {index} bin {binv} dec {val}" )
    return val

def get_corr(cnt_dict):
    try: 
        return cnt_dict["0"]["idx"][0]
    except IndexError:
        return cnt_dict["1"]["idx"][0]

if __name__ == "__main__":
    array = readfile()
    array2 = copy.deepcopy(array)

    res_dict = parse(array, 0)
    scrub = get_end_val(res_dict)
    print("scrub ", scrub)

    res_dict2 = parse(array, 1)
    oxy = get_end_val(res_dict2)
    print("oxy ", oxy)

    result = oxy * scrub 
    print("result ", result)
    
