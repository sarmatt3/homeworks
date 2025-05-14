import tkinter as tk
window = tk.Tk()
window.geometry('1000x1000')
canv = tk.Canvas(width=1000, height=1000) 
centerX = 500
centerY = 500
shift = 20
scale = 10

'''
1. Создать абстрактный класс Figure (на плоскости) с методами вычисления пло-щади и периметра, 
а также методом, выводящим информацию о фигуре на экран. Создать подклассы: Rectangle (прямоугольник), 
Circle (круг), Triangle (треугольник) со своими методами вычисления площади и периметра.
Создать список из n фигур и вывести полную информацию о фигурах на экран.
'''
from abc import ABC, abstractmethod
class Figure(ABC):
    '''
    Абстрактный класс фигур на плоскости с атрибутами
    вычисления площади и периметра фигур, а также выводом информации о
    фигурах на экран
    '''
    @abstractmethod
    def area(self):
        '''
        Метод вычисления площади
        '''
        pass

    @abstractmethod
    def perimeter():
        '''
        Метод вычисления периметра
        '''
        pass

    @abstractmethod
    def draw():
        pass

    @abstractmethod
    def info():
        '''
        Метод вывода информации на экран
        '''
        pass

    

class Rectangle(Figure):
    '''
    Класс прмоугольника на плоскости с атрибутами
    вычисления его площади и периметра , а также выводом информации о
    о нём на экран   
    '''
    def __init__(self, a, b):
        '''
        :param a - Сторона a
        :param b - Сторона b
        '''
        global centerX, centerY, shift, scale

        
        self.x = centerX
        self.y = centerY
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2*self.a + 2*self.b
    
    def draw(self, x = None, y = None):
        self.X = x
        self.Y = y
        
        canv.create_line(shift, self.y, self.x*2-shift, self.y, fill = 'gray', arrow = 'last')
        canv.create_line(self.x, shift, self.x, self.y*2-shift, fill = 'gray', arrow = 'first')
        canv.create_text(self.x-10, shift, text = 'Y', fill='gray')
        canv.create_text(2*self.x-shift, self.y-10, text = 'X', fill='gray')
        if self.X is None or self.Y is None:
            canv.create_rectangle(self.x, self.y - self.a * scale, self.x + self.b * scale, self.y, outline = 'blue')

        else:
            self.X = self.X * scale
            self.Y = self.Y * scale
            canv.create_rectangle(self.x + self.X, (self.y - self.a * scale)-self.Y, (self.x + self.b * scale) + self.X, self.y - self.Y, outline = 'blue')

    
    
    def info(self):
        print(f"Rectangle: Сторона a: {self.a} Сторона b: {self.b} Площадь: {self.area()} Периметр: {self.perimeter()} {self.draw()}")
        

class Circle(Figure):
    '''
    Класс круга на плоскости с атрибутами
    вычисления его площади и периметра , а также выводом информации о
    о нём на экран   
    '''
    def __init__(self, r):
        '''
        :param r - радиус окружности
        '''
        self.r = r
        global centerX, centerY, shift, scale

        
        self.x = centerX
        self.y = centerY

    def area(self):
        return 3.14 * self.r**2
    
    def perimeter(self):
        return 2*3.14*self.r
    
    def draw(self, x = None, y = None):
        self.X = x
        self.Y = y

        canv.create_line(shift, self.y, self.x*2-shift, self.y, fill = 'gray', arrow = 'last')
        canv.create_line(self.x, shift, self.x, self.y*2-shift, fill = 'gray', arrow = 'first')
        canv.create_text(self.x-10, shift, text = 'Y', fill='gray')
        canv.create_text(2*self.x-shift, self.y-10, text = 'X', fill='gray')
        if self.X is None or self.Y is None:
            canv.create_oval(self.x - self.r * scale, self.y - self.r * scale, self.x + self.r * scale, self.y + self.r * scale, outline = 'red')
        else:
            self.X = self.X * scale
            self.Y = self.Y * scale
            canv.create_oval((self.x - self.r * scale)+self.X, (self.y - self.r * scale) - self.Y, (self.x + self.r * scale) + self.X, (self.y + self.r * scale) - self.Y, outline = 'red')

        
        #canv.create_oval(self.x - self.r*scale, self.y, self.x+self.r*scale, self.y)
    
    def info(self):
        print(f"Circle: Радиус: {self.r} Площадь: {self.area()} Периметр: {self.perimeter()} {self.draw()}")

