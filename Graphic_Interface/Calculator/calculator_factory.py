import tkinter as tk

def criar_janelinha() -> tk.Tk:
    root = tk.Tk()
    root.title("Dom's Calculator")
    root.config(background='#000', padx=10, pady=10)
    root.resizable(False)
    return root

def make_label(root) -> tk.Label: # Essa função precisa receber um parâmetro da função da janela (creio eu que todas as funções)
    label = tk.Label(root, text='Sem texto ainda', anchor='e', justify='right')
    # Criar grid para a mensagem
    label.grid(row='0', column='0', columnspan='5', sticky='news')
    return label # Sempre retornar a variável no final da função

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row='1', column='0' , columnspan='5', sticky='news', pady=(0, 10))
    display.config(font=('TimesNewRoman', 20, 'bold'), justify='right', bd=1, relief='flat', highlightcolor='#ccc', highlightthickness='1')
    display.bind('<Control-a>', _display_control_a)
    return display # Sempre preciso retornar o parâmetro

def _display_control_a(event): # Precisa ter o evento para pegar o texto e selecioná-lo
    event.widget.select_range() # Esse select_range possui como função principal a 
    event.widget.icursor('end') # Mover o cursor para o fim
    return 'break'