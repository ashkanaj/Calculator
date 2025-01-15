import tkinter as tk

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("600x450")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        result_display = tk.Entry(self.master, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        result_display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        clear_button = tk.Button(self.master, text="C", font=("Arial", 18), command=self.clear, width=10, height=2)
        clear_button.grid(row=5, column=0, columnspan=4)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t), width=10, height=2)
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        current = self.result_var.get()
        if char == "=":
            try:
                result = str(eval(current))
                self.result_var.set(result)
            except Exception:
                self.result_var.set(":(")
        else:
            self.result_var.set(current + char)

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    view = View(root)
    root.mainloop()
