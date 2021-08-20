a = float(input('time in seconds:'))

h = int(a // 3600)
m = int((a % 3600) / 60)
s = int(a % 60)
print("{hours}:{minutes}:{seconds}".format(hours=h, minutes=m, seconds=s))


