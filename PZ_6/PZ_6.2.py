"""Дано число R и список размера N. Найти два различных элемента списка, сумма
которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
их индексов (определение наиболее близких чисел - то есть такой элемент AK, для
которого величина |AK - R| является минимальной)."""

R = 62
A = [1, 12, 43, 65, 18, 35, 44]


def find_closest_sum_pair(R, numbers):
    closest_sum = float()
    result_pair = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            current_sum = numbers[i] + numbers[j]
            if abs(current_sum - R) < abs(closest_sum - R):
                closest_sum = current_sum
                result_pair = [i, j]
    return result_pair


result = find_closest_sum_pair(R, A)
result.sort()
print(A)
print(f"Две ближайшие к числу {R} суммирующиеся числа (их индексы): {result}")