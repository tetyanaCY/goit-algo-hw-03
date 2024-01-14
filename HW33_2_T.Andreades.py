import turtle

def koch_snowflake(t, order, size):
    """
    Функція для малювання сніжинки Коха.

    Args:
    t (turtle.Turtle): Об'єкт Turtle для малювання.
    order (int): Рівень рекурсії.
    size (float): Довжина сторони сніжинки.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def draw_koch_snowflake(order, size=200):
    """
    Функція для створення візуалізації сніжинки Коха.

    Args:
    order (int): Рівень рекурсії.
    size (float): Довжина сторони сніжинки.
    """
    window = turtle.Screen()
    window.bgcolor("white")

    koch_turtle = turtle.Turtle()
    koch_turtle.speed(0)

    # Початкова позиція
    koch_turtle.penup()
    koch_turtle.goto(-size / 2, size / 3)
    koch_turtle.pendown()

    for _ in range(3):
        koch_snowflake(koch_turtle, order, size)
        koch_turtle.right(120)

    window.mainloop()

# Виклик функції з заданим рівнем рекурсії
# Використання високого рівня рекурсії може викликати сповільнення в роботі програми
draw_koch_snowflake(order=3)  # Наприклад, рівень рекурсії 3
