import re

file = open("input_03.txt")

data = ""

for line in file:
    data += line.rstrip("\n")


def applyMul(chain):
    parsed = re.findall("mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)", chain)
    res = 0
    for mul in parsed:
        mul = mul.lstrip("mul(").rstrip(")").split(",")
        res += int(mul[0]) * int(mul[1])
    return res

def isDont(i, data):
    return data[i:i+7] == "don't()"
def isDo(i, data):
    return data[i:i+4] == "do()"

res = 0
i = 0
while i < len(data):
    j = i
    while not isDont(j, data) and j < len(data) - 7:
        j += 1
    res += applyMul(data[i:j+7])
    i = j + 7
    while not isDo(i, data) and i < len(data) - 4:
        i += 1

print("total mul : ", applyMul(data))
print("total mul v2 : ", res)