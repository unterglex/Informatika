import numpy as np
import matplotlib.pyplot as plt

def generate_function():
    # Функция f(x) = x^2 + e^{-x} (имеет минимум)
    func = lambda x: x ** 2 + np.exp(-x)
    # Производная f'(x) = 2x - e^{-x}
    diff_func = lambda x: 2 * x - np.exp(-x)
    return func, diff_func

def gradientDescend(func=lambda x: x ** 2,
                    diffFunc=lambda x: 2 * x,
                    x0=3,
                    speed=0.01,
                    epochs=100):
    x_list = [x0]
    y_list = [func(x0)]
    for _ in range(epochs):
        x_new = x_list[-1] - speed * diffFunc(x_list[-1])
        x_list.append(x_new)
        y_list.append(func(x_new))
    return x_list, y_list

def plot_results(func, x_list, y_list):
    x_min = min(min(x_list) - 2, -5)
    x_max = max(max(x_list) + 2, 5)
    x_values = np.linspace(x_min, x_max, 400)
    y_values = [func(x) for x in x_values]

    plt.figure(figsize=(12, 6))
    plt.plot(x_values, y_values, label='f(x)', color='blue')
    plt.scatter(x_list, y_list, color='red', label='Градиентный спуск', s=20)
    plt.title('Метод градиентного спуска')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    func, diffFunc = generate_function()
    x_list, y_list = gradientDescend(
        func=func,
        diffFunc=diffFunc,
        x0=3,
        speed=0.1,
        epochs=100)
    print(f"Начальная точка: x0 = {x_list[0]}")
    print(f"Последнее значение: x = {x_list[-1]:.6f}, f(x) = {y_list[-1]:.6f}")

    plot_results(func, x_list, y_list)

    test_speeds = [0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
    print("\nТестирование разных значений скорости:")
    for speed in test_speeds:
        x_list, y_list = gradientDescend(
            func=func,
            diffFunc=diffFunc,
            x0=3,
            speed=speed,
            epochs=50)
        print(f"speed={speed:.2f}: конечное x={x_list[-1]:.4f}, f(x)={y_list[-1]:.4f}")