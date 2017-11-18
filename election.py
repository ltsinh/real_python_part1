from random import random

candidate_a_win = 0
candidate_b_win = 0

trials = 10000
for trial in range(0, trials):
    candidate_a = 0
    candidate_b = 0

    if random() < .87:
        candidate_a += 1
    else:
        candidate_b += 1

    if random() < .65:
        candidate_a += 1
    else: candidate_b += 1

    if random() < .17:
        candidate_a += 1
    else: candidate_b +=1

    if candidate_a > candidate_b:
        candidate_a_win += 1
    else:
        candidate_b_win += 1

print ("The probability that candidate A will win the election is:", candidate_a_win/trials)
print ("The probability that candidate B will win the election is:", candidate_b_win/trials)

