import math
import itertools

class Summinator:
  def __init__(self):
    self.last_value = ()

    self.sorted_values = []
    self.sums = {}
    self.indices = {}

  def sort_input(self):
    for j in range(int(input())):
      n = int(input())
      self.indices[j] = n

    self.sorted_values = sorted(self.indices.values())

  def print_sums(self):
    for i in range(len(self.indices)):
      key = self.indices[i]
      print(self.sums[key])

  def summinate(self):
    for i in self.sorted_values:
      starting_value, start = self.get_start()
      total = self.find_sum(starting_value, start, i)

      self.last_value = (total, i)
      self.sums[i] = total

  def get_start(self):
    return (0, 0) if not self.last_value else self.last_value

  def get_next_divisible(self, a, b):
    return math.ceil(a / b)

  def find_sum(self, starting_value, start, end):
    running_total = starting_value

    starting_three = self.get_next_divisible(start, 3)
    starting_five = self.get_next_divisible(start, 5)

    for i, j in itertools.zip_longest(range(starting_three, end, 3), range(starting_five, end, 5)):
      running_total += i

      if j and j % 3 != 0:
        running_total += j

    # for i in range(start, end):
    #   if i % 3 == 0 or i % 5 == 0:
    #     running_total += i

    return running_total

def main():
  s = Summinator()
  s.sort_input()
  s.summinate()
  s.print_sums()

if __name__ == "__main__":
  main()
