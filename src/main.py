import tkinter as tk

root = tk.Tk()
root.title("Hello World!")
root.geometry("300x200")
root.minsize(width=200, height=100)
root.resizable(width=True, height=True)
# parent, text
label = tk.Label(root, text="Hello World longer!", bg="red")
label.pack(side="top", fill="y", expand=True)
label2 = tk.Label(root, text="Hello World!", bg="blue")
label2.pack(sid="bottom")
root.mainloop()
