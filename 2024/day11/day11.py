import os
import copy
import time
import pandas as pd

def read_input(filename):
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, filename)
    with open(file_path, "r") as f:
        input_data = []
        for line in f:
            for u in line.split(" "):
                input_data.append(int(u))
    return input_data

def stone_rule_exec(input_data, blinks):
    print("Initial arrangement:")
    print(input_data)
    blink_results = input_data
    data = {'temp': blink_results}
    #data2 = {'temp': []}

    df = pd.DataFrame(data)
    df_temp = pd.DataFrame(data=[],columns=['temp'])
    
    df['temp'] = pd.to_numeric(df['temp'], downcast='integer')
    df_temp['temp'] = pd.to_numeric(df_temp['temp'], downcast='integer')

    start = time.time()
    for blink in range(blinks):
        df_temp = pd.DataFrame(data=[],columns=['temp'])
        for _, row in df.iterrows():
            #print("new loop ")
            #print(df_temp)
            #print("df ")
            #print(df)
            d = row["temp"]
            #print(" curr data ", d)
            if d == 0:
                #print("zero")
                df_temp = df_temp._append({"temp": 1}, ignore_index=True)
            elif len(str(d)) % 2 == 0:
                #print("split")
                q, r = divmod(len(str(d)), 2)
                d_st = str(d)
                first, sec = d_st[:q + r], d_st[q + r:]

                #print("first ", int(first))
                #print("sec ", int(sec))
                df_temp = df_temp._append({"temp": int(first)}, ignore_index=True)
                df_temp = df_temp._append({"temp": int(sec)}, ignore_index=True)
            else:
                #print("mult")
                df_temp = df_temp._append({"temp": int(d*2024)}, ignore_index=True)
        
        #print("COMPLETE")
        #print(df_temp)
        df = df_temp.copy(deep=True)
        df.dropna(inplace = True)
        #print(df)
        print(f"After {blink+1} blink/s: {time.time()-start} ")
        #print(" ".join(map(str, blink_results)))
        #print("df ")
        #print(df)
    print("df ")
    print(df)
    print("df len ", len(df))

if __name__ == "__main__":
    filename = "sample_input1.txt"
    blinks = 1

    filename = "sample_input2.txt"
    blinks = 6

    filename = "input.txt"
    blinks = 75

    input_data = read_input(filename)
    stone_rule_exec(input_data, blinks)
