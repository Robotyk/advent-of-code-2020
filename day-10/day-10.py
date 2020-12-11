def count_one_and_three_diff():
    one_jolt_diff, three_jolt_diff = 0, 1
    if data[0] == 1:
        one_jolt_diff += 1
    if data[0] == 3:
        three_jolt_diff += 1
    for i in range(len(data) - 1):
        if data[i + 1] - data[i] == 1:
            one_jolt_diff += 1
        if data[i + 1] - data[i] == 3:
            three_jolt_diff += 1

    return one_jolt_diff, three_jolt_diff


# def build_tree(root, element):
#     if len(root[1]) == 0:
#         return
#     for child in root[1]:
#         if 1 <= (element[0] - child[0]) <= 3 and element[0] not in [x[0] for x in child[1]]:
#             child[1].append(element)
#         build_tree(child, (element[0], []))
#
#
# def count_routes(root, counter):
#     if len(root[1]) == 0:
#         counter += 1
#         return counter
#     for child in root[1]:
#         counter = count_routes(child, counter)
#     return counter


if __name__ == '__main__':
    data = []
    with open("day-10-data", "r") as f:
        [data.append(int(line[:-1])) for line in f.readlines()]
    data.sort()

    print("First part answer: " + str(count_one_and_three_diff()[0] * count_one_and_three_diff()[1]))

    data.insert(0, 0)
    data.append(data[len(data) - 1] +  3)
    super_count = 1
    prev_count = 1
    prev_prev_count = 1
    prev_prev_prev_count = 1
    for i in range(len(data) - 3):
        count = 0
        if data[i + 1] - data[i] <= 3:
            count += 1
        if data[i + 2] - data[i] <= 3:
            count += 1
        if data[i + 3] - data[i] <= 3:
            count += 1
        super_count += count * prev_count + count * prev_prev_count + count * prev_prev_prev_count
        prev_prev_prev_count = prev_prev_count
        prev_prev_count = prev_count
        prev_count = count
    print(super_count)



    # first
    #
    # first_element = (data[0], [])
    # root = (-1, [first_element])
    # data.append(data[len(data) - 1] + 3)
    #
    # print(len(data))
    # for i in range(1, len(data)):
    #     print(i)
    #     build_tree(root, (data[i], []))
    #     i += 1
    #
    # tree_end = data[len(data) - 1]
    # print(count_routes(root, 0))

    # second
    #
    # routes = [[0]]
    # data.append(data[len(data) - 1] + 3)
    #
    # for i in range(len(data)):
    #     print(i)
    #     unique_routes = []
    #     for route in routes:
    #         if route not in unique_routes:
    #             unique_routes.append(route)
    #     routes = unique_routes
    #     routes_size = len(routes)
    #     for j in range(routes_size):
    #         route_len = len(routes[j])
    #         if data[i] - routes[j][route_len - 1] <= 3:
    #             routes[j].append(data[i])
    #         if route_len >= 2 and data[i] - routes[j][route_len - 2] <= 3:
    #             temp = routes[j][:-2]
    #             temp.append(data[i])
    #             routes.append(temp)
    #         if route_len >= 3 and data[i] - routes[j][route_len - 3] <= 3:
    #             temp = routes[j][:-3]
    #             temp.append(data[i])
    #             routes.append(temp)
    #
    # print(len(routes))