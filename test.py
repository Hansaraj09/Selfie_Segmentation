lst = [237, 72, -18, 237, 236, 237, 60, -158, -273, -78, 492, 243]
min((abs(x), x) for x in lst)[1]

min(lst, key=abs)