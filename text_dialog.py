import tkinter as tk
from tkinter import simpledialog

class CustomTextDialog(simpledialog.Dialog):
    def __init__(self, parent, title, initial_text=""):
        self.initial_text = initial_text
        super().__init__(parent, title)

    def body(self, master):
        self.text_widget = tk.Text(master, height=10, width=40)
        self.text_widget.insert(tk.END, self.initial_text)
        self.text_widget.pack()
        return self.text_widget

    def apply(self):
        self.result = self.text_widget.get("1.0", tk.END).strip()