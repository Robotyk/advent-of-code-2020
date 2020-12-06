if __name__ == '__main__':
    file = open("day-6-data", "r")
    forms = []
    questions = set()
    for line in file.readlines():
        if line is "\n":
            forms.append(questions)
            questions = set()
        else:
            questions.update(line[:-1])

    forms.append(questions)

    sum = sum([len(x) for x in forms])

    print("First part answer: " + str(sum))

