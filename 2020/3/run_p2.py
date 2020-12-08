slopes = [[1,1], [3,1], [5, 1], [7,1], [1,2]]
trackers = [[0,0] for _ in slopes]

def run():
    with open("input.txt", "r") as fp:
        trees = 0
        line = fp.readline().strip()
        y = 0
        while line:
            for slope, tracker in zip(slopes, trackers):
                print(trackers, slope)
                if y % slope[1] == 0:
                    if line[tracker[0] % len(line)] == "#":
                        tracker[1] += 1
                    tracker[0] += slope[0]

            line = fp.readline().strip()
            y += 1

        product = 1
        for t in trackers:
            product = product * t[1]
        return product


print(run())
