my_dict = {'a': 50, 'c': 5, 'd': 56, 'e': 4, 'f': 58, 'z': 1}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

count = 0
for key, value in sorted_dict.items():
    print(key, ':', value)
    count += 1
    if count == 3:
        break
