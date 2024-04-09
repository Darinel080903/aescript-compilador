import tkinter as tk

import sintaxis
from generate_code import generate_python_code
import generate_code
from lexer import lexer
import re

from sintaxis import parser


class IDESimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple IDE Simulator")
        self.text_widget = tk.Text(root, height=15, width=50)
        self.text_widget.pack()
        self.validate_button = tk.Button(root, text="Validate", command=self.validate_code)
        self.validate_button.pack()
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()
        self.console_text = tk.Text(root, height=10, width=50)
        self.console_text.pack()


    def validate_code(self):
        generate_code.variables = []
        generate_code.value_variables = []
        self.result_text.delete("1.0", tk.END)
        self.console_text.delete("1.0", tk.END)
        self.console_text.insert(tk.END, "Console output:\n")
        code = self.text_widget.get("1.0", tk.END)
        code = code.replace("\n", "")
        tokens_info = self.analyze_code(code)
        parsed_output = parser.parse(code)
        if sintaxis.error_message is not None:
            parser_result = sintaxis.error_message
            self.result_text.insert(tk.END, f"Parser result: {parser_result}\n")
            sintaxis.error_message = None
        else:
            parser_result = "No se encontraron errores de sintaxis."
            self.result_text.insert(tk.END, f"Parser result: {parser_result}\n")
            self.result_text.insert(tk.END, "Lexer result:\n")
            for token_info in tokens_info:
                self.result_text.insert(tk.END, f"{token_info}\n")
        python_code = generate_python_code(parsed_output)
        if type(python_code) == list:
            self.result_text.insert(tk.END, "\n")
            for code in python_code:
                fl_text = eval(code)
                self.console_text.insert(tk.END, f"{fl_text}\n")
        else:
            try:
                final_code = eval(python_code) #"No se declaro";
                print(final_code)
                self.console_text.insert(tk.END, f"\n{final_code}")
            except:
                self.console_text.insert(tk.END, f"\n{python_code}")

    def analyze_code(self, code):
        lexer.input(code)
        tokens_info = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens_info.append(f"Token: {tok.type}, Value: {tok.value}")
        return tokens_info


if __name__ == "__main__":
    root = tk.Tk()
    ide = IDESimulator(root)
    root.mainloop()
