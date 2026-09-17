num=1
for i in range(1,11):
    for j in range(i):
        print(num,end=' ')
        num+=1
    print()
    if num>10: 
       break