
n = int(input('Enter number: '))

lst = [1]

if n%2==0:
    n = n-1

for i in range(n-1):
    lst.append(lst[-1]+2)


print(lst)