import re

fname = "numbers.txt"
fh = open(fname)
sum = 0
count = 0
for line in fh:
    f = re.findall('[0-9]+',line)
    for num in f:
        count +=1
        sum = sum+(int(num))
print("There are", count, "values with a sum of", sum)