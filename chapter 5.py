a = (-1, 2, 3, 4)
answer = 0
index = 0
for i in range(1, len(a)):
    if a[i] > 0:
        index = i + 1
        break
for i in range(index, len(a)):
    answer += a[i]
print(answer)
