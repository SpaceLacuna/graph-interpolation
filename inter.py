import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


class AverageValue:

    def __init__(self, data):
        self.data = data

    def give_average(self):
        amount = 0
        quantity = 0
        for i in self.data:
            amount += i
            quantity += 1

        result = round(float(amount / quantity), 2)
        print("Average number is", result)


file_name = input("Please, enter file name as file_name.txt: ")

with open(file_name) as file:
    y = [float(i) for i in file.readlines()]

x = []
a = 0
for i in y:
    a += 1
    x.append(a)

a = AverageValue(y)
a.give_average()

y_max = max(y)
y_min = min(y)
i_max = y.index(y_max)
i_min = y.index(y_min)
x_max = x[i_max]
x_min = x[i_min]

print("Max value:", y_max)
print("Min value:", y_min)

x_np = np.array(x)
x_new = np.linspace(x_np.min(), x_np.max(), 501)
spl = make_interp_spline(x_np, y)
y_new = spl(x_new)

plt.plot(x, y, color="green", label="line")
plt.plot(x_new, y_new, "--", color="black", label="interpolated")
plt.plot(x_max, y_max, "o", color="red", label="max")
plt.plot(x_min, y_min, "o", color="blue", label="min")

plt.grid()
plt.title("Some function", fontsize=14)
plt.legend(title="Legend")
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.show()
