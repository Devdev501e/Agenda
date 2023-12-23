import tkinter as tk

def on_vertical_scroll(*args):
    canvas.yview(*args)

def on_horizontal_scroll(*args):
    canvas.xview(*args)

root = tk.Tk()
root.title("Scrollbar Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(expand=True, fill=tk.BOTH)

# Add some content to the Canvas
for i in range(20):
    canvas.create_text(150, i * 10, text=f"Item {i}", anchor=tk.CENTER)

# Create vertical scrollbar
vertical_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=on_vertical_scroll)
vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create horizontal scrollbar
horizontal_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=on_horizontal_scroll)
horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Configure the Canvas to use the scrollbars
canvas.config(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

root.mainloop()