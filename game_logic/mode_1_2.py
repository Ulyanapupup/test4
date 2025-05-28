# game_logic/mode_1_2.py
import json
import os

json_path = os.path.join('game_logic', 'questions_1_2.json')

with open(json_path, 'r', encoding='utf-8') as f:
    question_map = json.load(f)

possible_numbers = list(range(101))

def reset():
    global possible_numbers
    possible_numbers = list(range(101))

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

def filter_numbers(keyword, answer_yes):
    global possible_numbers
    func_name = question_map.get(keyword)
    if not func_name:
        return
    func = question_functions.get(func_name)
    if not func:
        return
    if answer_yes:
        possible_numbers = [n for n in possible_numbers if func(n)]
    else:
        possible_numbers = [n for n in possible_numbers if not func(n)]

def get_possible_numbers():
    return possible_numbers
