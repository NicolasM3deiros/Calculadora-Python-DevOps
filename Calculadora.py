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
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()