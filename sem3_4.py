
def tr( size, symbol):
    for i in range(1, size + 1):
        if i <= (size+1)//2:
            print(symbol * i)
        else:
            print(symbol * ((size + 1) - i))
size, symbol = input().split()
size = int(size)
tr(size, symbol)