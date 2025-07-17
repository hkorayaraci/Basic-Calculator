import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("600x450")
window.configure(bg="light blue")

entry = tk.Entry(window, width=30, borderwidth=5, font=("bold", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()

        expression = expression.replace('x', '*')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


btn = tk.Button(window, text="7", padx=25, pady=25, command=lambda: button_click(7))
btn.grid(row=1, column=0)

btn2 = tk.Button(window, text="8", padx=25, pady=25, command=lambda: button_click(8))
btn2.grid(row=1, column=1)

btn3 = tk.Button(window, text="9", padx=25, pady=25, command=lambda: button_click(9))
btn3.grid(row=1, column=2)

btn4 = tk.Button(window, text="4", padx=25, pady=25, command=lambda: button_click(4))
btn4.grid(row=2, column=0)

btn5 = tk.Button(window, text="5", padx=25, pady=25, command=lambda: button_click(5))
btn5.grid(row=2, column=1)

btn6 = tk.Button(window, text="6", padx=25, pady=25, command=lambda: button_click(6))
btn6.grid(row=2, column=2)

btn7 = tk.Button(window, text="7", padx=25, pady=25, command=lambda: button_click(7))
btn7.grid(row=3, column=0)

btn8 = tk.Button(window, text="8", padx=25, pady=25, command=lambda: button_click(8))
btn8.grid(row=3, column=1)

btn9 = tk.Button(window, text="9", padx=25, pady=25, command=lambda: button_click(9))
btn9.grid(row=3, column=2)

btn0 = tk.Button(window, text="0", padx=25, pady=25, command=lambda: button_click(0))
btn0.grid(row=4, column=0)

btn_plus = tk.Button(window, text="+", padx=25, pady=25, command=lambda: button_click('+'))
btn_plus.grid(row=1, column=3)

btn_minus = tk.Button(window, text="-", padx=25, pady=25, command=lambda: button_click('-'))
btn_minus.grid(row=2, column=3)

btn_divide = tk.Button(window, text="/", padx=25, pady=25, command=lambda: button_click('/'))
btn_divide.grid(row=3, column=3)

btn_multiply = tk.Button(window, text="x", padx=25, pady=25, command=lambda: button_click('x'))
btn_multiply.grid(row=4, column=3)

btn_equal = tk.Button(window, text="=", padx=25, pady=25, command=button_equal)
btn_equal.grid(row=4, column=2)

btn_clear = tk.Button(window, text="C", padx=25, pady=25, command=button_clear)
btn_clear.grid(row=4, column=1)

window.mainloop()
