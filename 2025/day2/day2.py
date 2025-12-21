import os


def read_input(filename):
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, filename)
    with open(file_path, "r") as f:
        data = []
        for line in f:
            data = line.split(",")
    return data

def decode(data):
    answer = 0
    for d in data:
        print(d)
        start, end = d.split("-")
        start = int(start)
        end = int(end)
        #print(start)
        #print(end)
        for val in range(start, end+1):
            print("*"*10)
            print(val)
            #if len(str(val)) > and len(str(val)) % 2 == 0:
            c = str(val)[0]
            rem = str(val)[1:]
            #print(f"c {c} rem {rem}")
            if search(c, rem, ""):
                print(f"found {val}")
                answer += val
    print(f"Answer: {answer}")

def search(c, rem, l):
    print(f"{c} in {rem} num {rem.count(c)} ")
    print(f"{len(rem) >= 1} {rem.count(c) >= 1} ")
    if (rem.count(c) != 0 and rem.count(c) % 2 == 0) or (len(rem) >= 1 and rem.count(c) >= 1):
        #try:
        
        if len(rem) > 1:
            print(f"keep search")
            input()
            x = rem[0]
            n_rem = rem[1:]
            search(x, n_rem, l)
        else:
            #print(f"ret true")
            return True
    else:
        print(f"ret false")
        return False

if __name__ == "__main__":
    filename = "sample_input.txt"
    #filename = "input.txt"
    data = read_input(filename)
    decode(data)
