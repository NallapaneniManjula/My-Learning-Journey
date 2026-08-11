n=int(input())
for i in range(n):
    parent,count=input().split()
    count=int(count)
    for j in range(count):
        child,value=input().split()
        print(parent + "." +child,value)