if __name__ == '__main__':
    file = open("day-5-data", "r")
    table = {70: 48, 66: 49, 82: 49, 76: 48}
    max = 0
    for line in file.readlines():
        row = int(line[:-4].translate(table), 2)
        column = int(line[-4:].translate(table), 2)
        seat_id = row * 8 + column
        if max < seat_id:
            max = seat_id

    print("First part answer: " + str(max))
