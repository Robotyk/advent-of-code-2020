def prepare_data():
    file = open("day-4-data", "r")
    data = []
    passport = {}
    for line in file.readlines():
        if line is not "\n":
            line = line[:len(line) - 1]
            for pair in line.split(" "):
                parts = pair.split(":")
                passport[parts[0]] = parts[1]
        else:
            data.append(passport)
            passport = {}
    data.append(passport)
    file.close()

    return data


if __name__ == '__main__':
    data = prepare_data()

    valid_passports_quantity = 0
    for passport in data:
        if all (key in passport.keys() for key in {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}):
            valid_passports_quantity = valid_passports_quantity + 1

    print("First part answer: " + str(valid_passports_quantity))