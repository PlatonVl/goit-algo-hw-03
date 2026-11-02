import random


def get_numbers_ticket(min, max, quantity):
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in (min, max, quantity)):
        return []

    if min < 1 or max > 1000 or min >= max:
        return []

    if quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)


print("Перевірка другого завдання:")

print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(10, 20, 5))
print(get_numbers_ticket(0, 49, 6))
print(get_numbers_ticket(1, 10, 15))
print(get_numbers_ticket(50, 20, 5))
print(get_numbers_ticket(1, 49, 0))
