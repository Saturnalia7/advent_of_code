from collections import Counter


def read_data():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data


def part1(data):
    allPoints = []
    for line in data:
        # Parse data into usable contents
        firstPoint, secondPoint = line.split("->")
        x1, y1 = tuple(map(int, firstPoint.split(",")))
        x2, y2 = tuple(map(int, secondPoint.split(",")))

        # Consider vertical & horizontal lines only
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    allPoints.append((x, y))

    return len([point for point in Counter(allPoints).values() if point > 1])


def main():
    data = read_data()

    print(part1(data))


if __name__ == "__main__":
    main()
