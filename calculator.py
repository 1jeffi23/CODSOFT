import tkinter as tk

expression = ""
def press(symbol):
    global expression
    expression += str(symbol)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, expression)
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, result)
        expression = str(result)
    except:
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, "ERROR")
        expression = ""
def clear():
    global expression
    text_box.delete(1.0, tk.END)
    expression = ""

window = tk.Tk()
window.geometry("633x730")
window.title("Calculator")

text_box = tk.Text(window, height=3, font=("Arial", 18), width=40)
text_box.grid(columnspan=5, padx=10, pady=10, sticky="nsew")

btn1 = tk.Button(window, text="1", font=("Arial", 16), command=lambda: press(1), width=10, height=3)
btn1.grid(column=1, row=2, padx=5, pady=5)

btn2 = tk.Button(window, text="2", font=("Arial", 16), command=lambda: press(2), width=10, height=3)
btn2.grid(column=2, row=2, padx=5, pady=5)

btn3 = tk.Button(window, text="3", font=("Arial", 16), command=lambda: press(3), width=10, height=3)
btn3.grid(column=3, row=2, padx=5, pady=5)

btn4 = tk.Button(window, text="4", font=("Arial", 16), command=lambda: press(4), width=10, height=3)
btn4.grid(column=1, row=3, padx=5, pady=5)

btn5 = tk.Button(window, text="5", font=("Arial", 16), command=lambda: press(5), width=10, height=3)
btn5.grid(column=2, row=3, padx=5, pady=5)

btn6 = tk.Button(window, text="6", font=("Arial", 16), command=lambda: press(6), width=10, height=3)
btn6.grid(column=3, row=3, padx=5, pady=5)

btn7 = tk.Button(window, text="7", font=("Arial", 16), command=lambda: press(7), width=10, height=3)
btn7.grid(column=1, row=4, padx=5, pady=5)

btn8 = tk.Button(window, text="8", font=("Arial", 16), command=lambda: press(8), width=10, height=3)
btn8.grid(column=2, row=4, padx=5, pady=5)

btn9 = tk.Button(window, text="9", font=("Arial", 16), command=lambda: press(9), width=10, height=3)
btn9.grid(column=3, row=4, padx=5, pady=5)

btn0 = tk.Button(window, text="0", font=("Arial", 16), command=lambda: press(0), width=10, height=3)
btn0.grid(column=2, row=5, padx=5, pady=5)

btn_plus = tk.Button(window, text="+", font=("Arial", 16), command=lambda: press("+"), width=10, height=3)
btn_plus.grid(column=4, row=2, padx=5, pady=5)

btn_minus = tk.Button(window, text="-", font=("Arial", 16), command=lambda: press("-"), width=10, height=3)
btn_minus.grid(column=4, row=3, padx=5, pady=5)

btn_div = tk.Button(window, text="/", font=("Arial", 16), command=lambda: press("/"), width=10, height=3)
btn_div.grid(column=4, row=4, padx=5, pady=5)

btn_mul = tk.Button(window, text="*", font=("Arial", 16), command=lambda: press("*"), width=10, height=3)
btn_mul.grid(column=4, row=5, padx=5, pady=5)

btn_rbr = tk.Button(window, text=")", font=("Arial", 16), command=lambda: press(")"), width=10, height=3)
btn_rbr.grid(column=3, row=5, padx=5, pady=5)

btn_rbl = tk.Button(window, text="(", font=("Arial", 16), command=lambda: press("("), width=10, height=3)
btn_rbl.grid(column=1, row=5, padx=5, pady=5)

btn_clear = tk.Button(window, text="C", font=("Arial", 16), command=clear, width=51, height=3)
btn_clear.grid(column=1, row=6, columnspan=5, padx=10, pady=10, sticky="nsew")

btn_equ = tk.Button(window, text="=", font=("Arial", 16), command=evaluate, width=51, height=3)
btn_equ.grid(column=1, row=7, columnspan=5, padx=10, pady=10, sticky="nsew")


window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()






