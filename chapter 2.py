a = str(input("Enter a string: "))
length = len(a)
lower = 0
upper = 0

for i in range(1, length):
    if a[i - 1].islower() and a[i].islower():
        lower += 1
    elif a[i - 1].isupper() and a[i].isupper():
        upper += 1

print('Amounts letters in the ', a, ' : ', length)
print('Lower register in pair: ', lower)
print('Upper register in pair: ', upper)
