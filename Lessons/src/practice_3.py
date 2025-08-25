import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

L1, L2, L3 = 1.0, 0.8, 0.6 

y = 0.7
x = 0.9
z = 1.2

fig = plt.figure(figsize=(10, 5))

# Создаем окна
ax1 = fig.add_subplot(1, 2, 1)
ax3 = fig.add_subplot(1, 2, 2)

# Рисуем желаемую точку манипулятора
circle = Circle((x, z), radius=0.1, facecolor='red', edgecolor='r', linewidth=1)
ax1.add_patch(circle)

circle = Circle((x, y), radius=0.05, facecolor='red', edgecolor='r', linewidth=1)
ax3.add_patch(circle)

ax1.set_title("xz")
ax1.set_aspect("equal")

ax3.set_title("xy")
ax3.set_aspect("equal")

# Наведем красоту.
ax1.set_ylim(-1, 4.5)
ax3.set_ylim(-0.5, 2)
ax1.set_xlim(-0.5, 1.5)
ax3.set_xlim(-0.5, 1.5)

plt.show()

q_1 = np.atan2(y, x)
CO = ((z - L1)**2 + x**2 + y**2 - L2**2 -L3**2)/(2*L2*L3)
q_3 = np.atan2(np.sqrt(1-(CO)**2), CO)

s = z-L1
rho = np.sqrt( x**2 + y**2 )
q_2 = np.atan2(s, rho) - np.atan2((L3*np.sin(q_3)), (L2 + L3*np.cos(q_3)))

print(q_1, q_2, q_3)


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

T = A_simplified_1 * A_simplified_2 * A_simplified_3
# Упрощаем
T_simplified = sp.simplify(T)


subs_dict = {
    q1: q_1, 
    q2: q_2,
    q3: q_3,
    l1: L1, 
    l2: L2,
    l3: L3
}

fig = plt.figure(figsize=(10, 5))

# Создаем окна
ax1 = fig.add_subplot(1, 2, 1)
ax3 = fig.add_subplot(1, 2, 2)

# Рисуем основание манипулятора
X = [0, 0.3, -0.3, 0]  
Y = [0, -0.6, -0.6, 0]
ax1.plot(X, Y, 'y-')
circle = Circle((0, 0), radius=0.3, facecolor='white', edgecolor='y', linewidth=1)
ax3.add_patch(circle)

# Рисуем желаемую точку манипулятора
circle = Circle((x, z), radius=0.1, facecolor='red', edgecolor='r', linewidth=1)
ax1.add_patch(circle)
circle = Circle((x, y), radius=0.05, facecolor='red', edgecolor='r', linewidth=1)
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
ax3.plot([x_2, x_3], [y_2, y_3], 'g-', label='3')

# Наведем красоту.
ax1.set_title("xz")
ax1.set_aspect("equal")

ax3.set_title("xy")
ax3.set_aspect("equal")


ax1.set_ylim(-1, 4.5)
ax3.set_ylim(-0.5, 2)
ax1.set_xlim(-0.5, 1.5)
ax3.set_xlim(-0.5, 1.5)

plt.show()