# x, y = input().split()
# x = int(x)
# y = int(y)
# def evkld(A,B):
#     if A % B == 0:
#         return B
#     else:
#         c = A % B
#         a = B
#         b = c
#         return evkld(a, b) 
# print(evkld(x, y))
# standart evkld

#extended:
i, j = input().split()
i = int(i)
j = int(j)

def evkld(A,B):
    if B == 0: return A, 1, 0

    else:
        q = A // B
        d, x1, y1 = evkld(B, A % B)
        x = y1
        y = x1 - q * y1
        return d, x, y 
d, x, y  = evkld(i,j)
print(x, y, d)