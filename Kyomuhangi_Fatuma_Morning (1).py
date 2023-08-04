import tkinter as tk


def print_receipt():
    # Retrieve input values from the entry fields
    customer_name = name_entry.get()
    item_name = item_entry.get()
    item_price = int(price_entry.get())
    item_quantity = int(quantity_entry.get())
    total = int(item_price * item_quantity)

    # Create the receipt text
    receipt_text = f"Customer: {customer_name}\n\n"
    receipt_text += "Item             Price\n"
    receipt_text += "----------------------------\n"
    receipt_text += f"{item_name}        ${item_price}\n"
    receipt_text += "----------------------------\n"
    receipt_text += f"Quantity:            {item_quantity}\n"
    receipt_text +="----------------------------\n"
    receipt_text += f"Total:           ${total}"

    # Print the receipt
    print(receipt_text)

    # Clear the entry fields
    name_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


# The main window
window = tk.Tk()
window.title("Fatuma's Receipt Machine program ")

# Labels for the input fields
name_label = tk.Label(window, text="Customer Name:")
item_label = tk.Label(window, text="Item:")
price_label = tk.Label(window, text="Amount:")
quantity_label = tk.Label(window, text="Quantity")

# Entry fields for the input values
name_entry = tk.Entry(window)
item_entry = tk.Entry(window)
price_entry = tk.Entry(window)
quantity_entry = tk.Entry(window)
# Button to print the receipt
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)

# Position of the labels, entry fields, and button in the window
name_label.grid(row=0, column=0, sticky="e")
item_label.grid(row=1, column=0, sticky="e")
price_label.grid(row=2, column=0, sticky="e")
quantity_label.grid(row=3, column=0, sticky="e")

name_entry.grid(row=0, column=1, padx=10, pady=5)
item_entry.grid(row=1, column=1, padx=10, pady=5)
price_entry.grid(row=2, column=1, padx=10, pady=5)
quantity_entry.grid(row=3, column=1, padx=10, pady=5)

print_button.grid(row=4, columnspan=2, padx=10, pady=10)

window.mainloop()
