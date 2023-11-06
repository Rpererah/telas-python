import tkinter as tk
import csv

# Função para verificar o login
def verificar_login():
    # Obter o nome de usuário e senha inseridos pelo usuário
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Verificar se o nome de usuário e a senha estão corretos
    if usuario == "usuario" and senha == "senha":
        # Se o login for bem-sucedido, mostrar uma mensagem de boas-vindas
        messagebox.showinfo("Login", "Login bem-sucedido!")
        # Adicionar as credenciais à lista
        credenciais.append([usuario, senha])
        # Salvar as credenciais em um arquivo CSV
        salvar_csv(credenciais)
        # Fechar a janela de login
        root.destroy()
        # Abrir uma nova janela ou realizar qualquer outra ação desejada após o login bem-sucedido
    else:
        # Se o login falhar, mostrar uma mensagem de erro
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos")

# Função para salvar as credenciais em um arquivo CSV
def salvar_csv(lista_credenciais):
    with open("credenciais.csv", "w", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        # Escrever as credenciais no arquivo CSV
        escritor.writerows(lista_credenciais)

# Inicializar a lista de credenciais
credenciais = []

# Criar uma janela
root = tk.Tk()
root.title("Login")

# Criar widgets na janela
label_usuario = tk.Label(root, text="Nome de Usuário:")
label_usuario.pack()
entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

botao_login = tk.Button(root, text="Login", command=verificar_login)
botao_login.pack()

# Iniciar o loop de eventos
root.mainloop()
