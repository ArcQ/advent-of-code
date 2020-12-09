from copy import copy

def run():
    valid_passports = 0
    passport_check = {"byr": 0,
                      "iyr": 0,
                      "eyr": 0,
                      "hgt": 0,
                      "hcl": 0,
                      "ecl": 0,
                      "pid": 0,
                      "cid": 1
                      }
    passport = copy(passport_check)

    with open("input.txt", "r") as fp:
        line = fp.readline()
        while line:
            splits=line.split(" ")
            if line == "\n":
                if all(v == 1 for v in passport.values()):
                    valid_passports += 1
                passport = copy(passport_check)
            else:
                for kv in splits:
                    kv_splits = kv.split(":")
                    k = kv_splits[0]
                    passport[k] = 1

            line = fp.readline()

        if all(v == 1 for v in passport.values()):
            valid_passports += 1
        return valid_passports


print(run())
