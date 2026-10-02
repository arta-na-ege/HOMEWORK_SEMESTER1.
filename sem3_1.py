# n = int(input())


# def simple(N):
#     n = 2
#     a = []
#     while n <= N**0.5:
#         if N % n == 0:
#             N = N//n
#             a.append(n)
#         else: n +=1
#     return N, a
# print(simple(n))


# f(0)=1
# f(1)=1

# f(n) = f(n-1) + f(n-2)


n = int(input())

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        d = fib(n-1) + fib(n-2)
        return d
print(fib(n))



    