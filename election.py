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

"""

from random import random

total_A_wins = 0
total_B_wins = 0

trials = 100000
for trial in range(0, trials):
    A_win = 0
    B_win = 0
    if random() < .87:  # 1st region
        A_win += 1
    else:
        B_win += 1
    if random() < .65:  # 2nd region
        A_win += 1
    else:
        B_win += 1
    if random() < .17:  # 3rd region
        A_win += 1
    else:
        B_win += 1
    # determine overall election outcome
    if A_win > B_win:
        total_A_wins += 1
    else:
        total_B_wins += 1

print("Probability A wins:", total_A_wins / trials)
print("Probability B wins:", total_B_wins / trials)
"""
