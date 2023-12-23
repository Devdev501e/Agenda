from tkinter import *
from filter import Filter
from data_base_reach import DataTransaction


class DialogText:

    def __init__(self, text, canvas, index, hour, date):
        self.canvas = canvas
        self.index = index
        self.window = Tk()
        self.text_input = Text(self.window)
        self.text_input.pack()
        self.button = Button(self.window, text='valider', command=self.change_text)
        self.button.pack()
        self.text_input.insert("1.0", text)
        self.date = date
        self.hour = hour
        self.window.mainloop()

    def change_text(self):
        text = self.text_input.get("1.0", "end-1c")
        text = Filter.bonjour(text)
        print(text)
        self.window.destroy()
        self.canvas.itemconfig(f"texte_{self.index}", text=text)
        DataTransaction.modify_data(self.date[0:10], self.date[5:7], self.hour, text, self.index)

        return text
