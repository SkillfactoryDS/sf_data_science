""""Игра угадай число.
Программа дожна угадать число от1 до 100 за минимальное количесво попыток (до 20)"""

import numpy as np
import random
random_number = random.randint(1, 101)

def game_core_v3(number:int=1)->int:
    """Рандомное угадывание загаданного числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 0
    begins = 1
    ends = 100
    
    while True:
        count+=1
        mid = (begins+ends)//2 # находим среднее число в имеющейся выборке
        if mid == random_number:
            print(f'Число {mid} было найдено за {count} попыток!')
            break  # выход из цикла, если число было угадано верно
        elif mid > random_number:
            ends = mid
        else:
            begins = mid
            
            
    return (count)



def score_game(game_core_v3)->int:
    """За какое количество попыток в среднем из 1000 подходов 
    алгоритм угадывает наш алгоритм задуманное число

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_1s=[]   # список для сохранения количества попыток
    np.random.seed(1)   # фиксируем сид для воспроизводимости
    random_array=np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_1s.append(game_core_v3(number))
    score=int(np.mean(count_1s))  # находим среднее количество попыток угадать число
    
    print(f'Ваш алгоритм угадывает число в среднем за : {score} попыток')
    return(score)

#RUN

if __name__ == "__main__": 
    score_game(game_core_v3)
    
    