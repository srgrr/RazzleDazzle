from numpy import random
import sys

game = {
  8:  lambda p, s: (p, s + p * 20),
  9:  lambda p, s: (p, s + p * 16),
  10: lambda p, s: (p, s + p * 10),
  11: lambda p, s: (p, s + p * 10),
  12: lambda p, s: (p, s + p * 10),
  13: lambda p, s: (p, s + p * 10),
  14: lambda p, s: (p, s + p * 3),
  15: lambda p, s: (p, s + p * 3),
  16: lambda p, s: (p, s + p * 2),
  17: lambda p, s: (p, s + p * 2),
  18: lambda p, s: (p, s // 2),
  19: lambda p, s: (p, s // 2),
  20: lambda p, s: (p, s),
  21: lambda p, s: (p, s),
  22: lambda p, s: (p, s),
  23: lambda p, s: (p, s),
  24: lambda p, s: (p, s),
  25: lambda p, s: (p, s),
  26: lambda p, s: (p, s),
  27: lambda p, s: (p, s),
  28: lambda p, s: (p, s),
  29: lambda p, s: (2 * p, s),
  30: lambda p, s: (p, s),
  31: lambda p, s: (p, s),
  32: lambda p, s: (p, s),
  33: lambda p, s: (p, s),
  34: lambda p, s: (p, s),
  35: lambda p, s: (p, s),
  36: lambda p, s: (p, s),
  37: lambda p, s: (p, s // 2),
  38: lambda p, s: (p, s // 2),
  39: lambda p, s: (p, s + p * 2),
  40: lambda p, s: (p, s + p * 2),
  41: lambda p, s: (p, s + p * 3),
  42: lambda p, s: (p, s + p * 3),
  43: lambda p, s: (p, s + p * 10),
  44: lambda p, s: (p, s + p * 10),
  45: lambda p, s: (p, s + p * 10),
  46: lambda p, s: (p, s + p * 16)
}

goal, roll = map(int, sys.argv[1:])

score, multiplier, money_spent = 0, 1, 0

while score < 2 * goal:
  money_spent += multiplier * roll
  dice_roll_sum = \
    sum(random.randint(1, 6) for _ in range(8))
  multiplier, score = \
    game[dice_roll_sum](multiplier, score)

print(f"You spent ${money_spent} before reaching {goal} points")
