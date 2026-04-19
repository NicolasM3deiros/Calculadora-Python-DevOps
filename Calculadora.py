import customtkinter as ctk
import math

# conf tema padrao
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()

        # setup da janela
        self.title("Calculadora")
        self.geometry("320x460")
        self.resizable(False, False)

        # display de resultados
        self.display = ctk.CTkEntry(self, width=300, height=60, font=("Arial", 40), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

        self.criar_botoes()

        # ativa a captura do teclado fisico
        self.bind("<Key>", self.tratar_teclado)
        self.focus_set() # Mantem o foco na janela principal

    def criar_botoes(self):
        # mapa dos botoes no padrao Windows
        botoes = [
            ['%', 'CE', 'C', '⌫'],
            ['1/x', 'x²', '√x', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]

        # renderiza a grade e adiciona funcionalidade
        for linha_idx, linha in enumerate(botoes):
            for col_idx, texto in enumerate(linha):
                comando = lambda x=texto: self.clique(x)
                
                # destaca o botao de igual
                cor = "#1f6aa5" if texto == "=" else "transparent" if texto not in "0123456789." else None
                
                btn = ctk.CTkButton(self, text=texto, width=70, height=50, font=("Arial", 18), 
                                    command=comando, fg_color=cor, border_width=1 if cor == "transparent" else 0)
                btn.grid(row=linha_idx+1, column=col_idx, padx=3, pady=3)

    def clique(self, valor):
        expressao = self.display.get()

        try:
            # limpa tudo
            if valor in ('C', 'CE'):
                self.display.delete(0, 'end')
            
            # apaga o ultimo caractere
            elif valor == '⌫':
                self.display.delete(len(expressao)-1, 'end')
            
            # calcula o resultado
            elif valor == '=':
                resultado = str(eval(expressao))
                self.display.delete(0, 'end')
                self.display.insert(0, resultado)
            
            # operacoes avancadas
            elif valor == 'x²':
                resultado = str(eval(expressao) ** 2)
                self.display.delete(0, 'end')
                self.display.insert(0, resultado)
            
            elif valor == '√x':
                resultado = str(math.sqrt(eval(expressao)))
                self.display.delete(0, 'end')
                self.display.insert(0, resultado)
            
            elif valor == '1/x':
                resultado = str(1 / eval(expressao))
                self.display.delete(0, 'end')
                self.display.insert(0, resultado)
            
            elif valor == '%':
                resultado = str(eval(expressao) / 100)
                self.display.delete(0, 'end')
                self.display.insert(0, resultado)
            
            # inverte o sinal
            elif valor == '+/-':
                if expressao.startswith('-'):
                    self.display.delete(0, 1)
                else:
                    self.display.insert(0, '-')
            
            # adiciona o numero/operador no visor
            else:
                self.display.insert('end', valor)
                
        except Exception: # trata divisoes por zero ou formatacoes invalidas
            self.display.delete(0, 'end')
            self.display.insert(0, 'Erro')

    # Nova funcao para traduzir o teclado para cliques virtuais
    def tratar_teclado(self, event):
        tecla = event.char
        tecla_especial = event.keysym

        # Mapeia teclas especiais para as strings que a funcao clique() ja entende
        if tecla_especial == "Return":
            self.clique('=')
        elif tecla_especial == "BackSpace":
            self.clique('⌫')
        elif tecla_especial == "Escape":
            self.clique('C')
        # Se for um numero ou operador matematico padrao
        elif tecla in '0123456789.+-*/':
            self.clique(tecla)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()