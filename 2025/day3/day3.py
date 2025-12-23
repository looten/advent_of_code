import os
import copy

def read_input(filename):
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, filename)
    with open(file_path, "r") as f:
        data = []
        for line in f:
            s = []
            for c in line:
               # print(c)
                if c != "\n":
                 s.append(int(c.replace("\n", "")))
            data.append(s)
    return data

def decode(data):
    answer = 0
    for d in data:
        print(d)
        tmp = []
        for idx, i in enumerate(d):
            print(f"start idx: {idx}, i: {i}, tmp {tmp} len tmp {len(tmp)}  len(d) - (idx + 1): {len(d) - (idx + 1)}")
            if len(tmp) < 12:
                tmp.append(i)
                print(f"start tmp {tmp}")
                if len(tmp) > 1:
                    print(f"{len(d) - (idx + 1 + len(tmp)) > 6 } {len(tmp) >=2} { tmp[-1] > tmp[-2]}")
              #  if idx < 7 and len(d) - (idx + 1) >= 6 and len(tmp) >=2 and tmp[-1] > tmp[-2]:
                if len(d) - (idx + 1 + len(tmp)) > 6 and len(tmp) >=2 and tmp[-1] > tmp[-2]:
                    new_first = tmp[-1]
                    tmp.pop()
                    tmp.pop()
                    tmp.append(new_first)
                    print(f"swapped idx: {idx}, i: {i}, tmp {tmp} len tmp {len(tmp)}")

            elif i > tmp[-1]:
                tmp.pop()
                tmp.append(i)
        t_str = ""
        for t in tmp:
            t_str += str(t)
        print("len tmp:", len(t_str))
        print(t_str)
        answer += int(str(t_str))
    print(f"Answer: {answer}")

if __name__ == "__main__":
    filename = "sample_input.txt"
    #filename = "input.txt"
    data = read_input(filename)
    decode(data)