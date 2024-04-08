import tkinter as tk 
import random
def draw_random_line(event):
    x1= random.randint(0, canvas.winfo_width())
    y1= random.randint(0, canvas.winfo_height())
    x2= random.randint(0, canvas.winfo_width())
    y2= random.randint(0, canvas.winfo_height())
    canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
root = tk.Tk()
root.title("Cliquez pour dessiner une ligne aléatoire")
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill='both', expand=True)
canvas.bind("<Button-1>", draw_random_line)
root.mainloop()