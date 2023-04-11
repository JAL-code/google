import tkinter as tk
from tkinter import messagebox
from collections import defaultdict

class RecipeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe App")

        # Create a dictionary to store recipe quantities and descriptions
        self.recipes = defaultdict(list)

        # Create label and entry widgets for recipe quantities
        self.quantities_label = tk.Label(master, text="Enter recipe quantities:")
        self.quantities_label.grid(row=0, column=0, padx=5, pady=5)

        self.quantities_entries = []
        for i in range(1, 6):
            quantity_label = tk.Label(master, text=f"{i}:")
            quantity_label.grid(row=i, column=0, padx=5, pady=5)
            quantity_entry = tk.Entry(master)
            quantity_entry.grid(row=i, column=1, padx=5, pady=5)
            self.quantities_entries.append(quantity_entry)

        # Create label and dropdown widgets for recipe descriptions
        self.descriptions_label = tk.Label(master, text="Enter recipe descriptions:")
        self.descriptions_label.grid(row=0, column=2, padx=5, pady=5)

        self.valid_options = ["eggs", "bacon", "cheese", "tomatoes", "peppers", "onions", "grits", "bread roll", "steak", "chicken", "hash browns", "corn beef hash", "honey", "butter", "jelly", "olive oil", "ketchup"]
        self.descriptions_menus = []
        for i in range(1, 6):
            description_label = tk.Label(master, text=f"{i} items:")
            description_label.grid(row=i, column=2, padx=5, pady=5)
            description_var = tk.StringVar(value=self.valid_options[0])
            description_menu = tk.OptionMenu(master, description_var, *self.valid_options)
            description_menu.grid(row=i, column=3, padx=5, pady=5)
            self.descriptions_menus.append(description_var)

        # Create a button to save recipe quantities and descriptions to file
        self.save_button = tk.Button(master, text="Save", command=self.save_recipes)
        self.save_button.grid(row=6, column=3, padx=5, pady=5)

        # Create a button to load all saved recipes
        self.load_button = tk.Button(master, text="Load", command=self.load_recipes)
        self.load_button.grid(row=6, column=2, padx=5, pady=5)

    def save_recipes(self):
        # Get the recipe quantities and descriptions from the entry and dropdown widgets and store them in the dictionary
        for i, quantity_entry in enumerate(self.quantities_entries):
            try:
                quantity = int(quantity_entry.get())
                description = self.descriptions_menus[i].get()
                self.recipes[i+2].append((quantity, description))
            except ValueError:
                messagebox.showerror("Error", f"Please enter a valid quantity for {i+2} items.")

        # Save the recipe quantities and descriptions to a text file
        with open("recipes.txt", "a") as f:
            for items, quantities_and_descriptions in self.recipes.items():
                for quantity, description in quantities_and_descriptions:
                    f.write(f"{items} items: {quantity} ({description})\n")

        # Clear the combobox and entry widgets and recipe dictionary
        for quantity_entry, description_menu in zip(self.quantities_entries, self.descriptions_menus):
            quantity_entry.delete(0, tk.END)
            description_menu.set(self.valid_options[0])
        self.recipes.clear()

        # Show a success message
        messagebox.showinfo("Success", "Recipe quantities saved.")


    def load_recipes(self):
        # Create a new window to display the saved recipes
        self.load_window = tk.Toplevel(self.master)
        self.load_window.title("Saved Recipes")

        # Create a text widget to display the saved recipes
        self.load_text = tk.Text(self.load_window, height=20, width=50)
        self.load_text.pack(padx=5, pady=5)

        # Load the saved recipes from the text file and display them in the text widget
        with open("recipes.txt", "r") as f:
            saved_recipes = f.read()
            self.load_text.insert(tk.END, saved_recipes)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
