def read_data():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data
