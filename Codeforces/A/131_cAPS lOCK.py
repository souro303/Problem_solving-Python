s = input()

if s.isupper():
    print(s.lower())
elif s[0].islower() and s[1:].isupper():
    print(s.capitalize())
elif len(s) == 1 and s.islower():
    print(s.upper())
else:
    print(s)