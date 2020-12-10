from copy import copy

def run():
    max_seat = ["", 0]
    with open("input.txt", "r") as fp:
        line = fp.readline()
        while line:
            row = [0,128]
            col = [0,8]
            for c in line.strip()[:7]:
                diff = (row[1] - row[0]) / 2
                if c == 'B':
                    row[0] = row[0] + diff
                if c == 'F':
                    row[1] = row[1] - diff

            for c in line.strip()[7:]:
                diff = (col[1] - col[0]) / 2
                if c == 'R':
                    col[0] = col[0] + diff
                if c == 'L':
                    col[1] = col[1] - diff
            seat = row[0] * 8 + col[0]
            if seat > max_seat[1]:
                max_seat[0] = line.strip()
                max_seat[1] = seat
            print(seat)
            line = fp.readline()

    return max_seat

print(run())
