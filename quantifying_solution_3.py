








# 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
#
# TODO: work out upto 10^9, so that would be:
#   - 10000000000
#   - 1000000000
#   - 100000000
#   - 10000000
#   - 1000000
#   - 100000
#   - 10000
#   - 1000
#   - 100
#   - 10
#
# QUESTION: is there a pattern we can spot to convert between
#           each factor without needing to work them out
#           manually?
tens = lambda x: 5 + (x * 2)

# 10 25
# 20 45
# 30 65
# 40 85
# 50 105
# 60 125
# 70 145
# 80 165
# 90 185
#
# total for 10 < 100 is 945
#
# 100 2950
# 200 4950
# 300 6950
# 400 8950
# 500 10950
# 600 12950
# 700 14950
# 800 16950
# 900 18950
#
# needs confirm, but this seems to work for all hundred values:
#   950 + ((N*1000) * 2)
#
# logic was that total value for 10 to <100 is 945,
# we can see that all 100 values in 950, i.e. (945 + 5) = (950)
# then we can see the first digits in the 100 values are (N * 2)
# and then messed around and 1000 seems to scale it correctly.
#
# so we can use this to get the range from (N*100 to (N+1)*100)
# e.g. 500 to <600, 600 to <700, etc.
# then if we'd iterate over all values upto N, so if we wanted to
# find all values for 400 we'd use N=[1,2,3], we don't include 4
# as that would be 400 to <500.
#
# what's great about this is we that we only need to test 10 values
# here, 1-9, as after 999 we move onto the thousands method. This
# logic applies for every stage.
hundreds = lambda x: 950 + ((x * 2) * 1000)

# 1000 299500
# 2000 499500
# 3000 699500
# 4000 899500
# 5000 1099500
# 6000 1299500
# 7000 1499500
# 8000 1699500
# 9000 1899500
#
# same logic as the 100s, theres always a fixed value of 99500 at
# the end, and has a prefix of (N*2). Then we work out the factor
# to scale the prefix up, which is 100000, five 0s as the suffix
# is 5-chars long.
#
# so the value is 99500 + ((N*2) * 100000)
#
# 2000 499500
thousands = lambda x: 99500 + ((x*2) * 100000)

# so there is a pattern emerging here in the format
# of each formula:
#   prefix + (t * 2 * scale)
#
# where "t" is "the number at the start", e.g. 200=2,
# 500=5, 1000000000=1, etc.
#
# is there a pattern for the prefix and scale values?
# if we can work out the prefix we can work out the value
# of the scale as it's based on the size of the prefix.
#
# known prefix values:
#   10:       5
#   100:      950
#   1000:     99500
#   10000:    9995000
#   100000:   999950000
#   1000000:  99999500000
#   10000000: 9999995000000

#
# the number of 9s at the start are the same
# as the number of zeros in (N - 1), e.g.
# 10 has 1 and 1 9s, 1000 has 3 zeros and 2 9s
#
# the 5 is followed by a 9 and then as many
# zeros as there were 9s.
#
# yeah we can put this into a function to work out.
#
# how does this then translate to the scale? since times
# works for everything but the tens, we could have a special
# check, but don't like that.
#
# ahhhhhhhhhhhhhhh that's fucking it, we can use power
# of 10s. so the scale is 10**N, where N is the the number
# of chars in the prefix.
#   - 10 :  1 == 10**1 = 10
#   - 100 : 3 == 10**3 = 1000
#   - 1000 : 5 == 10**5 = 100000
#
# I mean we can also see it goes up by two each time so we could
# also just use that, but then we need to know the previous value.
#
# okay so lets try and writ a function to see if it works, and then
# we can test different all possible ranges from 10 to 10**9 against
# the know values in the loop.
#
# okay that didn't work as expected, lets take a step back and make
# sure this works as expected. so lets run through all:
#   - 10s: works as expected
#   - 100s: does not work for any values
#
# that's it working now, the issue was we were multiplying
# the scale by N instead of T (see formula in above notes).
#
# why is the loop taking so long to finish? I would have assumed
# the time would stay the same as we should only be iterating over
# 10 values each time? ah okay, using the formula it would be, but
# we're also testing the iteration way to compare against the formula.
#
# we can't test 10**9 as we run out of memory just iterating, don't
# feel like implementing a cache solution just for the tests. The fact
# that it works for all values from 10**1 to 10**8 (inclusive) I think
# we're safe to say it's good to go.
#
# NOTE: if our tests fail then come back here and confirm that 10**9
#       works as expected.
#
# It's also fucking instant, which is a very nice change of pace from
# the issues we had with caching.
#
# okay now we need todo the same thing for 3s and then put them together
#
# NOTE: when using this, remember it's only for values over 20,
#       we need to manually iterate any values before that, tbf
#       we could also cache them, but since it's so few values I
#       don't think it will make a difference.
def get_prefix(n):
  count = str(n).count("0") - 1
  nines = "9" * count
  zeros = "0" * count

  return f"{nines}5{zeros}"

def get_scale(pre):
  return 10**len(str(pre))

def formula(n, t):
  prefix = get_prefix(n)
  scale = get_scale(prefix)
  total = int(prefix) + (t * 2 * int(scale))

  return total

def test_formula():
  '''
    Test that our formula works for 10, 100, 1000, ..., 10**9
  '''
  failed = []

  for power in range(1, 9):
    step = 10**power

    print(f"Testing ({power}): {step}")

    for i in range(step, step * 10, step):
      end = i + step
      # values = [j for j in range(i, end) if j % 5 == 0]
      # total = sum(values)

      check = formula(step, i // step)
      print(i, check)

      # if total != check:
      #   failed.append((i, total, check))

  assert len(failed) == 0, failed

test_formula()