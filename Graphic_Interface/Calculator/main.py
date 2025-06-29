import tkinter as tk
from calculator_factory import *

def main():
    root = criar_janelinha()
    label = make_label()
    root.mainloop()
    
if __name__ == "__main__": # Precisa comparar para executar corretamente
    main()