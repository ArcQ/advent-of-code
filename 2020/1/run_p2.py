arr = []
fp = open("input.txt", "r")
arr = [int(line.strip()) for line in fp.readlines()]

def run():
    for i,a in enumerate(arr[:-2]):
        diff_one = 2020 - a

        j = i + 1
        diffs = {}
        diffs[diff_one - arr[j]] = arr[j]

        while j < len(arr) - 1:
            j += 1
            if arr[j] in diffs:
                return arr[j] * diffs[arr[j]] * a
            diffs[diff_one - arr[j]] = arr[j]
    return nil

print(run())
