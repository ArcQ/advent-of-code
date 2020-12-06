diffs = {}

def run():
    with open("input.txt", "r") as fp:
        line = fp.readline()
        diffs[2020 - int(line)] = int(line)

        while line:
            line = fp.readline()
            if not line:
                return nil
            n = int(line)
            if n in diffs:
                return n * diffs[n]
            if line:
                diffs[2020 - n] = n

print(run())
