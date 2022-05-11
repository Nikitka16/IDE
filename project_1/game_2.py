"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # счетчик попыток
    min_meaning = 1 # нижняя граница множества
    max_meaning = 101 # верхняя граница множества
    predict_number = np.random.randint(min_meaning, max_meaning) # предполагаемое число из множества
    
    while True:  
        count += 1  
        if number == max_meaning: # производим проверку равенства по верхней границе
            break
        else:
            max_meaning -= 2  # корректируем верхнюю границу
            if number > max_meaning: 
                break
        if number == min_meaning: # производим проверку равенства по нижней границе
            break
        else:
            min_meaning += 2 # корректируем нижнюю границу
            if number < min_meaning:
                break        
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

    # RUN
if __name__ == '__main__':
    score_game(random_predict)