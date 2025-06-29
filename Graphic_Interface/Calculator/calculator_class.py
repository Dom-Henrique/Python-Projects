# A classe servirá para facilitar o desenvolvimento do projeto, abrangendo as funções necessárias para criar a calculadora.
# Lembrando que este aplicativo não possui nenhum

import tkinter as tk # Útil para realizar
from typing import List # 

class Calculator:
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry, buttons: List[List[tk.Button]]):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons