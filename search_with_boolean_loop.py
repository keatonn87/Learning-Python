found = False
print("Before", found)
for value in [5, 10, 15, 20, 25]:
    if value == 15:
        found = True
    print(found, value)
print("After", found)