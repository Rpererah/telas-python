import tkinter as tk
from tkinter import messagebox

listaUsuarios=[]

def verificar_login():
    usuario=entry_usuario.get()
    senha=entry_senha.get()
    messagebox.showinfo("Registro", "Registro bem sucedido")
    listaUsuarios.append([usuario,senha])

def mostrar_registros():
    print(listaUsuarios)

#criar uma janela
root=tk.Tk()
root.title("fazer registro")

label_usuario=tk.Label(root, text="Digite o usuario:")
entry_usuario=tk.Entry(root)
label_senha=tk.Label(root, text="Digite a senha")
entry_senha=tk.Entry(root,show="*")
botao_login=tk.Button(root,text="Entrar",command=verificar_login)
botao_mostraRegistros=tk.Button(root,text="Mostrar",command=mostrar_registros)

label_usuario.pack()
entry_usuario.pack()
label_senha.pack()
entry_senha.pack()
botao_login.pack()
botao_mostraRegistros.pack()


largura_tela=800
altura_tela=600

root.geometry(f"{largura_tela}x{altura_tela}" )

#bg tambem pode ser usado em botoes bg fundo fg cor de texto
root.configure(bg="gray")
root.mainloop()