import tkinter as tk
import math

ht = 1000
wt = 1000
center_x = wt//2
center_y = ht//2
scale = 50
shift = 20
window = tk.Tk()
window.title('Your function')
window.geometry('1000x1000')
canv = tk.Canvas(width=ht, height=wt)
color = 'gray'
a=-100
b=10

def f(x):
    return x**2

def F(x):
    return 2*x

class SecantMethod:
    def __init__(self, center_x = center_x, center_y = center_y, scale = scale, func = f, tunget = F,  a=a, b=b, shift = shift, color = color):
        self.centerX = center_x
        self.centerY = center_y
        self.scale = scale
        self.func = func
        self.color = color
        self.shift = shift
        self.a = a
        self.b = b
        self.tunget = tunget


    def funcDrawing(self):
        
        length = self.b - self.a   # длина отрезка
        h = 0.01         # шаг для рисования графика функции
        n = int(length / h)
        for i in range(n-1):
            x0 =  (self.a+i*h)*self.scale
            y0 =  self.func(self.a+i*h)*self.scale 
            x1 = (self.a+(i+1)*h)*scale
            y1 =  self.func(self.a+(i+1)*h)*self.scale 
            canv.create_line(self.centerX + x0, self.centerY - y0, self.centerX + x1, self.centerY - y1, fill='red', width=2)
    
    def DPSK(self):
        canv.create_line(0,self.centerY, 1000, self.centerY, arrow = 'last', fill=color)
        canv.create_line(self.centerX, 1000, self.centerX, 0, arrow='last', fill=color)
        canv.create_text(self.centerX-10, self.centerY+10, text='0', fill=color)

        x_len = 2*self.centerX - 2*self.shift
        start = self.centerX - self.shift
        n = (x_len-start)//self.scale     
        m = (start)// self.scale
        for i in range(n):
            canv.create_line(self.centerX + i*self.scale, self.centerY + 5, self.centerX + i*self.scale, self.centerY - 5, fill = self.color)
        for i in range(m):
            canv.create_line(self.centerX - i*self.scale, self.centerY + 5, self.centerX - i*self.scale, self.centerY - 5, fill = self.color)
        start = self.centerY - self.shift
        y_len = 2*self.centerY - 2*self.scale
        n = (y_len - start)//self.scale
        m = (start)// self.scale
        for i in range(n):
            canv.create_line(self.centerX + 5, self.centerY  +i*self.scale, self.centerX-5, self.centerY + i*self.scale, fill = self.color)
        for i in range(m):
            canv.create_line(self.centerX + 5, self.centerY - i*self.scale, self.centerX-5, self.centerY - i*self.scale, fill = self.color)

        x_len = 2*self.centerX - 2*self.shift
        start = self.centerX - self.shift
        n = (x_len-start)//self.scale     
        m = -1*((start)// self.scale)
        k=15
        for i in range(m+1,0):
            canv.create_text(self.centerX + i*self.scale, self.centerY + k, text=str(i), fill=self.color)
        for i in range(1,n):
            canv.create_text(self.centerX + i*self.scale, self.centerY + k, text=str(i), fill=self.color)
        start = self.centerY - self.shift
        y_len = 2*self.centerY - 2*self.scale
        n = (y_len - start)//self.scale
        m = -1*((start)// self.scale)
        for i in range(m+1,0):
            canv.create_text(self.centerX - k, self.centerY + i*self.scale, text=str(-1*i), fill=self.color)
        for i in range(1,n):
            canv.create_text(self.centerX - k, self.centerY + i*self.scale, text=str(-1*i), fill=self.color)
        canv.create_text(self.centerX - (k-5), self.centerY + (k-5), text='0', fill = self.color)
        canv.create_text(self.centerX + (k-5), self.shift, text='Y', fill = self.color)
        canv.create_text(2*self.centerX-self.shift, self.centerY - (k-5), text='X', fill = self.color)

    
    def secantMethod(self, e):
        self.e = e
        x0 = self.a
        x1 = self.b

        while abs(x0 - x1) > self.e:
            
            x = x0 - self.func(x0)*((x0 - x1)/(self.func(x0) - self.func(x1)))
            x0 = x1
            x1 = x
            
            
            canv.create_line(self.centerX + x0*self.scale, self.centerY, self.centerX + x*self.scale, self.centerY - self.func(x)*self.scale, fill = 'blue')
            
            

    def Demostration(self, e):
        self.e = e
        SecantMethod().DPSK()
        SecantMethod().funcDrawing()
        SecantMethod().secantMethod(e=self.e)

SecantMethod().Demostration(e = 0.001)

canv.pack()
tk.mainloop()

