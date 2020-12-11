import copy


if __name__ == '__main__':
    data = []
    with open("day-11-data", "r") as f:
        [data.append(list(line[:-1])) for line in f.readlines()]

    has_changed = True
    while has_changed:
        has_changed = False
        temp = copy.deepcopy(data)
        for i in range(len(data)):
            for j in range(len(data[0])):
                occupied_numbers = 0
                if i > 0 and j > 0 and data[i - 1][j - 1] == "#":
                    occupied_numbers += 1
                if i > 0 and data[i - 1][j] == "#":
                    occupied_numbers += 1
                if i > 0 and j < len(data[0]) - 1 and data[i - 1][j + 1] == "#":
                    occupied_numbers += 1
                if j > 0 and data[i][j - 1] == "#":
                    occupied_numbers += 1
                if j < len(data[0]) - 1 and data[i][j + 1] == "#":
                    occupied_numbers += 1
                if i < len(data) - 1 and j > 0 and data[i + 1][j - 1] == "#":
                    occupied_numbers += 1
                if i < len(data) - 1 and data[i + 1][j] == "#":
                    occupied_numbers += 1
                if i < len(data) - 1 and j < len(data[0]) - 1 and data[i + 1][j + 1] == "#":
                    occupied_numbers += 1

                if data[i][j] == "L" and occupied_numbers == 0:
                    temp[i][j] = "#"
                    has_changed = True
                elif data[i][j] == "#" and occupied_numbers >= 4:
                    temp[i][j] = "L"
                    has_changed = True

        data = temp

    result = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                result += 1
    print(result)
