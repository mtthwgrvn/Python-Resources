fname = input('Enter file name: ')
count = 0
fh = open(fname)

for line in fh:
    line = line.rstrip()
    if line == "": continue

    words = line.split()
    if words[0] != "From" : continue

    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
