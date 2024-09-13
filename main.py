import matplotlib.pyplot as plt
import os
from  numpy import sort
from pandas import read_csv as pd
from matplotlib.widgets import TextBox, Button

fig, ax = plt.subplots()
axbox = fig.add_axes([0.1, 0.02, 0.2, 0.04])
axbutton = fig.add_axes([0.82, 0.02, 0.1, 0.04])
df = 0
x = 0
y = 0
l = ax.scatter(x,y)
text = TextBox(axbox, 'csv-file',textalignment="center")
button = Button(axbutton, 'clear')
# класс для работы с интерфейсом 
class InterFace:
    index = 0
    def change(self, event):
        ax.cla()
        plt.draw()
    def sumbit(self, expression):
        global df
        global text
        global x
        global y
        ext = os.path.splitext(expression)[-1]
        if ext == ".csv":
            
            try:
                df = pd(expression)
            except FileNotFoundError:
                print("Файл не найден")
            else:
                ax.cla()
                x = df['x']
                x = sort(x)
                y = df['y']
                ax.scatter(x,y)
                fig.canvas.draw()
                ax.relim()
                ax.autoscale_view()
                plt.draw()
                
        else:
            print("Не подходящее расширение")
inter = InterFace()

text.on_submit(inter.sumbit)
button.on_clicked(inter.change)
plt.show()
