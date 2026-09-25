count = 0
ind = 0


with open('input.txt', 'r') as f:
    text = f.read()
for i in range(len(text)):
    if ((text[i] == '.' or text[i] == '?' or text[i] == '!') and (ind == 0)):
        count += 1
        ind = 1
    if ((ind == 1) and text[i] != '.' and text[i] != '?' and text[i] != '!'):
        ind = 0
print(count)