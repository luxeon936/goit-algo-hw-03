import turtle
import argparse

# Функція для рекурсивного малювання кривої Коха
def koch_curve(t, order, size):
    # Якщо рівень рекурсії 0, малюємо пряму лінію
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)  # Повертаємо на 60 градусів для створення першого кута
        koch_curve(t, order - 1, size / 3)
        t.right(120)  # Повертаємо на 120 градусів для створення другого кута
        koch_curve(t, order - 1, size / 3)
        t.left(60)  # Повертаємо назад на 60 градусів для завершення сегмента
        koch_curve(t, order - 1, size / 3)

# Функція для малювання сніжинки Коха на основі трьох кривих
def draw_koch_snowflake(order, size=300, color="blue"):
    window = turtle.Screen()  # Створюємо вікно для малювання
    window.bgcolor("white")  # Встановлюємо білий фон
    window.title("Сніжинка Коха")  # Встановлюємо заголовок вікна

    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.penup()
    t.goto(-size / 2, size / (2 * 3**0.5))
    t.pendown()

    # Малюємо три криві Коха, щоб сформувати сніжинку
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

# Функція для обробки аргументів командного рядка
def parse_arguments():
    parser = argparse.ArgumentParser(description="Створення фракталу «сніжинка Коха» з вказаним рівнем рекурсії.")
    # Додаємо аргумент для вказівки рівня рекурсії (обов'язковий)
    parser.add_argument('order', type=int, help="Рівень рекурсії (наприклад, 0, 1, 2, ...)")
    # Додаємо аргумент для розміру сніжинки (необов'язковий, за замовчуванням 300)
    parser.add_argument('--size', type=float, default=300, help="Розмір сніжинки (за замовчуванням 300)")
    # Додаємо аргумент для кольору сніжинки (необов'язковий, за замовчуванням синій)
    parser.add_argument('--color', type=str, default="blue", help="Колір сніжинки (за замовчуванням синій)")
    return parser.parse_args()  # Повертаємо аргументи, введені користувачем

# Основна функція, яка викликає всі інші функції
def main():
    args = parse_arguments()
    draw_koch_snowflake(args.order, args.size, args.color)

# Точка входу програми
if __name__ == "__main__":
    main()
