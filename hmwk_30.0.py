import time


def decoration(func):
    def wrapper(*args, **kwargs):
        started_at = time.time()

        result_of_func = func(*args, **kwargs)

        ended_at = time.time()
        end_at = round(ended_at - started_at, 1)
        k = 0
        for i in range(2, result_of_func // 2 + 1):
            if (result_of_func % i == 0):
                k = k + 1
        if k <= 0:
            return f"Простое число - {result_of_func} - было потрачено времени: {end_at}"
        else:
            return f"Составное число - {result_of_func} - было потрачено времени: {end_at}"

    return wrapper


@decoration
def sum_three(*args):
    summ = 0
    for i in args:
        summ = summ + i
    return summ


result = sum_three(4, 5, 6)
print(result)
