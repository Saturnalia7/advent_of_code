def read_data() -> list:
    """Read input data from txt

    :return: input data with \n stripped
    :rtype: list
    """
    # This is a context manager
    # Useful for closing objects or connections after use
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data


def part1() -> int:
    """Solves part 1

    :return: number of times current number is greater than previous
    :rtype: int
    """
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

        # Set for next eval pass
        previous_val = record
    return result


def part2() -> int:
    """Solves part 2

    :return: number of times current 3 sum window is greater than previous 3 sum
        window
    :rtype: int
    """
    data = read_data()
    previous_sum = None
    result = 0
    for idx, _ in enumerate(data):
        # Skip over until first 3 sum window
        if idx < 2:
            continue

        # Get sum of sliding window
        sum = int(data[idx]) + int(data[idx - 1]) + int(data[idx - 2])

        # Set previous on first pass
        if previous_sum is None:
            previous_sum = sum

        # Evaluate
        if previous_sum < sum:
            result += 1

        # Set previous for next eval pass
        previous_sum = sum
    return result


def main():
    print(part1())
    print(part2())


# If done via python main.py in terminal,
# this will call main
if __name__ == "__main__":
    main()
