s = input()
ans = ''

if int(s[0]) > 4 and int(s[0]) < 9:
    ans += str(9-int(s[0]))
else:
    ans += s[0]
    
for i in range(1, len(s)):
    if int(s[i]) > 4 and int(s[0]) <= 9:
        ans += str(9-int(s[i]))
    else:
        ans += s[i]

print(int(ans))


# s = input()
# ans = []

# first_digit = int(s[0])
# if first_digit > 4 and first_digit != 9:
#     ans.append(str(9 - first_digit))
# else:
#     ans.append(s[0])

# # Process the remaining digits
# for digit in s[1:]:
#     digit = int(digit)
#     if digit > 4:
#         ans.append(str(9 - digit))
#     else:
#         ans.append(str(digit))

# print(int(''.join(ans)))
