import numpy as np


class Board:
    def __init__(self, data: list):
        self.rows = self._make_rows(data=data)
        self.state = np.zeros((5, 5))
        self.won = 0

    def _make_rows(self, data: list):
        rows = [0] * len(data)
        for idx, _ in enumerate(data):
            rows[idx] = [int(val) for val in data[idx].split()]
        return rows

    def _mark_state(self, move: int):
        for i, row in enumerate(self.rows):
            for j, space in enumerate(row):
                if space == move:
                    self.state[i, j] = 1

    def _check_state(self):
        result = 0
        critera = [1.0] * 5
        for i in range(len(self.rows)):
            if critera == self.state[i, :].tolist():
                result = 1
            elif critera == self.state[:, i].tolist():
                result = 1
        if critera == self.state.diagonal().tolist():
            result = 1
        if critera == np.flipud(self.state).diagonal().tolist():
            result = 1
        return result

    def sum_unmarked(self):
        _sum = 0
        for idx, i in enumerate(self.state):
            for jdx, j in enumerate(i):
                if j == 0.0:
                    _sum += self.rows[idx][jdx]
        return _sum

    def make_move(self, move, **kwargs):
        result = 0
        self._mark_state(move=move, **kwargs)
        self.won = self._check_state()
        if self.won == 1:
            result = self.sum_unmarked()
        return result


def read_data():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data


def part1(moves: list, boards: list):
    for move in moves:
        for board in boards:
            win_result = board.make_move(move=move)
            if win_result != 0:
                print(move * win_result)
                return


def part2(moves: list, boards: list):
    for move in moves:
        for board in boards:
            win_result = None
            if board.won == 0:
                win_result = board.make_move(move=move)
            if win_result != 0:
                if sum([b.won for b in boards]) == len(boards):
                    print(move * win_result)
                    return


def main():
    data = read_data()
    moves = [int(val) for val in data[0].split(",")]
    boards = []
    for i in range(2, len(data), 6):
        boards.append(Board(data=data[i : i + 5]))

    part1(moves=moves, boards=boards)
    part2(moves=moves, boards=boards)


if __name__ == "__main__":
    main()
