import numpy as np
import matplotlib.pyplot as plt

def analytical_solution(t):
    return 1 / (0.25 * t**2 + 0.875)

def f(t, y, alpha=1):
    return -alpha * t * y**2

def heun_step(t, y, h, alpha=1):
    k1 = f(t, y, alpha)
    k2 = f(t + 0.5 * h, y + 0.5 * h * k1, alpha)
    k3 = f(t + 0.75 * h, y + 0.75 * h * k2, alpha)
    return y + (2 * k1 + 3 * k2 + 4 * k3) * h / 9

def heun_method_adaptive(t0, y0, h, t_end, tol, alpha=1):
    t_values = [t0]
    y_values = [y0]

    while t_values[-1] < t_end:
        t_n = t_values[-1]
        y_n = y_values[-1]

        y_temp1 = heun_step(t_n, y_n, h, alpha)
        y_temp2 = heun_step(t_n, y_n, h / 2, alpha)
        y_temp2 = heun_step(t_n + h / 2, y_temp2, h / 2, alpha)

        error = abs(y_temp1 - y_temp2)

        if error < tol:
            t_values.append(t_n + h)
            y_values.append(y_temp1)
        else:
            h = h / 2
            continue

        h = h * (tol / error) ** 0.5

    return t_values, y_values

# Задані параметри
t0 = 1
y0 = 1
t_end = 4
h = 0.1
tol = 1e-4

# Виклик адаптивного методу Гюна
t_values, y_values = heun_method_adaptive(t0, y0, h, t_end, tol)

# Розрахунок аналітичного розв'язку
analytical_y_values = [analytical_solution(t) for t in t_values]

# Побудова графіків
plt.plot(t_values, y_values, 'o-', label="Approximate solution (Heun)")
plt.plot(t_values, analytical_y_values, 'r--', label="Analytical solution")
plt.xlabel('t')
plt.ylabel('y')
plt.title('Adaptive Heun method')
plt.legend()
plt.grid(True)
plt.show()
