import tkinter as tk
import math
window = tk.Tk()
window.title('Your function')
center_x = 500
center_y = 500
window.geometry('1000x1000')
canv = tk.Canvas(width=1000, height=1000)
canv.pack()

canv.create_line(0,center_y, 1000, center_y, arrow = 'last')
canv.create_line(center_x, 1000, center_x, 0, arrow='last')
canv.create_text(center_x-10, center_y+10, text='0')
def f(x):
    return x**2-81

def Search_root(a,b,func,e,scale: int = 10):
    '''
    :param a - Начало отрезка
    :param b - Конец отрезка
    :param func - Функция
    :param e - Точность вычисления
    '''
    canv.create_line(center_x+a*scale, center_y, center_x+b*scale, center_y, fill = 'blue')
    d=0
    while abs(b-a)>e:
        canv.create_line(center_x+a*scale,center_y-5, center_x+a*scale, center_y+5)
        canv.create_line(center_x+b*scale,center_y-5, center_x+b*scale, center_y+5)
        canv.create_text(center_x+a*scale,center_y+10+d, text = str(a))
        canv.create_text(center_x+b*scale,center_y+10+d, text = str(b))

        canv.create_text(center_x+a*scale,center_y-10, text = 'a')
        canv.create_text(center_x+b*scale,center_y-10, text = 'b')
        
        c=(a+b)/2
        if func(c)*func(a)<0: 
            b=c 
            
        elif func(c)*func(b)<=0: 
            a=c
            
        else: canv.create_text(center_x+50, center_y + 50, text=str(c), fill='red')
        d+=0
    #return a
    canv.create_text(center_x + 100, center_y + 50, text=str(a), fill='red')

#def view(a,b,func,e):
    
scale = 20

x=Search_root(1,22,f,0.1, scale=scale)
print(x)

tk.mainloop()