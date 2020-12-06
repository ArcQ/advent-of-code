import sys
import requests

day = sys.argv[1]

response = requests.get("https://adventofcode.com/2020/day/" + day + "/input")
print(response.text)

f = open("./2020/" + day + ".txt", "w")
f.write(response.text)
f.close()

