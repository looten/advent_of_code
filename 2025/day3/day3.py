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
    K = 12
    for d in data:
        print(d)
        n = len(d)
        tmp = []
        for idx, i in enumerate(d):
            rem = n - idx
            while tmp and i > tmp[-1] and len(tmp) - 1 + rem >= K:
                tmp.pop()
            if len(tmp) < K:
                tmp.append(i)

        t_str = ""
        for t in tmp:
            t_str += str(t)
        print("len tmp:", len(t_str))
        if len(t_str) != 12:
            exit("ERROR LENGTH NOT 12")
        print(t_str)
        answer += int(str(t_str))
    print(f"Answer: {answer}")

if __name__ == "__main__":
    filename = "sample_input.txt"
    filename = "input.txt"
    data = read_input(filename)
    decode(data)