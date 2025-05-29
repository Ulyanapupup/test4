import json
import os
import random

json_path = os.path.join('game_logic', 'questions_1_2.json')

with open(json_path, 'r', encoding='utf-8') as f:
    question_map = json.load(f)

questions_list = list(question_map.keys())
question_index = 0
possible_numbers = list(range(101))

def reset():
    global possible_numbers, question_index
    possible_numbers = list(range(101))
    question_index = 0

def is_even(n): return n % 2 == 0
def is_odd(n): return n % 2 == 1
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
def greater_than_50(n): return n > 50
def less_than_30(n): return n < 30

question_functions = {
    "is_even": is_even,
    "is_odd": is_odd,
    "is_prime": is_prime,
    "greater_than_50": greater_than_50,
    "less_than_30": less_than_30
}

def next_question():
    global question_index
    if question_index >= len(questions_list):
        return None
    q = questions_list[question_index]
    question_index += 1
    return q

def process_answer(user_answer):
    global possible_numbers
    last_q = questions_list[question_index - 1]
    func_name = question_map[last_q]
    func = question_functions[func_name]
    yes = user_answer.strip().lower() == "да"
    if yes:
        possible_numbers = [n for n in possible_numbers if func(n)]
    else:
        possible_numbers = [n for n in possible_numbers if not func(n)]

    if len(possible_numbers) == 1:
        return f"Я знаю! Это число {possible_numbers[0]}", True
    if len(possible_numbers) == 0:
        return "Упс, вы меня обманули 🙃", True

    q = next_question()
    if q:
        return q, False
    return "Вопросы закончились, я сдаюсь.", True
