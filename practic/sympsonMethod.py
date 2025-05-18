import tkinter as tk
from tkinter import ttk
y = None

class GraphBuilder():
    
    def __init__(self, master):
        self.px = 5
        self.py = 5
        self.master = master
        self.master.geometry('1300x1000')
        self.canv = tk.Canvas(window, width=1000, height=1000, background='white', highlightbackground='#8B4513')
        self.canv.pack(side=tk.RIGHT)
        self.centerX = 500
        self.centerY = 500
        self.scale = 60
        self.shift = 10
        window.bind("<Up>", lambda e: self.graphOffset(0, -5))
        window.bind("<Down>", lambda e: self.graphOffset(0, 5))
        window.bind("<Left>", lambda e: self.graphOffset(-5, 0))
        window.bind("<Right>", lambda e: self.graphOffset(5, 0))
        window.bind('<Delete>', lambda e: self.rebooting())
        window.bind('<Return>', lambda e: self.createGraph())
        
        self.style = ttk.Style()
        self.style.theme_use('winnative')

        self.createDPSK()
        self.createWidgets()
        

        self.style.configure('Horizontal.TScale', background = '#FFDEAD', troughcolor = '#8B4513')
        
    
        self.style.configure("My.TLabel", background = "#FFDEAD", foreground = 'gray')
        self.style.configure("My1.TLabel", background = "#FFDEAD")
        self.style.configure("Tall.TEntry",pudding = (0,5), background = "#FFDEAD",)
        self.style.configure("Tall.TButton",  padding=(0, 5), foreground = 'black')
        self.style.configure('Custom.TButton', fill = 'red',)
        

    def f(self, x):  
        global y
        try:
            return eval(y, {'x': x})  
        except:
            return 0  
    
    def createWidgets(self):
        global y
        controlFrame = tk.Frame(window, width=300, height=1000)
        controlFrame.pack(anchor='nw', fill='both')
        controlFrame.configure(background="#FFDEAD")
        

        self.entry = ttk.Entry(controlFrame)  
        self.entry.pack(anchor='nw', pady=self.py, padx=self.px, fill='x')
        
        ttk.Button(controlFrame, style = "Tall.TButton", text='Построить', command=self.createGraph).pack(anchor='nw', pady=self.py, padx=self.px, fill='both')
        self.a = ttk.Entry(controlFrame)
        self.a.pack(anchor='nw', pady=self.py, padx=self.px, fill='x')

        self.b = ttk.Entry(controlFrame)
        self.b.pack(anchor='nw', pady=self.py, padx=self.px, fill='x')

        self.n = ttk.Entry(controlFrame)
        self.n.pack(anchor='nw', pady=self.py, padx=self.px, fill='x')
    
        sc=int(self.scale)
        ttk.Label(controlFrame, text=f"Масштаб", style='My1.TLabel').pack(anchor='nw', pady=self.py, padx=self.px)
        ttk.Label(controlFrame, textvariable=sc, style='My1.TLabel' ).pack(anchor='nw', pady=self.py, padx=self.px)
        self.slider = ttk.Scale(controlFrame, style="Horizontal.TScale", variable=sc, from_=10, to=300, orient=tk.HORIZONTAL, command=lambda e: self.changeScale(), )
        self.slider.pack(anchor='nw', pady=self.py, padx=self.px, fill='x')
        info = tk.Frame(controlFrame, width=300, height = 500)
        info.pack(anchor='nw', pady=self.py, padx=self.px)
        info.configure(background='#FFDEAD', highlightbackground='#DEB887')
       
        ttk.Button(controlFrame,style = "Tall.TButton", text = 'Сбросить', command=self.rebooting).pack(anchor='se', pady=self.py, padx=self.px, fill='x')
        self.slider.set(self.scale)
        
        ttk.Label(info, style='My.TLabel', text='← - Сдвинуть ось Oy влево').pack(anchor='nw', pady=self.py, padx=self.px)
        ttk.Label(info, style='My.TLabel', text='→ - Сдвинуть ось Oy вправо').pack(anchor='nw', pady=self.py, padx=self.px)
        ttk.Label(info, style='My.TLabel', text='↑ - Сдвинуть ось Ox вверх').pack(anchor='nw', pady=self.py, padx=self.px)
        ttk.Label(info, style='My.TLabel', text='↓ - Сдвинуть ось Ox вниз').pack(anchor='nw', pady=self.py, padx=self.px)
        ttk.Label(info, style='My.TLabel', text='DEL - Сброс').pack(anchor='nw', pady=self.py, padx=self.px)
        ttk.Label(info, style='My.TLabel', text='Enter - Построить график').pack(anchor='nw', pady=self.py, padx=self.px)

    def createDPSK(self):
        self.canv.delete('all')
        self.canv.create_line(self.centerX, 990, self.centerX, self.shift, arrow='last')
        self.canv.create_line(990, self.centerY, self.shift, self.centerY, arrow='first')
        xLen = (self.centerX*2 - 2*self.shift)
        yLen = (self.centerY*2 - 2*self.shift)
        for i in range(1,xLen-1):
            self.canv.create_line(self.centerX + i*self.scale, self.centerY + 5, self.centerX + i*self.scale, self.centerY - 5)
            self.canv.create_text(self.centerX + i*self.scale, self.centerY + 15, text = i)
        for i in range(1, yLen):
            self.canv.create_line(self.centerX + 5, self.centerY + i*self.scale, self.centerX - 5, self.centerY + i*self.scale)
            self.canv.create_text(self.centerX - 15, self.centerY + i*self.scale, text = -i)
        for i in range(1,xLen-1):
            self.canv.create_line(self.centerX - i*self.scale, self.centerY + 5, self.centerX - i*self.scale, self.centerY - 5)
            self.canv.create_text(self.centerX - i*self.scale, self.centerY + 15, text = -i)
        for i in range(1, yLen-1):
            self.canv.create_line(self.centerX + 5, self.centerY - i*self.scale, self.centerX - 5, self.centerY - i*self.scale)
            self.canv.create_text(self.centerX - 15, self.centerY - i*self.scale, text = i)

        self.canv.create_text(990, self.centerY - 10, text='X')
        self.canv.create_text(self.centerX - 10, 10, text='Y')

    def createGraph(self):
        global y
        y = self.entry.get()  
        self.createDPSK()  
        xLen = (self.centerX*2 - 2*self.shift)
        a = -int(self.a.get())
        b = int(self.b.get())
        h = 0.01
        n = int((b - a) / h)
        points = []
        for i in range(n):
            x = a + i * h
            try:
                y_val = self.f(x)
                points.append((self.centerX + x * self.scale, self.centerY - y_val * self.scale))
            except:
                continue
        if points:
            self.canv.create_line(points, fill='red')
        self.sympsonMethod()

    def graphOffset(self, dx, dy):
        if self.centerX >=990: self.centerX = 10
        if self.centerX <=10: self.centerX = 990
        if self.centerY >=990: self.centerY = 10
        if self.centerY <=20: self.centerY = 990
        self.centerX += dx
        self.centerY += dy
        self.createDPSK()
        self.createGraph()
        self.sympsonMethod()

    def changeScale(self):
        self.scale = self.slider.get()
        self.createDPSK()
        
        if self.entry.get() !="":
            self.createGraph()
        
    def rebooting(self):
        self.centerX = 500
        self.centerY = 500
        self.scale = 60
        self.slider.set(self.scale)
        self.createDPSK()
        
        if self.entry.get() !="":
            self.createGraph()
    
    def sympsonMethod(self):
        try:
            a = float(self.a.get())
            b = float(self.b.get())
            n = int(self.n.get())
            
            h = (b - a) / n
            points = []
            
            for i in range(n + 1):
                x = a + i * h
                y = self.f(x)
                points.append((self.centerX + x * self.scale, self.centerY, self.centerX + x * self.scale, self.centerY - y * self.scale))
            
            self.canv.create_line(points, fill="blue", width=2)
            
        except:
            pass





window = tk.Tk()
window.configure(background='#FFDEAD')
GraphBuilder(window)
window.mainloop()