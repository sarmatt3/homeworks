#1
class TwoVariables:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display(self):
        print(f"Переменная 1: {self.var1}, Переменная 2: {self.var2}")

    def update(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def sum(self):
        return self.var1 + self.var2

    def max_value(self):
        return max(self.var1, self.var2)

# Пример использования
obj = TwoVariables(5, 10)
obj.display()
print("Сумма:", obj.sum())
print("Максимальное значение:", obj.max_value())

obj.update(20, 15)
obj.display()
print("Сумма:", obj.sum())
print("Максимальное значение:", obj.max_value())

#2
class DecimalCounter:
    def __init__(self, min_value=0, max_value=10, current_value=0):
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = current_value

    def increment(self):
        if self.current_value < self.max_value:
            self.current_value += 1
        else:
            print("Достигнут максимум")

    def decrement(self):
        if self.current_value > self.min_value:
            self.current_value -= 1
        else:
            print("Достигнут минимум")

    @property
    def state(self):
        return self.current_value

# Пример использования
counter = DecimalCounter(0, 10, 5)
print("Текущее состояние:", counter.state)

counter.increment()
print("После увеличения:", counter.state)

counter.decrement()
print("После уменьшения:", counter.state)

counter.decrement()
counter.decrement()
counter.decrement()
counter.decrement()
print("После нескольких уменьшений:", counter.state)

#3

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients  # coefficients[0] + coefficients[1]*x + coefficients[2]*x^2 + ...

    def evaluate(self, x):
        return sum(coef * (x ** idx) for idx, coef in enumerate(self.coefficients))

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        padded_self = self.coefficients + [0] * (max_len - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_len - len(other.coefficients))
        return Polynomial([a + b for a, b in zip(padded_self, padded_other)])

    def __sub__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        padded_self = self.coefficients + [0] * (max_len - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_len - len(other.coefficients))
        return Polynomial([a - b for a, b in zip(padded_self, padded_other)])

    def __mul__(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result[i + j] += a * b
        return Polynomial(result)

    def __str__(self):
        return " + ".join(f"{coef}x^{idx}" for idx, coef in enumerate(self.coefficients) if coef != 0)

# Пример использования
p1 = Polynomial([1, 2, 3])  # 1 + 2x + 3x^2
p2 = Polynomial([3, 4, 5])  # 3 + 4x + 5x^2

print("Полином 1:", p1)
print("Полином 2:", p2)

p3 = p1 + p2
print("Сумма:", p3)

p4 = p1 - p2
print("Разность:", p4)

p5 = p1 * p2
print("Произведение:", p5)

print("Значение полинома 1 при x=2:", p1.evaluate(2))