def read_data():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data


def part1():
    data = read_data()
    result = 0
    previous_val = None
    for record in data:
        # Cast to integer
        record = int(record)
        # Set previous value on first pass
        if previous_val is None:
            previous_val = record

        # Evaluate
        if previous_val < record:
            result += 1

        previous_val = record
    return result


def part2():
    data = read_data()
    previous_sum = None
    result = 0
    for idx, record in enumerate(data):
        if idx < 2:
            continue
        sum = int(data[idx]) + int(data[idx - 1]) + int(data[idx - 2])
        if previous_sum is None:
            previous_sum = sum

        if previous_sum < sum:
            result += 1

        previous_sum = sum
    return result


def main():
    print(part1())
    print(part2())


# If done via python main.py in terminal,
# this will call main
if __name__ == "__main__":
    main()
