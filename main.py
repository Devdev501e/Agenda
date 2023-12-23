# Utilisation de exec() pour exécuter un autre fichier Python
file_to_execute = "Agenda.py"

try:
    with open(file_to_execute, "r") as file:
        code = file.read()
        exec(code)
except FileNotFoundError:
    print(f"Le fichier {file_to_execute} n'a pas été trouvé.")
except Exception as e:
    print(f"Une erreur s'est produite lors de l'exécution du fichier {file_to_execute}: {e}")