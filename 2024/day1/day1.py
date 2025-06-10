import os


def read_input(filename):
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, filename)
    with open(file_path, "r") as f:
        data1 = []
        data2 = []
        for line in f:
            #print(line)
            #print(line.split())
            d1, d2 = line.split()
            data1.append(int(d1))
            data2.append(int(d2))
            #print(d1)
            #print(d2)
    return data1, data2

def handle_and_calc_dist(data1, data2):
    data1.sort()
    data2.sort()
    print(data1)
    print(data2)

    res = []
    for d1, d2 in zip(data1, data2):
        res.append(abs(d1-d2))
    print(sum(res))

def similarity_score(data1, data2):
    res = []
    for d1 in data1:
        res.append(data2.count(d1) * d1)
    print(sum(res))

if __name__ == "__main__":
    #filename = "sample_input.txt"
    filename = "input.txt"
    data1, data2 = read_input(filename)
    #handle_and_calc_dist(data1, data2)
    similarity_score(data1, data2)
