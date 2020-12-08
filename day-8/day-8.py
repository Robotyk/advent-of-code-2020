if __name__ == '__main__':
    data = []
    with open("day-8-data", "r") as f:
        [data.append(line[:-1]) for line in f.readlines()]

    previous_instructions = set()
    accumulator = 0
    current_position = 0
    while True:
        if current_position in previous_instructions:
            print("First part answer: " + str(accumulator))
            break
        previous_instructions.add(current_position)
        instruction = data[current_position][:3]
        arg = int(data[current_position][4:])

        if instruction == "jmp":
            current_position += arg
        elif instruction == "acc":
            accumulator += arg
            current_position += 1
        else:
            current_position += 1
