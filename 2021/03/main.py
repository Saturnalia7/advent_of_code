def read_data():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data


def part1():
    data = read_data()
    array_sums = [0] * len(data[0])
    for record in data:
        for idx, char in enumerate(record):
            array_sums[idx] += int(char)

    gamma = ""
    epsilon = ""
    for _sum in array_sums:
        if _sum / len(data) > 0.5:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    result = gamma * epsilon
    return result


def part2():
    data = read_data()
    ox = loop_for_bit(_type="ox", source_list=data)
    co2 = loop_for_bit(_type="co2", source_list=data)
    return ox * co2


def loop_for_bit(_type: str, source_list: list) -> list:

    switch = {
        "ox": {"+": "1", "-": "0", "eq": "1"},
        "co2": {"+": "0", "-": "1", "eq": "0"},
    }

    loop_list = source_list
    array_sums = [0] * len(source_list)
    for bit in range(len(loop_list[0])):
        for record in loop_list:
            array_sums[bit] += int(record[bit])
        if array_sums[bit] / len(loop_list) > 0.5:
            val = switch[_type]["+"]
        elif array_sums[bit] / len(loop_list) < 0.5:
            val = switch[_type]["-"]
        else:
            val = switch[_type]["eq"]
        remove = []
        for record in loop_list:
            if record[bit] != val:
                remove.append(record)
        loop_list = list(set(loop_list) - set(remove))
        if len(loop_list) == 1:
            break
    rating = int(loop_list[0], 2)
    return rating


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
