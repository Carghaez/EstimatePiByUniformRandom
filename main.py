# Estimate pi, given that you have a uniform random (0, 1)
# Dato un insieme di numeri generato casualmente, con una distribuzione uniforme tra 0 e 1, calcolare il Pi Greco
import random

def estimate_pi(n):
  num_point_circle = 0
  num_point_total = 0
  for _ in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    distance = x**2 + y**2
    if distance <= 1:
      num_point_circle += 1
    num_point_total += 1
  return 4 * (num_point_circle / num_point_total)
