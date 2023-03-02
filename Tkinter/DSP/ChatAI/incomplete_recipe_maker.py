import tkinter as tk
from tkinter import messagebox
from collections import defaultdict

class RecipeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe App")

        # Create a dictionary to store recipe quantities and descriptions
        self.recipes = defaultdict(list)

        # Create label and entry widgets for recipe quantities and descriptions
        self.quantities_label = tk.Label(master, text="Enter recipe quantities:")
        self.quantities_label.grid(row=0, column=0, padx=5, pady=5)

        self.quantities_entries = []
        self.descriptions_entries = []
        for i in range(2, 6):
            quantity_label = tk.Label(master, text=f"{i} items:")
            quantity_label.grid(row=i, column=0, padx=5, pady=5)
            quantity_entry = tk.Entry(master)
            quantity_entry.grid(row=i, column=1, padx=5, pady=5)
            self.quantities_entries.append(quantity_entry)

            description_label = tk.Label(master, text=f"Description for {i} items:")
            description_label.grid(row=i, column=2, padx=5, pady=5)
            description_entry = tk.Entry(master)
            description_entry.grid(row=i, column=3, padx=5, pady=5)
            self.descriptions_entries.append(description_entry)

        # Create a button to save recipe quantities and descriptions to file
        self.save_button = tk.Button(master, text="Save", command=self.save_recipes)
        self.save_button.grid(row=6, column=3, padx=5, pady=5)

        # Create a button to load all saved recipes
        self.load_button = tk.Button(master, text="Load", command=self.load_recipes)
        self.load_button.grid(row=6, column=2, padx=5, pady=5)

    def save_recipes(self):
        # Get the recipe quantities and descriptions from the entry widgets and store them in the dictionary
        for i, quantity_entry in enumerate(self.quantities_entries):
            try:
                quantity = int(quantity_entry.get())
                description = self.descriptions_entries[i].get()
                self.recipes[i+2].append((quantity, description))
            except ValueError:
                messagebox.showerror("Error", f"Please enter a valid quantity for {i+2} items.")

        # Save the recipe quantities and descriptions to a text file
        with open("recipes.txt", "a") as f:
            for items, quantities_and_descriptions in self.recipes.items():
                for quantity, description in quantities_and_descriptions:
                    f.write(f"{items} items: {quantity} ({description})\n")

        # Clear the entry widgets and recipe dictionary
        for quantity_entry, description_entry in zip(self.quantities_entries, self.descriptions_entries):
            quantity_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
        self.recipes.clear()

        # Show a success message
        messagebox.showinfo("Success", "Recipes saved.")

    def load_recipes(self):
        # Load all saved recipes from the text file and display them in a message box
        with open("recipes.txt", "r") as f:
            recipes = f.read()

        if not recipes:
            messagebox.showwarning("No Recipes", "No recipes have been saved yet.")
        else:
            messagebox.showinfo("Recipes", recipes)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
