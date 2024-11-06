import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sys
import csv
import os
from backend.backend import Processing  # Import des fonctionnalités du back-end

class RedirectOutputToGUI:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        self.text_widget.update_idletasks()  # Met à jour l'affichage de la zone de texte

    def flush(self):
        pass

class RadiomicsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Extraction des paramètres radiomiques")
        self.root.geometry("800x600")
        self.csv_path_var = tk.StringVar()
        self.categories = {
            "firstorder": tk.BooleanVar(),
            "glcm": tk.BooleanVar(),
            "gldm": tk.BooleanVar(),
            "glrlm": tk.BooleanVar(),
            "glszm": tk.BooleanVar(),
            "ngtdm": tk.BooleanVar(),
            "shape": tk.BooleanVar(),
        }

        # Configuration de l'interface utilisateur
        self.setup_gui()

    def setup_gui(self):
        # Configuration des éléments GUI
        tk.Label(self.root, text="Fichier CSV :").pack(pady=5)
        tk.Entry(self.root, textvariable=self.csv_path_var, width=60).pack(pady=5)
        tk.Button(self.root, text="Charger CSV", command=self.load_csv_file).pack(pady=5)

        # Ajouter des cases à cocher pour les catégories
        tk.Label(self.root, text="Sélectionnez les catégories de paramètres :").pack(pady=5)
        for category in self.categories:
            tk.Checkbutton(self.root, text=category, variable=self.categories[category]).pack(anchor="w")

        tk.Button(self.root, text="Extraction des paramètres radiomiques", command=self.run_extraction).pack(pady=5)

        # Zone de texte pour afficher les résultats et messages
        log_frame = tk.Frame(self.root)
        log_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.log_text = tk.Text(log_frame, height=15, state="normal")
        self.log_text.pack(fill="both", expand=True)

        # Rediriger la sortie standard vers l'interface
        sys.stdout = RedirectOutputToGUI(self.log_text)

    def load_csv_file(self):
        file_path = filedialog.askopenfilename(title="Choisir un fichier CSV", filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            self.csv_path_var.set(file_path)

    def save_csv_file(self, results):
        if results:
            # Obtenir le chemin du fichier CSV d'origine
            original_csv_path = self.csv_path_var.get()
            # Générer le nom du fichier de résultats
            output_csv_file = os.path.splitext(original_csv_path)[0] + "_results.csv"

            # Écrire les résultats dans le fichier CSV
            keys = results[0].keys()
            with open(output_csv_file, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(results)

            self.log_text.insert(tk.END, f"Résultats sauvegardés dans : {output_csv_file}\n")

    def run_extraction(self):
        selected_categories = [cat for cat, var in self.categories.items() if var.get()]
        if not selected_categories:
            print("Veuillez sélectionner au moins une catégorie.")
            return

        try:
            processing_instance = Processing(self.csv_path_var.get(), "path_to_resampled_mask_directory")
            results = processing_instance.extract_radiomics_features(categories=selected_categories)
            self.display_results(results)
            self.save_csv_file(results)
            self.log_text.insert(tk.END, "Extraction terminée.\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"Erreur lors de l'extraction : {e}\n")


    def display_results(self, results):
        for result in results:
            self.log_text.insert(tk.END, f"Image: {result.get('Image', 'N/A')}\n")
            self.log_text.insert(tk.END, f"Mask: {result.get('Mask', 'N/A')}\n")
            self.log_text.insert(tk.END, "-" * 50 + "\n")

        # Afficher chaque caractéristique
        for key, value in result.items():
            if key not in ["Image", "Mask"]:
                self.log_text.insert(tk.END, f"{key}: {value}\n")
        self.log_text.insert(tk.END, "\n" + "=" * 50 + "\n\n")
