diffs = {}

def run():
    with open("input.txt", "r") as fp:
        valid_pw_count = 0
        line = fp.readline()
        while line:
            splits = line.split(" ")

            indexes = splits[0].split("-")
            i_one = int(indexes[0])
            i_two = int(indexes[1])

            check_c = splits[1][:-1]

            pw = splits[2]

            if (pw[i_one - 1] == check_c) != (pw[i_two - 1] == check_c):
                valid_pw_count += 1

            line = fp.readline()
        return valid_pw_count


print(run())
