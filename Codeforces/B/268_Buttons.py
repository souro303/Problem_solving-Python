n = int(input())

total_presses = 0

for i in range(0, n):
    total_presses += (i+1)*(n-i)-i

print(total_presses)