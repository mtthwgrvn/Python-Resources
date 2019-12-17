import re

count = 0
total = 0
hand = open('regex_sum_221009.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        line.append(x)
        final = (sum(line))

print(final)
