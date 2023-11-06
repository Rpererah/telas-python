import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario=entry_usuario.get()
    senha=entry_senha.get()

    if usuario == "rafael" and senha == "1234":
        # Se o login for bem-sucedido, mostrar uma mensagem de boas-vindas
        messagebox.showinfo("Login", "Login bem-sucedido!")
        # Fechar a janela de login
        root.destroy()
        # Abrir uma nova janela ou realizar qualquer outra ação desejada após o login bem-sucedido
    else:
        # Se o login falhar, mostrar uma mensagem de erro
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos")


#criar uma janela
root=tk.Tk()
root.title("fazer login")

label_usuario=tk.Label(root, text="Digite o usuario:")
entry_usuario=tk.Entry(root)
label_senha=tk.Label(root, text="Digite a senha")
entry_senha=tk.Entry(root,show="*")
botao_login=tk.Button(root,text="Entrar",command=verificar_login)

label_usuario.pack()
entry_usuario.pack()
label_senha.pack()
entry_senha.pack()
botao_login.pack()


largura_tela=800
altura_tela=600

root.geometry(f"{largura_tela}x{altura_tela}" )

#bg tambem pode ser usado em botoes bg fundo fg cor de texto
root.configure(bg="gray")
root.mainloop()