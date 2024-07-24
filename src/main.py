import tkinter as tk

root = tk.Tk()
root.title("Hello World!")
root.geometry("300x200")
root.minsize(width=200, height=100)
root.resizable(width=True, height=True)
# parent, text
label = tk.Label(root, text="Hello World!")
label.pack()
root.mainloop()
