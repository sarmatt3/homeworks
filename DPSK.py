import tkinter as tk
import math as mh
window = tk.Tk()
window.title('DPSK')


def Draw_axis(center_x: int, center_y: int, color , scale, shift: int):
    '''
    Функция рисует оси Ox и Oy
    :param center_x - Центр холста по оси Ox
    :param center_y - Центр холста по оси Oy
    :param color - цвет осей ДПСК
    :param shift - Отступ от краёв холста
    '''
    canv.create_line(shift, center_y, wt-shift, center_y, arrow='last', fill=color)
    canv.create_line(center_x, ht-shift, center_x, shift, arrow='last', fill = color )
def draw_scales(center_x: int, center_y: int, color: str, scale: int, shift: int):
    '''
    Функция рисует единичные отрезки на осях координат
    :param center_x - Центр холста по оси Ox
    :param center_y - Центр холста по оси Oy
    :param color - цвет осей ДПСК
    :param scale - масштаб
    :param shift - Отступ от краёв холста
    '''
    x_len = wt - 2*shift
    start = center_x - shift
    n = (x_len-start)//scale     # количество отсечек на  положительной части оси x
    m = (start)// scale
    for i in range(n):
        canv.create_line(center_x + i*scale, center_y + 5, center_x + i*scale, center_y - 5, fill = color)
    for i in range(m):
        canv.create_line(center_x - i*scale, center_y + 5, center_x - i*scale, center_y - 5, fill = color)
    start = center_y - shift
    y_len = ht - 2*scale
    n = (y_len - start)//scale
    m = (start)// scale
    for i in range(n):
        canv.create_line(center_x + 5, center_y  +i*scale, center_x-5, center_y + i*scale, fill = color)
    for i in range(m):
        canv.create_line(center_x + 5, center_y - i*scale, center_x-5, center_y - i*scale, fill = color)

def draw_numbers(center_x: int, center_y: int, color: str, scale: int, shift: int, k: int = 15):
    '''
    Функция рисует цифры, соответствующие единичным 
    отрезкам
    :param center_x - Центр холста по оси Ox
    :param center_y - Центр холста по оси Oy
    :param color - цвет осей ДПСК
    :param scale - масштаб
    :param shift - Отступ от краёв холста
    :param - Отступ цифр от осей 
    '''
    x_len = wt - 2*shift
    start = center_x - shift
    n = (x_len-start)//scale     
    m = -1*((start)// scale)
    for i in range(m+1,0):
        canv.create_text(center_x + i*scale, center_y + k, text=str(i))
    for i in range(1,n):
        canv.create_text(center_x + i*scale, center_y + k, text=str(i))
    start = center_y - shift
    y_len = ht - 2*scale
    n = (y_len - start)//scale
    m = -1*((start)// scale)
    for i in range(m+1,0):
        canv.create_text(center_x - k, center_y + i*scale, text=str(-1*i))
    for i in range(1,n):
        canv.create_text(center_x - k, center_y + i*scale, text=str(-1*i))
    canv.create_text(center_x - (k-5), center_y + (k-5), text='0', fill = color)
    canv.create_text(center_x + (k-5), shift, text='Y', fill = color)
    canv.create_text(wt-shift, center_y - (k-5), text='X', fill = color)


def CreateDPSK(center_x: int, center_y: int, color: str, scale: int, shift: int, k: int = 15):
    '''
    Функция рисует ДПСК
    :param center_x - Центр холста по оси Ox
    :param center_y - Центр холста по оси Oy
    :param color - цвет осей ДПСК
    :param scale - масштаб
    :param shift - Отступ от краёв холста
    '''
    Draw_axis(center_x=center_x, center_y=center_y, color=color, scale=scale, shift=shift)
    draw_scales(center_x=center_x, center_y=center_y, color=color, scale=scale, shift=shift)
    draw_numbers(center_x=center_x, center_y=center_y, color=color, scale=scale, shift=shift, k=k)


def f(x):
    '''
    Функция
    '''
    return x
    
def F(x):
    '''
    Функция
    '''
    return x**3



def draw_func(func, a: int, b: int, scale, center_x, center_y, f_color: str, f_wt):
    ''' 
    Функция рисует график функции f(x)
    :param  func - Функция
    :param  a - Начало отрезка, на котором определена функция 
    :param  b - Конец отрезка, на котором определена функция
    :param scale - масштаб
    :param center_x - Центр холста по оси Ox
    :param center_y - Центр холста по оси Oy
    :param f_color - Цвет графика функции
    '''
    
    length = b - a   # длина отрезка
    h = 0.01         # шаг для рисования графика функции
    n = int(length / h)
    
    for i in range(n-1):
        x0 =  (a+i*h)*scale
        y0 =  func(a+i*h)*scale 
        x1 = (a+(i+1)*h)*scale
        y1 =  func(a+(i+1)*h)*scale 
    

        canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1, fill=f_color, width=f_wt)
   
    
    
    
    create_point(center_x=wt//2, center_y=ht//2, color=color, scale=scale, shift=shift, x0 = 2, y0 = 2)



def create_point(center_x: int, center_y: int, color: str, scale: int, shift: int, x0: float, y0 = 0):
    x_len = wt - 2*shift
    canv.create_text(center_x + x0*scale, center_y - y0*scale, text='●')




wt=1000
ht=1000
bg_color = '#ffffff'
color = 'black'
scale = 40
shift = 20
f_color = 'red'
f_wt = None
x0=2
y0 = 0



window.geometry(str(wt) + 'x' + str(ht))
canv = tk.Canvas(width=wt, height=ht, bg=bg_color)
canv.pack()
CreateDPSK(center_x=wt//2, center_y=ht//2, color=color, scale=scale, shift=shift)
draw_func(f, -5, 5, center_x=wt//2, center_y=ht//2, scale=scale, f_color=f_color, f_wt=f_wt)
draw_func(F, -wt, wt, center_x=wt//2, center_y=ht//2, scale=scale, f_color='blue', f_wt=f_wt)

#create_point(center_x=wt//2, center_y=ht//2, color=color, scale=scale, shift=shift, x0 = x0, y0=y0)
tk.mainloop()