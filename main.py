import matplotlib.pyplot as plt
import os
from tkinter.messagebox import showerror
from  numpy import sort, cos, sin
from pandas import read_csv as pd
from matplotlib.widgets import TextBox, Button, RadioButtons

# расположение всего в окне 
fig, ax = plt.subplots()
fig.subplots_adjust(right=0.85, left= 0.1)
axbox = fig.add_axes([0.1, 0.02, 0.2, 0.04])
axbutton = fig.add_axes([0.82, 0.02, 0.1, 0.04])
axradio = fig.add_axes([0.87, 0.5, 0.09, 0.1])

# основы графика
x = 0
y = 0
l = ax.scatter(x,y)

# экземпляры элементов интерфейса
text = TextBox(axbox, 'csv-file',textalignment="center")
button = Button(axbutton, 'clear')
radio = RadioButtons(axradio, ('standart','cos(x)', 'sin(x)'))
class Graph:
    global x
    global y
    def draw(self, x, y):
        self.x = x
        self.y = y
        self.x = sort(self.x)
        ax.scatter(self.x,self.y)
        fig.canvas.draw()
        plt.draw()
graph = Graph()
# класс для работы с интерфейсом 
class InterFace:

    f = 0
    
    global text

    # очищает график от всего
    def clear(self, event):
        radio.clear()
        ax.cla()
        plt.draw()
    
    def funcRadio(self, label):
        ax.cla()
        var = {'cos(x)': cos(self.f['x']), 'sin(x)': sin(self.f['x'])}
        if label != 'standart':
            graph.draw(self.f['x'], var[label])
            return
        graph.draw(self.f['x'], self.f['y'])
        

    # загружает и выводит на экран график из файла
    def sumbit(self, expression):
        radio.clear()
        ext = os.path.splitext(expression)[-1]
        if ext == ".csv":
            try:
                self.f = pd(expression)
            except FileNotFoundError:
                showerror('Ошибка', 'Нет такого файла')
            else:
                ax.cla()
                graph.draw(self.f['x'], self.f['y'])
                
        else:
            showerror('Ошибка', 'Не правильное расширение файла')

inter = InterFace() # экземпляр логики интерфейса

#соединение интерфейса с логикой его работы
text.on_submit(inter.sumbit)
button.on_clicked(inter.clear)
radio.on_clicked(inter.funcRadio)
plt.show()
