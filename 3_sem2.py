s = input().strip()

m = str.maketrans('AHIMOTUVWXY18E3JL2SZ5', 'AHIMOTUVWXY183ELJ5S2Z')
pal = s == s[::-1]
ms =  set(s) <= set('AHIMOTUVWXY18E3JL2SZ5') and s == s[::-1].translate(m)
print(f"{s} is {'not palindrome' if not pal and not ms else 'Palindrome' if pal and not ms else 'Mirror string' if not pal and ms else 'Mirror palindrome'}.")