import string

path = 'C:/Users/79656/AppData/Local/Programs/Python/Python313/LICENSE.txt'

with open(path, 'r') as f:
    text = f.read()

for s in string.punctuation:
    text = text.replace(s, ' ')

text = text.lower()
words = text.split()

c = {}

for w in words:
    if w in c:
        c[w] = c[w] + 1
    else:
        c[w] = 1

items = list(c.items())

def get_count(p):
    return p[1]

items.sort(key=get_count, reverse=True)

print("Самые частые слова:")
for w, count in items[:10]:
    print(w, "-", count)




# import string

# f = open('sem4(25.09.2026)\\LICENCE.txt', 'r', encoding='utf-8')
# text = f.read()
# f.close()

# for s in string.punctuation:
#     text = text.replace(s, ' ')

# text = text.lower()

# words = text.split()
 
# c = {}

# for w in words:
#     if w in c:
#         c[w] = c[w] + 1
#     else:
#         c[w] = 1

# items = list(c.items())

# def get_count(p):
#     return p[1]

# items.sort(key=get_count, reverse=True)

# print("самые частые слова")
# for w, count in items[:10]:
#     print(w, "-", count)
