import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = evaluate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def evaluate_expression(expression):
    try:
        operands = expression.split('+')
        result = 0
        for operand in operands:
            if '-' in operand:
                sub_operands = operand.split('-')
                sub_result = evaluate_expression(sub_operands[0])
                for sub_operand in sub_operands[1:]:
                    sub_result -= evaluate_expression(sub_operand)
                result += sub_result
            else:
                result += float(operand)
        return result
    except:
        return "Error"

# This is where the window is then created
window = tk.Tk()
window.title("Kyomuhangi Fatuma")

# The input is displayed from here
entry = tk.Entry(window, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "+"
]

row = 1
col = 0

for button in buttons:
    tk.Button(window, text=button, width=5, command=lambda btn=button: button_click(btn)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# We then create a clear button
tk.Button(window, text="C", width=5, command=button_clear).grid(row=row, column=col, padx=5, pady=5)

# The equals button
tk.Button(window, text="=", width=5, command=button_equal).grid(row=row, column=col+1, padx=5, pady=5)

# This following loop is to make sure that we keep doing calculations.
window.mainloop()
