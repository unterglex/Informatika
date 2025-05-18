import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import random

def generate_data(a, b, c, x_min=0.1, x_max=5, points=100):
    x = np.linspace(x_min, x_max, points)
    y = a * x ** b + c + np.array([random.uniform(-3, 3) for _ in range(points)])
    return x, y

print("Введите коэффициенты для степенной регрессии y = a * x^b + c:")
true_a = float(input('a: '))
true_b = float(input('b: '))
true_c = float(input('c: '))

x, y = generate_data(true_a, true_b, true_c)

def predict(x, a, b, c):
    return a * x ** b + c

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def gradient(x, y, a, b, c):
    pred = predict(x, a, b, c)
    error = pred - y
    x_clipped = np.clip(x, 0.1, 10)
    a_clipped = max(a, 0.1)
    b_clipped = max(b, 0.1)
    da = (2 / len(x)) * np.dot(error, x_clipped ** b_clipped)
    db = (2 / len(x)) * np.dot(error, a_clipped * x_clipped ** b_clipped * np.log(x_clipped))
    dc = (2 / len(x)) * np.sum(error)
    return da, db, dc

def fit(x, y, speed=1e-5, epochs=100, a0=2, b0=2, c0=1):  # Меньше speed, лучше начальные значения
    a, b, c = a0, b0, c0
    a_list, b_list, c_list, mse_list = [a], [b], [c], [mse(y, predict(x, a, b, c))]
    for epoch in range(epochs):
        da, db, dc = gradient(x, y, a, b, c)
        if np.isnan(da) or np.isnan(db) or np.isnan(dc):
            print(f"NaN обнаружен на эпохе {epoch}. Остановка обучения.")
            break
        a = max(min(a - speed * da, 10), 0.1)
        b = max(min(b - speed * db, 5), 0.1)
        c -= speed * dc
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
        mse_list.append(mse(y, predict(x, a, b, c)))
    return a_list, b_list, c_list, mse_list

speed = 1e-5
epochs = 100
a0, b0, c0 = 2, 2, 1
a_list, b_list, c_list, mse_list = fit(x, y, speed, epochs, a0, b0, c0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
plt.subplots_adjust(bottom=0.25)

ax1.scatter(x, y, color='blue', label='Исходные данные')
line, = ax1.plot(x, predict(x, a0, b0, c0), color='red', label='Предсказание')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Степенная регрессия')
ax1.legend()
ax1.grid(True)

ax2.plot(range(len(mse_list)), mse_list, color='red')
ax2.set_xlabel('Эпоха')
ax2.set_ylabel('MSE')
ax2.set_title('Ошибка обучения')
ax2.grid(True)

ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Эпоха', 0, len(mse_list) - 1, valinit=0, valstep=1)

def update(val):
    epoch = int(slider.val)
    a = a_list[epoch]
    b = b_list[epoch]
    c = c_list[epoch]
    loss = mse_list[epoch]
    line.set_ydata(predict(x, a, b, c))
    ax1.set_title(f'Эпоха {epoch}: a={a:.3f}, b={b:.3f}, c={c:.3f}, MSE={loss:.3f}')
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()

final_a, final_b, final_c = a_list[-1], b_list[-1], c_list[-1]
print(f"\nФинальные коэффициенты: a = {final_a:.4f}, b = {final_b:.4f}, c = {final_c:.4f}")
print(f"Финальное MSE: {mse_list[-1]:.4f}")