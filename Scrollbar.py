from tkinter import *


class CanvasScrollBar:

    def __init__(self, canvas, frame,mainframe):


        self.frame = frame
        self.canvas = canvas

        scrollbar = Scrollbar(mainframe, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((0, 0), window=frame, anchor=NW)

    def on_frame_configure(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def on_arrow_scroll(self,event):
        if event.keysym == "Up":
            self.canvas.yview_scroll(-1, "units")
        elif event.keysym == "Down":
           self.canvas.yview_scroll(1, "units")

    def scroling(self,frame):

        frame.bind("<Configure>", self.on_frame_configure)
        frame.bind("<MouseWheel>", self.on_mousewheel)
        frame.bind("<Up>", self.on_arrow_scroll)
        frame.bind("<Down>", self.on_arrow_scroll)