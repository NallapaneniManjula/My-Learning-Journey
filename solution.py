s = input()
count = 0
for ch in s:
    if ch.isalpha():
        count += 1
print(count)