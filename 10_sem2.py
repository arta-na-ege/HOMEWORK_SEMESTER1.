with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

voc = set('аеёюяиыоуэАЕЁЮЯИЫОУЭ')
soglas = set('бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ')
res =[]

for i in range(len(text)):
    c = text[i]
    res. append(c)
    if c in voc and i>0 and text[i-1] in soglas:
# если в тексте есть только буквы, то можно заменить на: 
# if с in voc and i>0 and text[i-1] not in voc
# и соответственно можно вырезать строку 4(где задается множество soglas)


        res.append('с' + c)



print(''.join(res))


