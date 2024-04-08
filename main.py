import tkinter as tk
from ui import IDESimulator

def main():
    root = tk.Tk()
    app = IDESimulator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
