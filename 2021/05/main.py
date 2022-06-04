def read_data():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data


def get_points(data: list):
    points = []
    for _set in data:
        _set = _set.split(" -> ")
        set_conv = []
        for point in _set:
            set_conv.append([int(val) for val in point.split(",")])
        points.append(set_conv)
    return points


def iter_list_max(data: list, _max=None):
    if _max is None:
        _max = float("-inf")
    for el in data:
        if isinstance(el, list):
            _max = iter_list_max(el, _max)
        else:
            _max = max(el, _max)
    return _max


def part1(points: list):
    result = 0
    _max = iter_list_max(points)
    print(_max)
    return result


def main():
    data = read_data()
    points = get_points(data=data)

    print(part1(points))


if __name__ == "__main__":
    main()
