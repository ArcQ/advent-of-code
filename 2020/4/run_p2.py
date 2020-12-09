from copy import copy
import re

def hgt_check(v):
    if v[-2:] == "cm":
        return int(v[:-2]) >= 150 and int(v[:-2]) <= 193
    elif v[-2:] == "in":
        return int(v[:-2]) >= 59 and int(v[:-2]) <= 76
    return False

def run():
    valid_passports = 0
    passport_checker = {"byr": lambda v: int(v) >= 1920 and int(v) <= 2002,
                        "iyr": lambda v: int(v) >= 2010 and int(v) <= 2020,
                        "eyr": lambda v: int(v) >= 2020 and int(v) <= 2030,
                        "hgt": lambda v: hgt_check(v),
                        "hcl": lambda v: re.match("^\#[a-f0-9]{6}$", v) and True,
                        "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                        "pid": lambda v: re.match("^[0-9]{9}$", v) and True,
                        "cid": lambda v: True
                        }
    passport_check = {"byr": False,
                      "iyr": False,
                      "eyr": False,
                      "hgt": False,
                      "hcl": False,
                      "ecl": False,
                      "pid": False,
                      "cid": True
                      }
    passport = copy(passport_check)

    with open("input.txt", "r") as fp:
        line = fp.readline()
        while line:
            splits=line.split(" ")
            if line == "\n":
                if all(v == True for v in passport.values()):
                    valid_passports += 1
                passport = copy(passport_check)
            else:
                for kv in splits:
                    kv_splits = kv.split(":")
                    k = kv_splits[0]
                    print(kv_splits[1])
                    passport[k] = passport_checker[k](kv_splits[1].strip())

            print(passport)
            line = fp.readline()

        if all(v == 1 for v in passport.values()):
            valid_passports += 1
        return valid_passports


print(run())
