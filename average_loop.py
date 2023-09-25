count = 0
sum = 0
print("Before", count, sum)
for value in [5, 10, 15, 20, 25]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)