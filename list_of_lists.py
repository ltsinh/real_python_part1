universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500],
    ]

def enrollment_stats(universities):

    enrollment_total = []
    tuition_total = []

    for amount in universities:
        enrollment_total.append(amount[1])
        tuition_total.append(amount[2])

    return enrollment_total, tuition_total

print(enrollment_stats(universities))

"""
def mean(list):
    if len(list) == 0:
        return "There is no information in this list."

    list_summation = 0
    for i in range(len(list)):
        list_summation += int(list[i])
    return int(list_summation / len (list)
               
"""

def mean(list):

    if len(list) == 0:
        return "There is no information in this list."

    length = len(list)
    list_summation = 0

    for i in range(length):
        list_summation += int(list[i])

    list_summation = sum(list)
    average = int(list_summation / length)
    return average


def median(list):
    list_sorted = sorted(list)
    length = len(list_sorted)
    if not length % 2:
        list_amt = list_sorted[int(length / 2)] + list_sorted[int(length / 2 - 1)] / 2.0
        return list_amt
    average = list_sorted[int(length / 2)]
    return average



totals = enrollment_stats(universities)
print("\n")
print("*****" * 5)
print("Total students:   {}".format(sum(totals[0])))
print("Total tuition:  $ {}".format(sum(totals[1])))
print("\nStudent mean:     {}".format(mean(totals[0])))
print("Student median:   {}".format(median(totals[0])))
print("\nTuition mean:   $ {}".format(mean(totals[1])))
print("Tuition median: $ {}".format(median(totals[1])))
print("*****" * 5)
print("\n")
