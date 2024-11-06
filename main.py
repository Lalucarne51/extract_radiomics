from frontend.frontend import RadiomicsGUI  # Importer l'interface graphique
import tkinter as tk

if __name__ == "__main__":
    # Démarrer l'application Tkinter
    root = tk.Tk()
    app = RadiomicsGUI(root)
    root.mainloop()
