# quest_gen.py

import random

def generate_question(level):
    """
    Gera uma pergunta matemática baseada no nível.
    Retorna: (texto_da_pergunta, resposta_correta)
    """
    if level < 3:
        # Nível fácil: adição ou subtração
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if random.choice([True, False]):
            return f"Quanto é {a} + {b}?", str(a + b)
        else:
            return f"Quanto é {a + b} - {a}?", str(b)
    elif level < 6:
        # Nível médio: multiplicação
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        return f"Quanto é {a} × {b}?", str(a * b)
    elif level < 9:
        # Nível difícil: divisão
        b = random.randint(2, 10)
        a = b * random.randint(2, 10)
        return f"Quanto é {a} ÷ {b}?", str(a // b)
    else:
        # Nível avançado: verdadeiro ou falso
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        op = random.choice(['+', '-', '*'])
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        else:
            result = a * b
        is_correct = random.choice([True, False])
        displayed_result = result if is_correct else result + random.randint(1, 5)
        return f"{a} {op} {b} = {displayed_result}? (s/n)", 's' if is_correct else 'n'