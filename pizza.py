import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Pizza Order")
root.geometry("400x400")

# Variables
size_var = tk.StringVar(value="Medium")
crust_var = tk.StringVar(value="Thin")
toppings_vars = {
    "Cheese": tk.IntVar(),
    "Pepperoni": tk.IntVar(),
    "Mushrooms": tk.IntVar(),
    "Olives": tk.IntVar()
}
drink_var = tk.StringVar()

# --- Widgets ---

# Pizza Size (Radiobuttons)
tk.Label(root, text="Choose Pizza Size:").pack(anchor='w')
for size in ["Small", "Medium", "Large"]:
    tk.Radiobutton(root, text=size, variable=size_var, value=size).pack(anchor='w')

# Crust Type (Radiobuttons)
tk.Label(root, text="Choose Crust Type:").pack(anchor='w')
for crust in ["Thin", "Thick", "Stuffed"]:
    tk.Radiobutton(root, text=crust, variable=crust_var, value=crust).pack(anchor='w')

# Toppings (Checkbuttons)
tk.Label(root, text="Select Toppings:").pack(anchor='w')
for topping, var in toppings_vars.items():
    tk.Checkbutton(root, text=topping, variable=var).pack(anchor='w')

# Drink Selection (Combobox)
tk.Label(root, text="Choose a Drink:").pack(anchor='w')
drink_combo = ttk.Combobox(root, textvariable=drink_var)
drink_combo['values'] = ["Coke", "Sprite", "Water", "No Drink"]
drink_combo.current(0)
drink_combo.pack(anchor='w')

# Submit Button
def submit_order():
    selected_toppings = [t for t, v in toppings_vars.items() if v.get() == 1]
    order_summary = (
        f"Size: {size_var.get()}\n"
        f"Crust: {crust_var.get()}\n"
        f"Toppings: {', '.join(selected_toppings) if selected_toppings else 'None'}\n"
        f"Drink: {drink_var.get()}"
    )
    messagebox.showinfo("Order Summary", order_summary)

ttk.Button(root, text="Place Order", command=submit_order).pack(pady=10)

# Run the app
root.mainloop()