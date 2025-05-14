import tkinter as tk
from tkinter import ttk, filedialog, colorchooser, font, messagebox
import subprocess


class Interface():
    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x1000')
        self.master.title('Text Master')
        self.b = 0
        self.fileWay = ''
        self.lastChar = ''
        #window.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.color = 'BLACK'
        self.style = ttk.Style()
        self.style.configure("TButton", foreground=self.color)
        self.style.configure('My.TButton', foreground = 'black')
        self.style.configure('Bold.TButton', foreground = 'black', font = ('Times New Roman', 12, 'bold'))
        self.style.configure('Italic.TButton', foreground = 'black', font = ('Times New Roman', 12, 'italic'))
        self.style.configure('U.TButton', foreground = 'black', font = ('Times New Roman', 12, 'underline'))
        self.fonts = font.families()
        
        self.createMenu()
        self.createEntryField()
        
        


    def createEntryField(self):
        self.fieldFrame = tk.Frame(self.master, width=1000, height=800)  # Исправлено: self.master вместо window
        self.fieldFrame.pack(anchor='nw', fill='both')
        # Текстовое поле
        self.textField = tk.Text(self.fieldFrame, height=800, foreground=self.color, wrap='word')
        self.textField.pack(anchor='nw', fill='both')


    def createMenu(self):
        px = 5
        buttonWd = 15
        self.menuFrame = tk.Frame(self.master, width=1000, height=100) 
        self.menuFrame.pack(anchor='nw', fill='both')

        self.openButton = ttk.Button(self.menuFrame, style =  'My.TButton', text='Открыть', width=buttonWd, command=self.openFile)
        self.openButton.grid(row=0, column=0, sticky='nw', padx=px)

        self.saveButton = ttk.Button(self.menuFrame, style =  'My.TButton', text='Сохранить', width=buttonWd, command=lambda: self.saveFile('.txt'))
        self.saveButton.grid(row=1, column=0, sticky='nw', padx=px)

        self.saveAsButton = ttk.Button(self.menuFrame, style =  'My.TButton', text='Сохранить как...', command=lambda: self.saveAsFile('.txt'), width=buttonWd)
        self.saveAsButton.grid(row=2, column=0, sticky='nw', padx=px)

        self.colorButton = ttk.Button(self.menuFrame, style = 'TButton', text = '■', command=self.selectColor, width=buttonWd - 10)
        self.colorButton.grid(row=0, column=1, sticky='nw', padx=px)

        fontVar = tk.StringVar(value='Times New Roman')
        self.fontBox = ttk.Combobox(self.menuFrame, textvariable=fontVar, values=self.fonts)
        self.fontBox.grid(row=0, column=2, sticky='nw', columnspan=3, padx=px)
        self.fontBox.bind("<<ComboboxSelected>>", self.selectFont)
        self.fontBox.set('Times New Roman')

        self.size = 25
        self.sizeVar = tk.StringVar(value=25)
        self.fontSize = ttk.Spinbox(self.menuFrame, from_=10, to=128, width=buttonWd - 10, textvariable=self.sizeVar, command=self.sizeChange)
        self.fontSize.grid(row=2, column=1, sticky='nw', columnspan=1, padx=px)
        self.fontSize.set(25)
        buiFrame = ttk.Frame(self.menuFrame, width= 15, height=5)
        buiFrame.grid(row = 2, column= 3, columnspan=3)

        self.bold = ttk.Button(buiFrame, text='B', width = 5, style='Bold.TButton', command=lambda: self.BIU('B')).grid(row=2, column=3, sticky='nw')

        self.italic = ttk.Button(buiFrame, text='I', width = 5, style='Italic.TButton', command=lambda: self.BIU('I')).grid(row=2, column=4, sticky='nw')

        self.underline = ttk.Button(buiFrame, text='U', width = 5, style='U.TButton', command=lambda: self.BIU('U') ).grid(row=2, column=5, sticky='nw')
        self.modeState = tk.IntVar()
        self.mode = ttk.Checkbutton(self.menuFrame, text='Python Mode', variable=self.modeState, command = lambda: self.pythonMode())
        self.mode.grid(row=1, column=6, sticky='nw')
        
        
        
        
        self.buiCort = []
     



    def openFile(self):
        file = filedialog.askopenfilename()
        if file != "":
            with open(file, "r", encoding='utf-8') as f: 
                text = f.read()
                self.textField.delete("1.0", tk.END)
                self.textField.insert("1.0", text)
            self.fileWay = file
            window.title(f'Text Master - {file}')

        
    def saveAsFile(self, form):
        if form == '.txt':
            file = filedialog.asksaveasfilename(defaultextension=form, filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        else:
            file = filedialog.asksaveasfilename(defaultextension=form, filetypes=[('Python files', '*.py'), ('All files', '*.*')])
        if file != "":
            text = self.textField.get("1.0", tk.END)
            with open(file, "w", encoding='utf-8') as f:
                f.write(text)
            self.fileWay = f
            window.title(f'Text Master - {file}')

    def saveFile(self, form):
        if self.fileWay != '':
            with open(self.fileWay, 'w') as f:
                f.write(self.textField.get('1.0', tk.END))
        else:
            self.saveAsFile(form=form)
        
    def onClosing(self):
        if self.fileWay == '':
            result = messagebox.askokcancel("Выход", "Сохранить изменения перед выходом?")
            if result == True:
                self.saveAsFile()
        window.destroy()

    def selectColor(self):
        color_info = colorchooser.askcolor(initialcolor=self.color)
        if color_info[1]: 
            self.color = color_info[1]  
            self.style.configure("TButton", foreground=self.color)
            self.textField.configure(foreground=self.color)

    def sizeChange(self):
        self.size = int(self.fontSize.get())
        selection = self.fontBox.get()
        self.textField.configure(font=(selection, self.size, self.buiCort))
        

    def selectFont(self, event):
        selection = self.fontBox.get()
        self.textField.configure(font=(selection, self.size, self.buiCort))
    
    def BIU(self, var):
        if var == 'B' and 'bold' not in self.buiCort and self.b == 0:
            self.buiCort.append('bold')
            self.style.configure('Bold.TButton', foreground = 'green')

        elif var == 'B' and 'bold' in self.buiCort:
            self.buiCort.remove('bold')
            self.style.configure('Bold.TButton', foreground = 'black')
            
        if var == 'U' and 'underline' not in self.buiCort:
            self.buiCort.append('underline')
            self.style.configure('U.TButton', foreground = 'green')

        elif var == 'U' and 'underline' in self.buiCort:
            self.buiCort.remove('underline')
            self.style.configure('U.TButton', foreground = 'black')
            
        if var == 'I' and 'italic' not in self.buiCort:
            self.buiCort.append('italic')
            self.style.configure('Italic.TButton', foreground = 'green')

        elif var == 'I' and 'italic' in self.buiCort:
            self.buiCort.remove('italic')
            self.style.configure('Italic.TButton', foreground = 'black')

        
        self.textField.configure(font=(self.fontBox.get(), self.size, ' '.join(self.buiCort)))

#############################################################################################################################################################
    
    def pythonMode(self):
        if self.modeState.get() == 1:
            window.bind("<Return>", self.specialSymbDetect())
            self.runButton = ttk.Button(self.menuFrame, style='My.TButton', text = 'RUN', command=self.runFile)
            self.runButton.grid(row=2, column=6, sticky='nw')
            self.textField.configure(background='black', fg='white', )
            self.color = 'white'
            self.style.configure("TButton", foreground=self.color)
        else: 
            window.unbind('<Return>')
            self.runButton.grid_forget()
            self.textField.configure(background='white', fg='black')
            self.color = 'black'
            self.style.configure("TButton", foreground=self.color)

        

    def specialSymbDetect(self):
        self.lastChar = self.textField.get('1.0', 'end-1c')
        if self.lastChar == ':':
            self.textField.insert("\n\t")
            return "break"  
        return None
    
    def runFile(self):
        self.saveFile('.py')
        exec(open(str(self.fileWay)).read())
        #subprocess.run(['python', str(self.fileWay)])


window = tk.Tk()
Interface(window)
window.mainloop()