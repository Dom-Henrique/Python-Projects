import tkinter as tk
from calculator_factory import criar_janelinha

def main():
    root = criar_janelinha()
    root.mainloop()
    
if __name__ == "__main__": # Precisa comparar para executar corretamente
    main()