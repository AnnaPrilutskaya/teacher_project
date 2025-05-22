import random

# Глобальная переменная для хранения текущей сложности
current_difficulty = 'first_class'  # значение по умолчанию

def set_difficulty(difficulty):
    """Устанавливает сложность для всех последующих примеров."""
    global current_difficulty # говорим: "используй глобальную переменную!"
    current_difficulty = difficulty # меняем её значение
    return current_difficulty  # Возвращаем установленную сложность


def generate_problem(difficulty='first_class'):
    """Генерирует пример и правильный ответ."""
    global current_difficulty
    print(f"Текущая сложность: {current_difficulty}")  # отладка
    
    if current_difficulty == 'first_class':
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(['+', '-'])
    elif current_difficulty == 'second_class':
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        operator = random.choice(['+', '-'])
    elif current_difficulty == 'third_class':
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        operator = random.choice(['+', '-', '*'])
    elif current_difficulty == 'forth_class':
        a = random.randint(10, 1000)
        b = random.randint(10, 1000)
        operator = random.choice(['*'])

    problem = f"{a} {operator} {b}"
    correct_answer = eval(problem)  
    return problem, correct_answer