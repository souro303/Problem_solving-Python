t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    if not s:
        print(0)
        continue
    transitions = 0
    prev = s[0]
    for c in s[1:]:
        if c != prev:
            transitions += 1
            prev = c
    if s[0] == '1':
        transitions += 1
    print(transitions)