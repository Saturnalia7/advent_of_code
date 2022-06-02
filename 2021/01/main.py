def read_data():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data


def main():
    data = read_data()
    counter = 0
    previous_val = None
    for record in data:
        # Cast to integer
        record = int(record)
        # Set previous value on first pass
        if previous_val is None:
            previous_val = record

        # Evaluate
        if previous_val < record:
            counter += 1

        previous_val = record
    print(counter)


# If done via python main.py in terminal,
# this will call main
if __name__ == "__main__":
    main()
