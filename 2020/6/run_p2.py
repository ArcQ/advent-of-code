def run():
    with open("input.txt", "r") as fp:
        line = fp.readline()
        tracker = {}
        sum_n = 0
        p = 0
        while line:
            if line == "\n":
                for k in tracker.keys():
                    if tracker[k] == p:
                        sum_n += 1
                tracker = {}
                p = 0
            else:
                p += 1
                for c in line.strip():
                    if c in tracker:
                        tracker[c] += 1
                    else:
                        tracker[c] = 1
            line = fp.readline()
            print(tracker)
        for k in tracker.keys():
            if tracker[k] == p:
                sum_n += 1

        return sum_n

print(run())
