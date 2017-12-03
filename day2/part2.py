TEST_INPUT = [[5,9,2,8], [9,4,7,3], [3,8,6,5]]

def parse_input():
    to_sum = []
    with open('input.txt', 'r') as f:
        for line in f:
            to_sum.append(check_row([int(x) for x in line.strip('\n').split('\t')]))
    return sum(to_sum)


def check_row(row):
    divisible_vals = []
    row = sorted(row, reverse=True)
    for idx in range(len(row)):
        num1 = row[idx]
        for jdx in range(idx, len(row)):
            num2 = row[jdx]
            if num1 == num2:
                continue
            if not num1 % num2:
                return num1 / num2

"""
for row in TEST_INPUT:
    print check_row(row)
"""
print parse_input()
