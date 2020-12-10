if __name__ == '__main__':
    data = []
    with open("day-10-data", "r") as f:
        [data.append(int(line[:-1])) for line in f.readlines()]

    data.sort()

    one_jolt_diff = 0
    three_jolt_diff = 1

    if data[0] == 1:
        one_jolt_diff += 1
    if data[0] == 3:
        three_jolt_diff += 1


    for i in range(len(data) - 1):
        if data[i + 1] - data[i] == 1:
            one_jolt_diff += 1
        if data[i + 1] - data[i] == 3:
            three_jolt_diff += 1



    print("First part answer: " + str(one_jolt_diff * three_jolt_diff))





