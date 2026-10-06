import tkinter as tk

janela = tk.Tk()
janela.overrideredirect(True)
janela.wm_attributes("-topmost", True) #type: ignore

frames = []
i = 0

import os

caminho_gif = os.path.join(os.path.dirname(os.path.abspath(__file__)), "teste.gif")
while True:
    try:
        frames.append(tk.PhotoImage(file=caminho_gif, format=f"gif -index {i}")) #type: ignore
        i += 1
    except tk.TclError:
        break

frame = 0

label = tk.Label(janela)
label.pack()

x, y = 0, 0
dx, dy = 4, 4

def mover():
    global x, y, dx, dy, frame

    w = janela.winfo_screenwidth()
    h = janela.winfo_screenheight()

    img = frames[frame] #type: ignore
    iw = img.width() #type: ignore
    ih = img.height() #type: ignore

    x += dx
    y += dy

    if x <= 0 or x + iw >= w:
        dx *= -1

    if y <= 0 or y + ih >= h:
        dy *= -1

    frame = (frame + 1) % len(frames) #type: ignore
    label.config(image=frames[frame]) #type: ignore

    janela.geometry(f"+{x}+{y}")
    janela.after(20, mover)

mover()
janela.mainloop()