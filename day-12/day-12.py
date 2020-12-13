def calculate_position():
    x_pos, y_pos, direction = 0, 0, 90
    for instr in data:
        if instr[0] == "N" or (instr[0] == "F" and direction == 0):
            y_pos -= instr[1]
        if instr[0] == "S" or (instr[0] == "F" and direction == 180):
            y_pos += instr[1]
        if instr[0] == "E" or (instr[0] == "F" and direction == 90):
            x_pos += instr[1]
        if instr[0] == "W" or (instr[0] == "F" and direction == 270):
            x_pos -= instr[1]
        if instr[0] == "R":
            direction = (direction + instr[1]) % 360
        if instr[0] == "L":
            direction = (direction - instr[1]) % 360
    return x_pos, y_pos


if __name__ == '__main__':
    data = []
    with open("day-12-data", "r") as f:
        [data.append((line[:1], int(line[1:-1]))) for line in f.readlines()]

    print("First part answer: " + str(calculate_position()[0] + calculate_position()[1]))