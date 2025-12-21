import os


def read_input(filename):
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, filename)
    with open(file_path, "r") as f:
        data = []
        cnt = 0
        for line in f:
            #print(line)
            #print(line.split())
            direction = line[0]
            steps = int(line[1:].replace("\n",""))
            #if steps > 99:
             #   steps = steps % 99
            data.append({cnt:{direction: steps}})
            #print(data)
            cnt += 1
    return data

def decode(data):
    numbers = [x for x in range(0, 100)]
    #print(data)
    num = 50
    answer = 0
    print(f"The dial starts by pointing at {num}")
    for d in data:
        for k,v in d.items():
            #print(k)
            if 'L' in v:
                # go left
                steps = v['L']

                num -= steps
            else:
                steps = v['R']
                num += steps

            if num % 100 == 0:
	            answer += 1
            #if steps > 99:
                #input()
    print(f"Answer: {answer}")
            #print(steps)
if __name__ == "__main__":
    filename = "sample_input.txt"
    filename = "input.txt"
    data = read_input(filename)
    #handle_and_calc_dist(data1, data2)
    decode(data)
