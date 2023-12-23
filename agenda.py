from tkinter import *
from editable_label import EditableLabel
import datetime
from data_base_reach import DataTransaction

hour_number = 24
navigation = [0]
width_agenda = 180
height_agenda = 40


def agenda_creation():
    frame_agenda_inside = Frame(frame_agenda)
    frame_agenda_inside.pack(fill=X, expand=True)
    frame_date = Frame(date)
    frame_date.pack(fill=X, expand=True)
    rows = DataTransaction.get_data()
    date_actuelle = datetime.datetime.now()
    date_ulterieur = date_actuelle + datetime.timedelta(days=0 - date_actuelle.weekday() - navigation[0])

    label_year = Label(frame_date, text=f'{date_ulterieur.year}')
    label_year.grid(row=0, column=4)
    back_button = Button(frame_date, relief="flat", command=lambda: navig_button(7), image=image_right)
    back_button.grid(row=1, column=0)
    foward_button = Button(frame_date, relief="flat", bg='#fff', command=lambda: navig_button(-7), image=image_left)
    foward_button.grid(row=1, column=8)

    for i in range(0, 7):

        date_ulterieur = date_actuelle + datetime.timedelta(days=i - date_actuelle.weekday() - navigation[0])
        color_day = 'white'
        if date_ulterieur == date_actuelle:
            color_day = 'red'

        frame_jour = Canvas(frame_date, bg='#4065A4', width=width_agenda, height=height_agenda)
        frame_jour.grid(row=1, column=i + 1)
        frame_jour.create_text(100, 20,
                               text=f"{day_list[date_ulterieur.weekday()]}  {date_ulterieur.day}  {moth_list[date_ulterieur.month - 1]}",
                               font=("Helvetica", 9, "bold"), fill=color_day)

        for k in range(0, hour_number):

            canvas_hour = Canvas(frame_agenda_inside, bg='#4065A4', bd=1, relief=GROOVE, width=40, height=40)
            canvas_hour.grid(row=k, column=0)
            canvas_hour.create_text(22, 22,
                                    text=f"{k}",
                                    font=("Helvetica", 9, "bold"), fill='white')

            color_hour = 'lightgrey'
            if date_actuelle.hour == k and date_ulterieur == date_actuelle:
                color_hour = 'red'

            frame_input = Frame(frame_agenda_inside, bg=color_hour)
            frame_input.grid(row=k, column=i + 1)

            EditableLabel(frame_input, width=width_agenda, height=height_agenda, label_id=str(date_ulterieur), sql=rows,
                          hour=k)


def navig_button(jours):
    navigation[0] += jours

    frame_agenda.winfo_children()[0].destroy()

    date.winfo_children()[0].destroy()

    agenda_creation()


def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")


def on_arrow_scroll(event):
    if event.keysym == "Up":
        canvas.yview_scroll(-1, "units")
    elif event.keysym == "Down":
        canvas.yview_scroll(1, "units")


# Interface graphique
app = Tk()

image_left = PhotoImage(file="image/droite.png")
image_right = PhotoImage(file="image/gauche.png")
facteur_echantillonnage = 15  # Vous pouvez ajuster ce facteur selon vos besoins

# Redimensionner l'image avec subsample
image_left = image_left.subsample(facteur_echantillonnage, facteur_echantillonnage)
image_right = image_right.subsample(facteur_echantillonnage, facteur_echantillonnage)
app.title("Agenda")

# scrolable interface

# defs

###################################
frame_1 = Frame(app)
frame_1.pack(padx=15, pady=15)

date = Frame(frame_1)
date.pack(fill=X, expand=True)

# Créez un cadre de taille spécifique


canvas = Canvas(frame_1, height=500, width=1400)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar = Scrollbar(frame_1, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
frame_agenda = Frame(canvas)
canvas.config(yscrollcommand=scrollbar.set)
canvas.create_window((0, 0), window=frame_agenda, anchor=NW)

app.bind("<MouseWheel>", on_mousewheel)


##########################################################################################


def scroling(frame):
    frame.bind("<Configure>", on_frame_configure)
    frame.bind("<MouseWheel>", on_mousewheel)
    frame.bind("<Up>", on_arrow_scroll)
    frame.bind("<Down>", on_arrow_scroll)


scroling(frame_agenda)

# Champ de saisie pour l'événement


day_list = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
moth_list = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
             'Novembre', 'Decembre']

day_list_AN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moth_list_AN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                'November', 'December']


agenda_creation()

# Bouton pour ajouter un événement


# Lancer l'application
app.mainloop()
