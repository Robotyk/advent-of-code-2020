def find_earliest_bus():
    i = departure_timestamp
    while True:
        for x in bus_departures:
            if i % x == 0:
                return x, i - departure_timestamp
        i += 1


if __name__ == '__main__':
    with open("day-13-data", "r") as f:
        departure_timestamp = int(f.readline())
        bus_departures = [int(x) for x in f.readline().split(",") if x != "x"]

    print("First part answer: " + str(find_earliest_bus()[0] * find_earliest_bus()[1]))
