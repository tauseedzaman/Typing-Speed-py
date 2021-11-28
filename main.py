# A simpple Typing Speed Checker
# Auther: Tauseed Zaman
# Date: 28/11/2021
import tkinter as tk
from time import sleep
from threading import Thread
from random import choice

class TypeSpeed:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed")
        self.root.geometry("850x8000")
        self.texts = open("texts.txt",'r').read().split("\n")

        self.frame = tk.Frame(self.root)
        self.sample_label = tk.Label(self.frame,font=("Helvetice",18), text = choice(self.texts))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=2, pady=5)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetice",24))
        self.input_entry.grid(row=1,column=0,  columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>",self.start)

        self.speed_label = tk.Label(self.frame,font=("Helvetice",18), text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n 0.00 WPM")
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=2, pady=5)

        self.reset_btn = tk.Button(self.frame,fg="green",bg="yellow", text="Reset",font=("Helvetice",18), command=self.reset)
        self.reset_btn.grid(row=3,column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)
        self.counter =0
        self.running = False
        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16,17,18]:
                self.running = True
                t = Thread(target=self.time_thread)
                t.start()  

        #check where is the entries are corrent or not
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget("text")[:-1]:
            self.running=False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            sleep(0.1)
            self.counter +=0.1

            cps = len(self.input_entry.get())/self.counter
            cpm = cps * 60

            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n {wps:.2f}WPS\n {wpm:.2f}WPM")

    # reset the application when the reset button is pressed
    def reset(self):
        self.running=False
        self.counter=0
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n 0.00 WPM")
        self.sample_label.config(text=choice(self.texts))
        self.input_entry.delete(0,tk.END)

TypeSpeed()
