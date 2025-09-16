class score_filter:
    def __init__(self, min_score: float, max_score: float):
        self.min_score = min_score
        self.max_score = max_score
        self.cum_x = None
        self.cum_y = None
        self.total_matrix_sum = None

    def fit(self, x: list, y: list, pairs):
        n = len(x)
        m = len(y)
        self.cum_x = [0] * (n + 1)
        for i in range(n):
            self.cum_x[i + 1] = self.cum_x[i] + x[i]

        self.cum_y = [0] * (m + 1)
        for j in range(m):
            self.cum_y[j + 1] = self.cum_y[j] + y[j]

        total_x_sum = self.cum_x[len(x)] 
        total_y_sum = self.cum_y[len(y)]
        self.total_matrix_sum = total_x_sum * total_y_sum
        
        self.pairs_to_process = list(pairs)
        return self

    def __iter__(self):
        for i, j in self.pairs_to_process:
            sum_sub = self.cum_x[i + 1] * self.cum_y[j + 1]
            fraction = sum_sub / self.total_matrix_sum

            if self.min_score < fraction < self.max_score:
                yield (i, j)