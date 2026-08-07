import ast
def decremental(arr):
    s = arr[0]
    for i in range(1, len(arr)):
        if s[-1] == arr[i][0]:
            s += arr[i][1:]
        else:
            s += arr[i]
    print(len(s))
arr = ast.literal_eval(input())
decremental(arr)