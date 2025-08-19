import sympy as sp

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Arc

# Определяем символы
theta_i, alpha_i, a_i, d_i = sp.symbols('theta_i alpha_i a_i d_i')
q1, q2, q3, l1, l2, l3 = sp.symbols('q1 q2 q3 l1 l2 l3')
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

#________________________________________________________________________________________
L1, L2, L3 = 1.0, 0.8, 0.6  # длины звеньев (задаем произвольно, но так, чтоб выглядело реалистично)

# Зафиксируем первое звено, чтоб визуализировать на плоскости.
Q1 = np.deg2rad(20)
Q2 = np.deg2rad(15)
Q3 = np.deg2rad(30)

subs_dict = {
    q1: Q1, 
    q2: Q2,
    q3: Q3,
    l1: L1, 
    l2: L2,
    l3: L3
}


fig = plt.figure(figsize=(10, 5))

# Создаем окна
ax1 = fig.add_subplot(1, 2, 1)
#ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 2, 2)

# Рисуем основание манипулятора
x = [0, 0.3, -0.3, 0]  
y = [0, -0.6, -0.6, 0]
ax1.plot(x, y, 'y-')
#ax2.plot(x, y, 'y-')
circle = Circle((0, 0), radius=0.3, facecolor='white', edgecolor='y', linewidth=1)
ax3.add_patch(circle)

# Рисуем первое звено
# Для этого берем последний столбец матрицы A1 и значения по осям


coord_1 = A_simplified_1[:, -1]

x_1_r = coord_1[0]
y_1_r = coord_1[1]
z_1_r = coord_1[2]

x_1 = float(x_1_r.subs(subs_dict))
y_1 = float(y_1_r.subs(subs_dict))
z_1 = float(z_1_r.subs(subs_dict))

ax1.plot([0, x_1], [0, z_1], 'b-', label='1')
#ax2.plot([0, y_1], [0, z_1], 'b-', label='1')
circle = Circle((x_1, y_1), radius=0.01, facecolor='white', edgecolor='b', linewidth=1)
ax3.add_patch(circle)


# Рисуем второе звено
# Для этого берем последний столбец матрицы A1*A2 и значения по оси z0 и y0
B =  A_simplified_1 * A_simplified_2
coord_2 = B[:, -1]

x_2_r = coord_2[0]
y_2_r = coord_2[1]
z_2_r = coord_2[2]

x_2 = float(x_2_r.subs(subs_dict))
y_2 = float(y_2_r.subs(subs_dict))
z_2 = float(z_2_r.subs(subs_dict))

ax1.plot([x_1, x_2], [z_1, z_2], 'r-', label='2')
#ax2.plot([y_1, y_2], [z_1, z_2], 'r-', label='2')
ax3.plot([x_1, x_2], [y_1, y_2], 'r-', label='2')

# Рисуем третье звено
# Для этого берем последний столбец матрицы T и значения по оси z0 и y0
coord_3 = T[:, -1]

x_3_r = coord_3[0]
y_3_r = coord_3[1]
z_3_r = coord_3[2]

x_3 = float(x_3_r.subs(subs_dict))
y_3 = float(y_3_r.subs(subs_dict))
z_3 = float(z_3_r.subs(subs_dict))

ax1.plot([x_2, x_3], [z_2, z_3], 'g-', label='3')
#ax2.plot([y_2, y_3], [z_2, z_3], 'g-', label='3')
ax3.plot([x_2, x_3], [y_2, y_3], 'g-', label='3')


ax1.set_title("zx")
ax1.set_aspect("equal")

#ax2.set_title("zy")
#ax2.set_aspect("equal")

ax3.set_title("xy")
ax3.set_aspect("equal")

ax1.set_xlim(-0.5, 1.5)
ax3.set_xlim(-0.5, 1.5)


dx = x_2 - x_1
dz = z_2 - z_1

# продлеваем линию за вторую точку
factor = 1.5  # во сколько раз удлинить
x_ext = x_2 + dx * factor
z_ext = z_2 + dz * factor

ax1.plot([x_2, x_ext], [z_2, z_ext], color='gray', linewidth=0.8, linestyle='--')  # пунктиром

ax1.axhline(z_1, color='gray', linewidth=0.8, linestyle='--')
ax1.axvline(0, color='gray', linewidth=0.8, linestyle='--')

ax3.axhline(0, color='gray', linewidth=0.8, linestyle='--')




center = (0, 0)      # центр
radius = 0.6         # радиус
start_angle = 0     # начальный угол (градусы)
end_angle = np.rad2deg(Q1)      # конечный угол (градусы)

# создаём дугу
arc = Arc(center, width=2*radius, height=2*radius,
          angle=0, theta1=start_angle, theta2=end_angle,
          color="blue", linewidth=2)

ax3.add_patch(arc)
# добавляем подпись
mid_angle = np.deg2rad((start_angle + end_angle) / 2)  # в радианы
x_text = center[0] + (radius + 0.1) * np.cos(mid_angle)  # чуть дальше радиуса
y_text = center[1] + (radius + 0.1) * np.sin(mid_angle)

ax3.text(x_text, y_text, "q1", fontsize=12, color="b")
#___________________________________________________________________________
center_2 = (x_1, z_1)      # центр
radius_2 = 0.6         # радиус
start_angle_2 = 0     # начальный угол (градусы)
end_angle_2 = np.rad2deg(Q2)      # конечный угол (градусы)

# создаём дугу
arc = Arc(center_2, width=2*radius_2, height=2*radius_2,
          angle=0, theta1=start_angle_2, theta2=end_angle_2,
          color="r", linewidth=2)

ax1.add_patch(arc)
# добавляем подпись
mid_angle_2 = np.deg2rad((start_angle_2 + end_angle_2) / 2)  # в радианы
x_text_2 = center_2[0] + (radius_2 + 0.1) * np.cos(mid_angle_2)  # чуть дальше радиуса
y_text_2 = center_2[1] + (radius_2 + 0.1) * np.sin(mid_angle_2)

ax1.text(x_text_2, y_text_2, "q2", fontsize=12, color="r")

#___________________________________________________________________________
center_3 = (x_2, z_2)      # центр
radius_3 = 0.4         # радиус
start_angle_3 = np.rad2deg(Q2)     # начальный угол (градусы)
end_angle_3 = np.rad2deg(Q2+Q3)      # конечный угол (градусы)

# создаём дугу
arc_2 = Arc(center_3, width=2*radius_3, height=2*radius_3,
          angle=0, theta1=start_angle_3, theta2=end_angle_3,
          color="g", linewidth=2)

ax1.add_patch(arc_2)
# добавляем подпись
mid_angle_3 = np.deg2rad((start_angle_3 + end_angle_3) / 2)  # в радианы
x_text_3 = center_3[0] + (radius_3 + 0.1) * np.cos(mid_angle_3)  # чуть дальше радиуса
y_text_3 = center_3[1] + (radius_3 + 0.1) * np.sin(mid_angle_3)

ax1.text(x_text_3, y_text_3, "q3", fontsize=12, color="g")

plt.show()