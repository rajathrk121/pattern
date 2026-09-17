n=4

for i in range(n):
    for j in range(i+1):
        print(1 if i==0 else j%2,end=' ')
    print()