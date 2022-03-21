from relogio import Telaprincipal
import tkinter as tk

try:
    janelaRaiz = tk.Tk()
    Telaprincipal(janelaRaiz)
    janelaRaiz.mainloop()
except Exception as E:
    print(E.__class__())
    print(E)
