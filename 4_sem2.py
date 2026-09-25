#a = list(input().split())
#for i in range(0, len(a)-1, 2): a[i], a[i+1] = a[i+1], a[i]
#print(*a)
#Solvation:
a = input().split()

a[0:-1:2],a[1::2] = a[1::2],a[0:-1:2] #для того чтобы у второго среза была та же длина, что у 1 

print(*a)