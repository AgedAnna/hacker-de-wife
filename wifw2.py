import tkinter as tk
from tkinter import messagebox
from WIFW import obter_senha_wifi

# função que é chamada quando o botão é clicado
def exibir_senha_wifi():
    nome_rede = nome_rede_entry.get() # obter o nome da rede Wi-Fi do campo de entrada
    senha = obter_senha_wifi(nome_rede) # obter a senha da rede Wi-Fi
    if senha:
        messagebox.showinfo("Senha da rede Wi-Fi", f"A senha da rede Wi-Fi é: {senha}")
    else:
        messagebox.showerror("Erro", "Não foi possível obter a senha da rede Wi-Fi.")

# criar a janela
janela = tk.Tk()
janela.title("Obter senha da rede Wi-Fi")

# criar o campo de entrada para o nome da rede Wi-Fi
nome_rede_label = tk.Label(janela, text="Nome da rede Wi-Fi:")
nome_rede_label.grid(row=0, column=0)
nome_rede_entry = tk.Entry(janela)
nome_rede_entry.grid(row=0, column=1)

# criar o botão para exibir a senha da rede Wi-Fi
exibir_senha_button = tk.Button(janela, text="Exibir senha", command=exibir_senha_wifi)
exibir_senha_button.grid(row=1, column=0, columnspan=2)

# iniciar a janela
janela.mainloop()
