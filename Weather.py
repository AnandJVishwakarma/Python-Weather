from tkinter import *
import tkinter as tk
import math
import requests

top = Tk()

def show_weather():
    e2=e1.get()
    address='http://api.openweathermap.org/data/2.5/weather?appid=27915982925f17d53c5a3460cebc2071&q='
    url=address+e2
    json_data=requests.get(url).json()
    format_add=json_data['main']
    str1="\n Weather is {} \n Temperature is minimum {} Celcius \n Temperature is maximum {} celcius".format(json_data['weather'][0]['main'],int(round(format_add['temp_min']-273)),int(round(format_add['temp_max']-272)))
    tk.Label(top,text=str1,fg="white",bg="black",width=50,height=10).grid(row=4,column=1)

tk.Label(top, text="Enter City name").grid(row=0)
e1 = tk.Entry(top)
e1.grid(row=0, column=1)
tk.Button(top,text='Show', command=show_weather).grid(row=3,column=1, sticky=tk.W,pady=4)
tk.Label(top,text=" ",fg="white",bg="black",width=50,height=10).grid(row=4,column=1,sticky = tk.W+tk.E)

top.mainloop()
tk.mainloop()