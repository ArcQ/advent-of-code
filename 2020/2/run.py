diffs = {}

def run():
    with open("input.txt", "r") as fp:
        valid_pw_count = 0
        line = fp.readline()
        while line:
            splits = line.split(" ")

            repeats = splits[0].split("-")
            min_repeat = int(repeats[0])
            max_repeat = int(repeats[1])

            repeat_c = splits[1][:-1]

            c_count = 0

            for c in splits[2]:
                if c == repeat_c:
                    c_count += 1

            if c_count >= min_repeat and c_count <= max_repeat:
                valid_pw_count += 1

            line = fp.readline()
        return valid_pw_count


print(run())
