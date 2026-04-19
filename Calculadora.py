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

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()