n = int(input())
result = {}
for _ in range(n):
    m = int(input())
    for i in range(m):
        key, value = input().split()
        value = int(value)
        result[key] = result.get(key, 0) + value
for key, value in result.items():
    print(key, value)