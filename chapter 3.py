c = [2, -5, 8, 10, -2, 19, -23, -1, -10, -20, -2]
answer = 1

for i in c:
    if i < 0:
        answer *= i

print(answer)
