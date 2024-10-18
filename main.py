import matplotlib.pyplot as plt
import os
from tkinter.messagebox import showerror
from pandas import read_csv as pd
from matplotlib.widgets import TextBox, Button, RadioButtons

# расположение всего в окне 
fig, ax = plt.subplots()
fig.subplots_adjust(right=0.85, left= 0.1)
axbox = fig.add_axes([0.1, 0.02, 0.2, 0.04])
axbutton = fig.add_axes([0.82, 0.02, 0.1, 0.04])
axradioMode = fig.add_axes([0.87, 0.65, 0.09, 0.1])

# основы графика
x = [0,1]
y = [1,0]
l = ax.scatter(x,y)
ax.grid()
mode = 0

# экземпляры элементов интерфейса
text = TextBox(axbox, 'csv-file',textalignment="center")
button = Button(axbutton, 'clear')
radioB_mode = RadioButtons(axradioMode, ('one','a lot'))

# класс графика
class Graph:
    def __init__(self) -> None:
        self.x = []
        self.y = []
    # метод draw рисует график
    def draw(self, x, y):
        self.x = x
        self.y = y
        self.sort(x,y)
        ax.scatter(self.x,self.y)
        ax.grid()
        plt.draw()
    def sort(self, x,y):
        l = []
        for i in range(len(x)):
            l.append((x[i],y[i]))
        l.sort(key=lambda x: x)
        X = []
        Y = []
        for item in l:
            X.append(item[0])
            Y.append(item[1])
        return X,Y

# класс для работы с интерфейсом 
class InterFace:
    def __init__(self) -> None:
        self.graph = Graph() # экземпляр класса графика
        self.f = 0 # сюда помещается файлик csv

    # очищает график от всего
    def clear(self, event):
        ax.cla()
        plt.draw()
        

    def RadioB_Mode(self, label):
        global mode
        if label == 'one':
            mode = 0
        else:
            mode = 1

    # загружает и выводит на экран график из файла
    def sumbit(self, expression):
        global mode
        ax.grid()
        ext = os.path.splitext(expression)[-1]
        if ext == ".csv":
            try:
                self.f = pd(expression)
            except FileNotFoundError:
                showerror('Ошибка', 'Нет такого файла')
            else:
                if mode == 0:
                    ax.cla()
                # сортировка точек от меньшего к большему по оси X 
                x = self.f['x']
                y = self.f['y']
                
                self.graph.draw(x, y)  
        else:
            showerror('Ошибка', 'Не правильное расширение файла')

inter = InterFace() # экземпляр логики интерфейса

#соединение интерфейса с логикой его работы
text.on_submit(inter.sumbit)
button.on_clicked(inter.clear)
radioB_mode.on_clicked(inter.RadioB_Mode)
plt.show()
