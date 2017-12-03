def parse_input():
    nums = []
    with open('input.txt', 'r') as f:
        for line in f:
            nums.append([int(x) for x in line.strip('\n').split('\t')])
    return nums

def calculate_checksum(nums):
    diffs = []
    for row in nums:
        diffs.append(max(row) - min(row))
    return sum(diffs)


print calculate_checksum(parse_input())

