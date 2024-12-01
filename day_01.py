file = open("input_01.txt")

l1 = []
l2 = []

for line in file:
    data = line.rstrip("\n").split("   ")
    l1.append(int(data[0]))
    l2.append(int(data[1]))

# PART ONE

l1.sort()
l2.sort()

delta_sum = 0

for i in range(len(l1)):
    delta_sum += abs(l1[i] - l2[i])

print("delta sum : ", delta_sum)


# PART TWO

sim_score = 0

for a in l1:
    nb_found = 0

    for b in l2:
        if a == b:
            nb_found += 1

    sim_score += a * nb_found

print("similarity score : ", sim_score)    