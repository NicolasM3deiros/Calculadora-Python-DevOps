import customtkinter as ctk

# conf tema padrao
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()

        # setup da janela
        self.title("Calculadora")
        self.geometry("300x400")
        self.resizable(False, False)

        # display de resultados
        self.display = ctk.CTkEntry(self, width=280, height=50, font=("Arial", 30), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        self.criar_botoes()

    def criar_botoes(self):
        # mapa dos botoes
        botoes = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        # renderiza a grade e adiciona funcionalidade
        for linha_idx, linha in enumerate(botoes):
            for col_idx, texto in enumerate(linha):
                # expressao lambda para capturar o valor de cada botao
                comando = lambda x=texto: self.clique(x)
                btn = ctk.CTkButton(self, text=texto, width=65, height=50, font=("Arial", 20), command=comando)
                btn.grid(row=linha_idx+1, column=col_idx, padx=5, pady=5)

    def clique(self, valor):
        # limpa o visor
        if valor == 'C':
            self.display.delete(0, 'end')
        # calcula o resultado
        elif valor == '=':
            try:
                expressao = self.display.get()
                resultado = str(eval(expressao))
                self.display.delete(0, 'end')
                self.display.insert(0, resultado)
            except Exception: # trata divisao por zero ou erro de sintaxe
                self.display.delete(0, 'end')
                self.display.insert(0, 'Erro')
        # adiciona o numero/operador no visor
        else:
            self.display.insert('end', valor)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()