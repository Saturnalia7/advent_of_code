from os import read


def read_data():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data


def part1():
    data = read_data()
    depth = 0
    horizontal = 0
    for record in data:
        datum = record.split()
        move = int(datum[1])
        if datum[0] == "forward":
            horizontal += move
        elif datum[0] == "up":
            depth -= move
        elif datum[0] == "down":
            depth += move

    result = depth * horizontal
    return result


def part2():
    data = read_data()
    depth = 0
    horizontal = 0
    aim = 0
    for record in data:
        datum = record.split()
        move = int(datum[1])
        if datum[0] == "forward":
            horizontal += move
            depth += aim * move
        elif datum[0] == "up":
            aim -= move
        elif datum[0] == "down":
            aim += move

    result = depth * horizontal
    return result


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
