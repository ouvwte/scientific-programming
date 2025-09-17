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