class Triangle(Figure):
    '''
    Класс треугольника на плоскости с атрибутами
    вычисления его площади и периметра , а также выводом информации о
    о нём на экран   
    '''
    
    def __init__(self, footing, b, c, h):
        '''
        :param footing - Основание треугольника
        :param b - Сторона b
        :param c - Сторона c
        :param h - Высота
        '''
        global centerX, centerY, shift, scale

        
        self.x = centerX
        self.y = centerY
        self.footing = footing
        self.b = b
        self.c = c
        self.h = h

    def area(self):
        return 0.5*self.footing*self.h
    
    def perimeter(self):
        return self.footing + self.b + self.c 
    
    def draw(self, x = None, y = None):
        self.X = x
        self.Y = y

        canv.create_line(shift, self.y, self.x*2-shift, self.y, fill = 'gray', arrow = 'last')
        canv.create_line(self.x, shift, self.x, self.y*2-shift, fill = 'gray', arrow = 'first')
        canv.create_text(self.x-10, shift, text = 'Y', fill='gray')
        canv.create_text(2*self.x-shift, self.y-10, text = 'X', fill='gray')
        if self.X is None or self.Y is None:
            canv.create_polygon(self.x, self.y,  self.x + self.b*scale, self.y, self.x + self.footing*scale, self.y - self.footing * scale, fill = '', outline='green')
        else:
            self.X = self.X * scale
            self.Y = self.Y * scale
            canv.create_polygon(self.x+self.X, self.y-self.Y,  self.x+(self.X + self.b*scale) , self.y - self.Y, self.x + (self.X + self.footing*scale), self.Y - (self.footing*scale) , fill = '', outline='green')
    
    
    def info(self):
        print(f"Triangle: Основание: {self.footing} Сторона b:{self.b} Сторона c: {self.c} Высота: {self.h} Площадь: {self.area()} Периметр: {self.perimeter()} {self.draw()}")
 
        
figurs = [    
    Rectangle(10, 45),
    Circle(5),
    Triangle(5,12,6,8),
    Rectangle(2, 2)
    ]
#for i in figurs:
    #i.info()

Rectangle(10, 45).draw(-10, 4)
Circle(5).draw(-10, 4)
Triangle(30,40,50,40).draw(-10,4)
print('2############')

'''
2. Составить описание класса для вектора, заданного координатами его 
концов в трехмерном пространстве. Реализовать операции сложения и вычитания 
векторов, результатом которого является вектор, а также вычисления скалярного 
произведения двух векторов, длины вектора, косинуса угла между двумя век-торами.
'''

class Vector:
    '''
    Класс векторов a, b на плоскости 
    '''
    
    def __init__(self, x: int, y: int, z: int):
        '''
        :param x - Координата вектора a по Ox
        :param y - Координата вектора a по Oy
        :param z - Координата вектора a по Oz
        
        '''
        self.x = x
        self.y = y
        self.z = z
        
    
    def amount(self, x1, y1, z1):
        '''
        Метод суммирования двух векторов
        Возвращает вектор
        :param x1 - Координата вектора b по Ox
        :param y1 - Координата вектора b по Oy
        :param z1 - Координата вектора b по Oz
        '''
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1 
        spisok = []
        
        spisok +=[self.x + self.x1, self.y + self.y1, self.z + self.z1]
        return spisok
    
    def dif(self, x1, y1, z1):
        '''
        Метод вычитания двух векторов
        Возвращает вектор
        :param x1 - Координата вектора b по Ox
        :param y1 - Координата вектора b по Oy
        :param z1 - Координата вектора b по Oz
        '''

        self.x1 = x1
        self.y1 = y1
        self.z1 = z1 
        spisok = []
        
        spisok +=[self.x - self.x1, self.y - self.y1, self.z - self.z1]
        return spisok
    
    def scal(self, x1, y1, z1):
        '''
        Метод скалярного произведения
        двух векторов
        :param x1 - Координата вектора b по Ox
        :param y1 - Координата вектора b по Oy
        :param z1 - Координата вектора b по Oz
        '''
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1 
        
        return (self.x + self.x1) * (self.y + self.y1) * (self.z + self.z1)
    
    def lenVector(self, x1 = None, y1 = None, z1 = None):
        '''
        Метод нахождения длин двух векторов
        Возвращает список, содержащий длины векторов
        :param x1 - Координата вектора b по Ox
        :param y1 - Координата вектора b по Oy
        :param z1 - Координата вектора b по Oz
        '''
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
    
        
        if x1 is None or y1 is None or z1 is None:
            return ((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5
        else:
            return ((self.x1)**2 + (self.y1)**2 + (self.z1)**2)**0.5
        
    
    def cos(self, x1, y1, z1):
        '''
        Метод нахождения косинуса угла между
        двумя векторами
        :param x1 - Координата вектора b по Ox
        :param y1 - Координата вектора b по Oy
        :param z1 - Координата вектора b по Oz
        '''
       
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        
        lenght = ((x1**2)+(self.y1**2)+(self.z1**2))**0.5
        
        return self.scal(self.x1, self.y1, self.z1) / (lenght*self.lenVector())
    
    def info(self, x1, y1, z1):
        '''
        Метод вывода информации на экран
        :param x1 - Координата вектора b по Ox
        :param y1 - Координата вектора b по Oy
        :param z1 - Координата вектора b по Oz
        '''
       
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
       
        return(f'Cумма: {self.amount(self.x1, self.y1, self.z1)} Разность: {self.dif(self.x1, self.y1, self.z1)} Скалярное произведение: {self.scal(self.x1, self.y1, self.z1)} Длина векторa: {self.lenVector(self.x1, self.y1, self.z1)} Косинус угла между векторами: {self.cos(self.x1, self.y1, self.z1)}')
    

print(Vector(5,7,0).info(0,2,5))
canv.pack()
tk.mainloop()