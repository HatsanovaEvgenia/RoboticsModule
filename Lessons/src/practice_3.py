import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Arc

# Определяем символы
theta_i, alpha_i, a_i, d_i = sp.symbols('theta_i alpha_i a_i d_i')
q1, q2, q3, l1, l2, l3, x, y, z = sp.symbols('q1 q2 q3 l1 l2 l3 x y z')
L1, L2, L3 = 1.0, 0.8, 0.6 


# Задаем матрицу
A = sp.Matrix([
    [sp.cos(theta_i), -sp.sin(theta_i)*sp.cos(alpha_i),  sp.sin(theta_i)*sp.sin(alpha_i), a_i*sp.cos(theta_i)],
    [sp.sin(theta_i),  sp.cos(theta_i)*sp.cos(alpha_i), -sp.cos(theta_i)*sp.sin(alpha_i), a_i*sp.sin(theta_i)],
    [0,               sp.sin(alpha_i),                  sp.cos(alpha_i),                 d_i],
    [0,               0,                                0,                               1]
])

# Вывод
# sp.pretty_print(A)  # красивый вид

# Подставляем значения для первой матрицы
subs_dict_1 = {
    theta_i: q1,
    alpha_i: sp.pi/2,
    a_i: 0,
    d_i: l1
}
A_1 = A.subs(subs_dict_1)

# Подставляем значения для второй матрицы
subs_dict_2 = {
    theta_i: q2, 
    alpha_i: 0,
    a_i: l2,
    d_i: 0
}
A_2 = A.subs(subs_dict_2)

# Подставляем значения для третьей матрицы
subs_dict_3 = {
    theta_i: q3,
    alpha_i: 0,
    a_i: l3,
    d_i: 0
}
A_3 = A.subs(subs_dict_3)

# Упрощаем
A_simplified_1 = sp.simplify(A_1)
A_simplified_2 = sp.simplify(A_2)
A_simplified_3 = sp.simplify(A_3)

# Выводим результат
sp.pretty_print(A_simplified_1)
sp.pretty_print(A_simplified_2)
sp.pretty_print(A_simplified_3)

T = A_simplified_1 * A_simplified_2 * A_simplified_3
# Упрощаем
T_simplified = sp.simplify(T)

# Выводим результат
sp.pretty_print(T_simplified)

coord = T[:, -1]

x == coord[0]
y == coord[1]
z == coord[2]