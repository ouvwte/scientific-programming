class list_divider(list):
    def __truediv__(self, other):
        if not isinstance(other, int):
            raise TypeError("Делитель должен быть целым числом")
        n = len(self)
        k = other
        if k <= 0 or k > n:
            raise ValueError("Деление невозможно")
        
        q, r = divmod(n, k)
        # первые r списков будут длиной q+1, остальные длиной q
        sizes = [q + 1] * r + [q] * (k - r)
        
        # упорядочиваем по невозрастанию (и так уже отсортировано)
        result = []
        idx = 0
        for size in sizes:
            result.append(self[idx: idx + size])
            idx += size
        return result

a = list_divider([1, 2, 3, 4, 5, 6, 7])

print(a / 3)
print(a / 2)
print(a / 7)
# print(a / 0)
print(a / 2.5)