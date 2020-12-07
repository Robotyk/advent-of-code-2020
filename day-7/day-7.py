import re

if __name__ == '__main__':
    file = open("day-7-data", "r")

    data = {}
    for line in file.readlines():
        re_split = re.split("\d", line)
        if len(re_split) > 1:
            bags = []
            for x in re_split:
                bags.append(x.split())
            data[bags[0][0] + " " + bags[0][1]] = [x[0] + " " +x[1] for x in bags[1:]]

    bags_for_gold = set()
    prev_set_size = -1
    while prev_set_size != len(bags_for_gold):
        prev_set_size = len(bags_for_gold)
        for k, v in data.items():
            if "shiny gold" in v or [x for x in bags_for_gold if x in v]:
                bags_for_gold.add(k)

    print("First part answer: " + str(len(bags_for_gold)))
