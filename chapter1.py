a = int(input("Enter a number: "))

chet = 0
ne_chet = 0

while a > 0:
    if a % 2 == 0:
        chet += 1
    else:
        ne_chet += 1
    a = a // 10

print(f'Even: {chet}, Uneven: {ne_chet}')
