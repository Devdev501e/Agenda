from tkinter import *
from filter import Filter
from data_base_reach import DataTransaction
from modif_text import DialogText

from CanvasWithRoundedBorders import CanvasWithRoundedBorders


class EditableLabel:

    def __init__(self, master=None, label_id=None, width=None, height=None, sql=NONE, hour=None, **kwargs):

        task = False
        self.label_id = label_id
        self.master = master
        self.canvas = CanvasWithRoundedBorders(master, width=width, height=100)
        self.canvas.bind("<Button-1>", self.modifier_texte)
        self.hour = hour
        self.width = width





        for row in sql:

            if str(row[1]) == label_id[0:10]:
                # hours
                if str(hour) == str(row[3]):

                    self.creat_task(row[4], row[5])
                    task = True

        self.text = Text(master, height=5, width=10, **kwargs)
        self.canvas_first = Canvas(master, width=width,
                                       bg="white", height=height)
        if not task:
            self.canvas_first.pack()

        self.text.bind("<KeyPress-Shift_R>", self.stop_editing)
        self.canvas_first.bind("<Button-1>", self.start_editing)

    def start_editing(self, event):
        # Afficher le widget Entry et cacher le label pendant l'édition
        # self.delete(0, END)

        self.text.config(relief=SOLID, bd=1, insertontime=True, selectbackground="blue", height=10)
        self.text.focus_set()
        self.canvas_first.forget()
        self.text.pack()
    def close_task(self,event=None):
        self.canvas.destroy()
        self.frame.destroy()
        self.canvas_first.pack()
        DataTransaction.delete_data(self.label_id[0:10], self.label_id[5:7], self.hour)
        self.canvas = CanvasWithRoundedBorders(self.master, width=self.width, height=100)
        self.canvas.bind("<Button-1>", self.modifier_texte)
        print('ta mère')

    def creat_task(self, title, content):
        self.frame = Frame(self.master)
        self.frame.pack(fill=X, expand=True)
        close = Canvas(self.frame, width=11, height=11)
        close.pack(side=RIGHT)
        rayon = 5
        x_centre, y_centre = 7, 7
        close.create_oval(x_centre - rayon, y_centre - rayon, x_centre + rayon, y_centre + rayon, fill="red")
        close.bind("<Button-1>", self.close_task)



        self.canvas.create_canvas_rounded()
        self.canvas.create_text(100, 15, text=f'{title}', font=("Helvetica", 9, "bold"), fill="black", width=180,
                                tags=("texte", "texte_1"))
        self.canvas.create_text(10, 30, text=f'{content}', font=("Helvetica", 8), fill="black", anchor="nw",
                                justify="left", width=180, tags=("texte", "texte_2"))





    def stop_editing(self, event=None):
        # Cacher le widget Entry et afficher le label après l'édition
        title = ""
        content = ""
        c = 0
        for i in self.text.get("1.0", "end-1c"):
            if i == '*':
                c += 1
            elif c == 1:
                title += i
            elif c == 2:
                content += i
        content = Filter.bonjour(content)

        if title != "" and content != "":
            self.creat_task(title, content)
            DataTransaction.write_data(self.label_id[0:10], self.label_id[5:7], self.hour, content, title)
            self.text.forget()

    def modifier_texte(self, event):
        # Récupère l'item sous le clic de la souris
        item_id = self.canvas.find_closest(event.x, event.y)

        # Vérifie si l'item est un texte dans le canvas
        if "texte" in self.canvas.gettags(item_id):
            # Récupère l'index du texte

            index = int(self.canvas.gettags(item_id)[1][6])

            # Affiche la boîte de dialogue pour la modification
            self.modifier_texte_dialogue(index)

    def modifier_texte_dialogue(self, index):
        # Affiche une boîte de dialogue pour modifier le texte
        texte_actuel = self.canvas.itemcget(f"texte_{index}", "text")
        # nouveau_texte = simpledialog.askstring("Modifier le texte", "Nouveau texte :", initialvalue=texte_actuel)
        nouveau_texte = DialogText(texte_actuel, self.canvas, index, self.hour, self.label_id, )

        # Si un nouveau texte est saisi, modifie le texte dans le canvas
        if nouveau_texte is not None:
            self.canvas.itemconfig(f"texte_{index}", text=nouveau_texte)
