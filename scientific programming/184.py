class list_divider(list):
    """
    Наследник list с операцией деления на натуральное число k:
    a / k -> list из k списков, отвечающих условиям задачи.
    """
    def __truediv__(self, other):
        # Тип делителя: целое, но не bool
        if not isinstance(other, int) or isinstance(other, bool):
            raise TypeError("Делитель должен быть целым числом (bool не допускается)")
        k = other
        # k должно быть натуральным (положительным)
        if k <= 0:
            raise ValueError("Делитель должен быть натуральным (k > 0)")

        n = len(self)
        # q = базовая длина, r = количество частей длиной q+1
        q, r = divmod(n, k)

        # размеры частей в невозрастающем порядке:
        # сначала r частей длиной q+1, затем (k-r) частей длиной q
        sizes = [q + 1] * r + [q] * (k - r)

        result = []
        idx = 0
        for sz in sizes:
            # Явно приводим к обычному list, чтобы возвращаемый объект был чистым list
            part = list(self[idx: idx + sz])
            result.append(part)
            idx += sz
        return result

a = list_divider([1, 2, 3, 4, 5, 6, 7])

print(a / 3)
print(a / 2)
print(a / 7)
# print(a / 0)
print(a / 2.5)