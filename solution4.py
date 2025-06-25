
print('Enter the numbers: ')
lst = list(map(int,input().split()))

d = {}
for i in range(1,10):
    d[i]=0

    for j in range(len(lst)):
        if lst[j]%i==0:
            d[i]+=1




print(d)
