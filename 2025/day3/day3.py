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
        first = -1
        last = -1
        for idx, i in enumerate(d):
            #print(f"idx: {idx}, i: {i}, first: {first}, last: {last}")
            if i > first and idx + 1 < len(d):
                first = i
                last = -1
            elif i > last:
                last = i
        print(f"first: {first}, last: {last}")
        answer += int(str(first) + str(last))

            
    print(f"Answer: {answer}")

if __name__ == "__main__":
    filename = "sample_input.txt"
    filename = "input.txt"
    data = read_input(filename)
    decode(data)
