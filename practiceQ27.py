"""
You are given a complex . Your task is to convert it to polar coordinates."""

import math

z = input()
c = complex(z)

x = c.real
y = c.imag

r = math.hypot(x, y)
theta = math.atan2(y, x)

print(r)
print(theta)