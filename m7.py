import numpy as np
import matplotlib.pyplot as plt

alpha = 1
beta = 1
t_start = alpha
t_end = alpha + 3
h = 0.1  # крок

def differential_equation(t, y):
    return -alpha * beta * t * y**2

def milne_simpson_method():
    t_values = [t_start]
    y_values = [beta]

    t = t_start
    y = beta

    while t < t_end:
        k1 = h * differential_equation(t, y)
        k2 = h * differential_equation(t + h / 2, y + k1 / 2)
        k3 = h * differential_equation(t + h / 2, y + k2 / 2)
        k4 = h * differential_equation(t + h, y + k3)

        y_next = y + (k1 + 4 * k2 + k3) / 6  # Метод Мілна-Сімпсона

        y = y_next  # Оновлення значення y
        t += h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

def analytical_solution(t):
    C = 1/beta - 2/alpha**2
    return 1 / (alpha * beta * t**2 / 2 - C)

# Побудова графіка для методу Мілна-Сімпсона та аналітичного розв'язку
milne_t, milne_y = milne_simpson_method()
analytical_y_milne = [analytical_solution(t) for t in milne_t]

plt.plot(milne_t, milne_y, label='Milne-Simpson Method')
plt.plot(milne_t, analytical_y_milne, label='Analytical Solution', linestyle='--')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('Comparison of Milne-Simpson Method and Analytical Solution')
plt.show()
