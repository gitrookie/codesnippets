import json

with open("logconf1.json", "r") as fp:
    jd = json.load(fp)

print(jd)
