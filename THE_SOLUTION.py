





# there's an issue with the current approach,
# as although we can workout the sum of all
# values divisible by 3 and 5, it does not
# take into account that there are shared values
# across 3 and 5, and thus there will be duplicate
# values included in the final total.
#
# so, we need a way to determine the total number
# of values divisible by both 3 and 5 in a given
# range. Then we can subtract this from the total
# and it will remove the duplicate values.
#
# printing out all the values the first thing that
# we're seeing si that the shared values are in
# increments of 15, i.e. all values under 100 are:
#   15
#   30
#   45
#   60
#   75
#   90
#
# total values are:
#   under 100:  315
#   under 1000: 32850
#   under 10000: 3298500
#
# can we do the same thing as before, where we work
# out the values for 10s, 100s, 1000s, etc.?
#
# 15   = 15  = 15 x 1
# 30   = 45  = 15 x 3
# 45   = 90  = 15 x 5
# 60   = 150 = 15 x 10
# 75   = 225 = 15 x 15
# 90   = 315 = 15 x 21
# 105  = 420 = 15 x 28
#
# The sum is 15 x (the sum of all indices)
# E.g. 90 = 15 x (6+5+…+1) = 15 x 21
#
# So we want to find the sum of all number for (last value divisible by 15) / 15. So if N was 50, we’d use 45.
#
# There’s known formulas we can use, so the sum of all natural numbers upto N is:
# (N x (N + 1)) / 2
#
# So if we wanted to find the sum of all numbers divisible by 15 upto N we would do:
# multiple/m = n - (n % 15)
# index/i = m / 15
# Sum-of = (i x (i + 1)) / 2
# Total = 15 x sum-of
#
# Can we do the same thing for numbers divisible by 3 and 5?
#
# YES WE CAN!!!!!!!!!!
#
# had a wee off by one error, but that's sorted, and now we
# have a function to work out the sum of all values divisible
# by D upto N.

def sum_of_all_values(n, d):
  '''
    NOTE: n is inclusive within this function,
          so if you wanted to find <n pass
          in (n - 1)
  '''
  multiple = n - (n % d)
  multiplier = multiple // d
  sum_of = (multiplier * (multiplier + 1)) // 2
  total = d * sum_of

  return d * sum_of

def manual(n, d):
  return sum(i for i in range(n) if i % d == 0)

def test(d):
  '''
    we've tested 3, 5 and 15 upto 1000 and the function
    approach matches the manual approach
  '''
  for n in range(1000):
    # we need to pass in -1
    s = sum_of_all_values(n - 1, d)
    m = manual(n, d)

    assert m == s, (n, d)

def solution(n):
  end = n - 1
  threes = sum_of_all_values(end, 3)
  fives = sum_of_all_values(end, 5)
  fifteen = sum_of_all_values(end, 15)

  return threes + fives - fifteen

def main():
  t = int(input())

  for i in range(t):
    n = int(input())
    total = solution(n)
    print(int(total))

if __name__ == "__main__":
  main()