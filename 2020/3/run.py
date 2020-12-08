
def run():
    with open("input.txt", "r") as fp:
        trees = 0
        line = fp.readline().strip()
        x = 0
        while line:
            if line[x % len(line)] == "#":
                trees += 1
            x += 3
            line = fp.readline().strip()

        return trees


print(run())
