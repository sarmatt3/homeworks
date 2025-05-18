import math

def f(x):
    return x**2

def integralSearch(func, a: int, b:int, n:int):
    h = (b - a)/n
    x0 = a
    s = 0
    for i in range(n):
        
        s += func(x0) * h
        x0 += h
    return s

def centreTriangle(func, a, b, n):
    h = (b - a)/n
    x0 = a
    x1 = x0 + h
    s=0
    for _ in range(n):
        s += func(((x1 + x0)/2))*h
        x0 = x1
        x1 += h
    return s

def squareMethod(func, a, b, n):
    h = (b-a)/n
    x0 = a
    s = 0
    x1 = x0 + h
    for i in range(n):
        s += func((x0 + x1 )/2)*(x1 - x0)
        x0 = x1
        x1 += h
    return s



print(f'Mетод триугольников {integralSearch(func=f, a = 0, b = 1, n = 1000)}')
print(f'Метод центрального треугольника {centreTriangle(f, 0, 1, 1000)}')
print(f"Метод прямоугольников {squareMethod(f, 0, 1, 1000)}")