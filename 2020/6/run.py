def run():
    with open("input.txt", "r") as fp:
        line = fp.readline()
        tracker = set()
        sum_n = 0
        while line:
            if line == "\n":
                sum_n += len(tracker)
                tracker = set()
            else:
                for c in line.strip():
                    tracker.add(c)
            line = fp.readline()

        sum_n += len(tracker)
        return sum_n

print(run())
