from itertools import zip_longest

a = ["64", "23", "314"]

for g in zip_longest(*a, fillvalue='0'):
    print(g)