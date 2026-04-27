# Codewars 8kyu - Reverse a String
# Data: 2026-04-27
# Lógica: slicing com passo -1 percorre a string de trás para frente
# 'world'[::-1] → 'dlrow'
# 'word'[::-1] → 'drow'

def solution(string):
    return string[::-1]