import tkinter as tk

def criar_janelinha() -> tk.Tk:
    root = tk.Tk()
    root.title("Calculator")
    root.config(padx=10, pady=10, background='#000') # Vai configurar o espaçamento
    root.resizable(False, False)
    root.mainloop
    return root

def make_label(root) -> tk.Label: # Essa função servirá para definir a mensagem que aparece no topo
    label = tk.Label(root, text='')