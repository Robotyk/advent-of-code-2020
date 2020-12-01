def find_summands(data):
    x_1 = 0
    length = len(data)
    while x_1 < length:
        x_2 = x_1 + 1
        while data[x_1] + data[x_2] <= 2020:
            if data[x_1] + data[x_2] == 2020:
                return data[x_1], data[x_2]
            else:
                x_2 = x_2 + 1
        x_1 = x_1 + 1


if __name__ == '__main__':
    file = open("day-1/day-1-data", "r")
    data = list(map(int, file.readlines()))
    data.sort()

    summands = find_summands(data)

    answer = summands[0] * summands[1]

    print(answer)

    file.close()
