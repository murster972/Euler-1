






start = 0
max_value = 10**5
step = 1000

cache = {}
running_total = 0

for i in range(start, max_value + 1):
  if i % 3 == 0 or i % 5 == 0:
    running_total += i
  if (i + 1) % step == 0:
    cache[i + 1] = running_total

print(cache)