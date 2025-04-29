t = int(input())
for m in range(t):
    s = input()
    
    n = len(s)
    zeros = s.count('0')
    ones = n - zeros

    for i in s:
        if i == '0' and ones > 0:
            ones -= 1
        elif i == '1' and zeros > 0:
            zeros -= 1
        else:
            break
    
    print(zeros + ones)
