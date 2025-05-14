import tkinter as tk
from tkinter import ttk
import math



class Calculator:
    def __init__(self, master):
        self.style = ttk.Style()
        self.style.configure("Tall.TButton",  padding=(0, 10))
        self.style.configure("Custom.TButton", font=("Arial", 12, "bold"),padding=(0, 15))
        self.master = master
        self.master.title("Калькулятор")
        self.master.geometry('460x410')
        self.master.resizable(False, False)
        self.memory = 0
        self.field = ttk.Entry(window, width=50, style='Tall.TButton', font='TimesNewRoman')
        self.field.grid(row = 0, column = 0, columnspan=4)
        label = ttk.Label(text='    ', width=10)
        label.grid(row=1, column=0)
        grid = 0

        self.createButtons()
        self.result_shown = False



    def buttonCommand(self,id):
        '''
        Функция выполняет операции при нажатии кнопок, в зависимости от 
        их id
        id:
        1 Вставка 1
        2 Вставка 2
        3 Вставка 3
        ...
        0 - Вставка 0
        MR - чтение памяти
        MC - очистка памяти
        M+ - Добавление в память
        M- - вычитание из памяти
        C - Очистка поля
        CE - Очистка поля и памяти
        √ - Вычисление квадратного корня
        ⌫ - удаление последнего символа
        '''
        
        self.id = id
        self.current_text = self.field.get()  # Получаем текущий текст из Entry
        self.field.delete(0, tk.END)
        self.field.insert(0, self.current_text + self.id) 
        l = len(self.current_text)
        if self.current_text[-1:] in '/*-+.' and self.current_text[-2:-1] in '/*-+.':
            self.current_text = self.current_text.replace(self.current_text[-2:-1], self.current_text[-1:],1)
            self.current_text = self.current_text[:-1]
            self.field.delete(0, tk.END)
            self.field.insert(0, self.current_text + self.id) 
            
        
        if self.id == 'C':
            self.field.delete(0, tk.END)
        elif self.id == '=':
        
            try:
                self.field.delete(0, tk.END)
                if self.current_text[-1:] in '/*-+.':
                    self.current_text = self.current_text[:-1] + self.current_text[-1:] + self.current_text[:-1]
                elif self.current_text[0] in '/*-+.':
                    self.current_text = self.current_text[1:]
                elif self.current_text[0] == '√':
                    self.current_text = self.current_text[1:]
                    result = math.sqrt(int(self.current_text))
                    self.current_text =str( result)
                    
                    
                result = eval(self.current_text)
                self.field.insert(0, result)
                self.result_shown = True

            except ZeroDivisionError:              #Обработка ошибки деления на ноль
        
                self.field.delete(0, tk.END)
                self.field.insert(0, f'ОШИБКА: деление на 0')
                self.result_shown = True
            
            except SyntaxError:                   #Обработка ошибки неверного синтаксиса
                self.field.delete(0, tk.END)
                self.field.insert(0, f'ОШИБКА: Неверный синтаксис')
                self.result_shown = True

            except Exception as e:                #Обработка иных ошибок
                self.field.delete(0, tk.END)
                self.field.insert(0, f'ОШИБКА: {e}')
                self.result_shown = True

        
        elif self.id == '⌫':
            self.field.delete(0, last = tk.END)
            self.field.insert(0, self.current_text.replace('⌫','',1))
            self.current_text = self.current_text[:-1]
            self.field.delete(0, tk.END)
            self.field.insert(0, self.current_text)
            self.result_shown = False
        
        


        elif self.id == 'MR':
            self.field.delete(0, tk.END)
            
            self.field.insert(0, str(self.memory))
            self.result_shown = False
            
        
        elif self.result_shown:
            self.field.delete(0, tk.END)
            self.result_shown = False
            self.field.insert(0, self.id)
            self.result_shown = False

        elif self.id == 'M+':
            self.field.delete(0, tk.END)
            self.current_text = self.current_text.replace('M+','',1)
            self.field.insert(0, self.current_text)
            self.memory += float(self.current_text)
            label = ttk.Label(text='M: ' + str(self.memory), foreground='gray', width=10)
            label.grid(row=1, column=0)


            self.result_shown = True

        elif self.id == 'M-':
            self.field.delete(0, tk.END)
            self.current_text = self.current_text.replace('M-','',1)
            self.field.insert(0, self.current_text )
            self.memory -= float(self.current_text)
            label = ttk.Label(text='M: ' + str(self.memory), foreground='gray', width=10)
            label.grid(row=1, column=0)

            self.result_shown = True

        elif self.id == 'MC':
            self.field.delete(0, tk.END)
            self.current_text = self.current_text.replace('M-','',1)
            self.field.insert(0, self.current_text)
            self.memory = 0
            
            label = ttk.Label(text='    ', width=10)
            label.grid(row=1, column=0)

            self.result_shown = True
        
        elif self.id == 'CE':
            self.field.delete(0, tk.END)
            self.memory = 0
            label = ttk.Label(text='    ', width=10)
            label.grid(row=1, column=0)

        
            


            

        


    def createButtons(self):
        '''
        Функция создает кнопки для калькулятора
        '''
        symbols = ['√','M+','M-','MR','⌫','C','CE','MC','1','2','3','+','4','5','6','-','7','8','9','*','.','0','=','/']
        m=0
        n=2
        for i in symbols:
            self.btn = ttk.Button(text=i, style="Custom.TButton", command=lambda c=i: self.buttonCommand(id=c))
            
            self.btn.grid(row=n, column=m)
            m += 1
            if m%4 == 0: 
                n+=1 
                m=0

       
if __name__ == "__main__":
    window = tk.Tk()
    calc = Calculator(window)
    window.mainloop()
