list1 = [1, 2, 2, 3, 4, 5]
list2 = [4, 5, 5, 6, 7, 8]

A = set(list1)
B = set(list2)

print("Первый список:", sorted(A))
print("Второй список:", sorted(B))
print()

print(" A ^ B:")
print(sorted(A ^ B))
print()

print("Уникальные для первого (A - B):")
print(sorted(A - B))

print("Уникальные для второго (B - A):")
print(sorted(B - A))
print()

print("Уникальные для (A | B):")
print(sorted(A | B))
print()

print("В обоих списках (A & B):")
print(sorted(A & B))