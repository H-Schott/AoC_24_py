file = open("input_02.txt")

def check(line):
    old_delta = line[0] - line[1]
    for i in range(len(line) - 1):
        delta = line[i] - line[i + 1]
        if (abs(delta) < 1 or abs(delta) > 3):
            return False
        if (delta * old_delta < 0):
            return False
        old_delta = delta
    return True


def new_check(line):
    if (check(line)): return True
    for i in range(len(line)):
        if (check(line[:i] + line[i+1:])): return True
    return False


nb_safe = 0
for line in file:
    data = line.rstrip("\n").split(" ")
    data_int = [int(i) for i in data]
    if (new_check(data_int)): nb_safe += 1


print("number of safe lines : ", nb_safe)