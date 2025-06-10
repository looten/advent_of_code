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
    update_idx = []
    cnt = 0
    for update in updates:
        print("\n")
        recheck_rules = True
        while recheck_rules:
            recheck_rules = False
            for rule in rules:
                if any(x in rule.keys() for x in update) and any(x in rule.values() for x in update):
                    #print(f"u {update} r {rule}")
                    complete = False
                    while not complete:
                        prev_data = []
                        for u in update:
                            prev_data.append(u)
                            #print("prev_data ", prev_data)
                            #print("u ", u)
                            #print("rule.keys() ", rule.keys())
                            #print("u in rule.keys() ", u in rule.keys())
                            #print("rule.values()  ", list(rule.values() ))
                            #print("prev_data ", prev_data)
                            #print("rule.values() in prev_data ", any(p in list(rule.values()) for p in prev_data))
                            check_p = any(p in list(rule.values()) for p in prev_data)
                            if u in rule.keys() and check_p:
                                #print("broke rule!")
                                #print(update)
                                #print(rule)
                                idx1 = update.index(list(rule.keys())[0])
                                idx2 = update.index(list(rule.values())[0])
                                tmp = update[idx1]
                                update[idx1] = update[idx2]
                                update[idx2] = tmp
                                #print("after swap")
                                #print(update)
                                recheck_rules = True
                                update_idx.append(cnt)
                                #break
                            else:
                                complete = True
        cnt+=1
    for i in range(len(updates)):
        if i not in update_idx:
            continue
        else:
            #if broken_rule:
            update = updates[i]
            middle = update[len(update) // 2]
            #print(middle)
            #print mid_indx
            print("middle")
            print(middle)
            sum += middle
    print(sum)


if __name__ == "__main__":
    filename = "sample_input.txt"
    filename = "input.txt"
    rules, updates = read_input(filename)
    #print(rules)
   # print(updates)
    check_updates(rules, updates)
