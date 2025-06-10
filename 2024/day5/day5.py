import os


def read_input(filename):
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, filename)
    with open(file_path, "r") as f:
        rules = []
        updates = []
        for line in f:
            if "|" in line:
                rule = dict()
                first, second = line.split("|")
                rule[int(first)] = int(second)
                rules.append(rule)
            elif "," in line:
                update = []
                for u in line.split(","):
                    update.append(int(u))
                updates.append(update)
    return rules, updates

def check_updates(rules, updates):
    sum = 0
    complete = True
    update_idx = []
    for update in updates:
        for rule in rules:
            #print(rule)
            if any(x in rule.keys() for x in update) and any(x in rule.values() for x in update):
                #print(f"u {update} r {rule}")
                prev_data = []
                complete = False
                while not complete:
                    for u in update:
                        prev_data.append(u)
                        #print("u ", u)
                        #print("rule.keys() ", rule.keys())
                        #print("u in rule.keys() ", u in rule.keys())
                        #print("rule.values()  ", list(rule.values() ))
                        #print("prev_data ", prev_data)
                        #print("rule.values() in prev_data ", any(p in list(rule.values()) for p in prev_data))
                        check_p = any(p in list(rule.values()) for p in prev_data)
                        if u in rule.keys() and check_p:
                            print("broke rule!")
                            print(update)
                            print(rule)
                            idx1 = update.index(list(rule.keys())[0])
                            idx2 = update.index(list(rule.values())[0])
                            tmp = update[idx1]
                            update[idx1] = update[idx2]
                            update[idx2] = tmp
                            print("after swap")
                            print(update)
                            broken_rule = True
                            update_idx.append(cnt)
                            #break
                        else:
                            complete = True
        cnt+=1

    for idx in update_idx:
        #if broken_rule:
        middle = update[len(update[idx]) // 2]
        #print(middle)
        #print mid_indx
        print("middle")
        print(middle)
        sum += middle
    print(sum)


if __name__ == "__main__":
    filename = "sample_input.txt"
    #filename = "input.txt"
    rules, updates = read_input(filename)
    #print(rules)
   # print(updates)
    check_updates(rules, updates)
