# Codewars 8kyu - Odd or Even
# Data: 2026-04-27

def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"