

# TODO: now we need to work out a formula for 3s
#
# you know what todo, work out some manual values
# and then try to spot patterns.





step = 10

for i in range(step, step * 10, step):
  end = i + step
  values = [j for j in range(i, end) if j % 3 == 0]
  total = sum(values)

  print(i, end, total)