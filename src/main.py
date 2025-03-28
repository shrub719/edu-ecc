from tinyec.ec import SubGroup, Curve
import matplotlib.pyplot as plt
import numpy as np

field = SubGroup(p=17, g=(15, 13), n=18, h=1)
curve = Curve(a=0, b=7, field=field, name="p1707")

print(curve)

x = []
y = []
p = curve.g
k = 1
while p.x:
    p = k * curve.g
    print(f"{k}G = ({p.x}, {p.y})")
    x.append(p.x)
    y.append(p.y)
    k += 1

plt.plot(x, y, "o")
plt.show()