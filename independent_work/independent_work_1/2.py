import math

t = 1
x = 3

z = ((9 * math.pi * t + 10 * math.cos(x)) /
     (math.sqrt(t) - abs(math.sin(t)))) * math.exp(x)

print(z)

