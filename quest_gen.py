# quest_gen.py

import random

def generate_question(level=1):
    if level <= 3:
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(['+', '-'])
    elif level <= 6:
        a, b = random.randint(100, 1000), random.randint(100, 1000)
        op = random.choice(['+', '-', '*', '/'])
    elif level <= 9:
        op = random.choice(['prime', 'even_odd', '+', '-', '*', '/'])
        if op == 'prime':
            a = random.randint(2, 100)
            question = f"O número {a} é primo? (s/n)"
            answer = 's' if is_prime(a) else 'n'
            return question, answer
        elif op == 'even_odd':
            a = random.randint(1, 100)
            question = f"O número {a} é par? (s/n)"
            answer = 's' if a % 2 == 0 else 'n'
            return question, answer
        else:
            a, b = random.randint(10, 500), random.randint(1, 50)
    else:
        a, b = random.randint(500, 2000), random.randint(1, 200)
        op = random.choice(['+', '-', '*', '/', 'prime', 'even_odd'])
        if op == 'prime':
            question = f"O número {a} é primo? (s/n)"
            answer = 's' if is_prime(a) else 'n'
            return question, answer
        elif op == 'even_odd':
            question = f"O número {a} é par? (s/n)"
            answer = 's' if a % 2 == 0 else 'n'
            return question, answer

    if op == '+':
        question = f"Quanto é {a} + {b}?"
        answer = a + b
    elif op == '-':
        question = f"Quanto é {a} - {b}?"
        answer = a - b
    elif op == '*':
        question = f"Quanto é {a} * {b}?"
        answer = a * b
    elif op == '/':
        a = a - (a % b)  # garantir divisão exata
        question = f"Quanto é {a} ÷ {b}?"
        answer = a // b

    return question, answer

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
