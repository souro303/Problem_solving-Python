s = input()

oc = 0
for i in set(s):
    if s.count(i) % 2 != 0:
        oc += 1

print('First' if oc % 2!= 0 or oc == 0 else 'Second')