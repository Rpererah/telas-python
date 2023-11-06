import tkinter as tk
import random

# Configurações do jogo
largura_janela = 800
altura_janela = 600
velocidade_bola = 5
velocidade_paleta = 20


# Função para mover as paletas
def mover_paletas(event):
    tecla = event.keysym
    if tecla == "w":
        canvas.move(paleta_esquerda, 0, -velocidade_paleta)
    elif tecla == "s":
        canvas.move(paleta_esquerda, 0, velocidade_paleta)
    elif tecla == "Up":
        canvas.move(paleta_direita, 0, -velocidade_paleta)
    elif tecla == "Down":
        canvas.move(paleta_direita, 0, velocidade_paleta)

# Função para mover a bola
def mover_bola():
    global dx, dy
    canvas.move(bola, dx, dy)
    posicao_bola = canvas.coords(bola)
    # Obter a posição da paleta esquerda
    posicao_paleta_esquerda = canvas.coords(paleta_esquerda)
    # Obter a posição da paleta direita
    posicao_paleta_direita = canvas.coords(paleta_direita)


    if posicao_bola[1] <= 0 or posicao_bola[3] >= altura_janela:
        dy *= -1
    if posicao_bola[0] <= 0:
        reiniciar_jogo()
    if posicao_bola[2] >= largura_janela:
        dx *= -1
    if (posicao_bola[0] <= posicao_paleta_esquerda[2] and posicao_paleta_esquerda[1] <= posicao_bola[1] <= posicao_paleta_esquerda[3]) or \
       (posicao_bola[2] >= posicao_paleta_direita[0] and posicao_paleta_direita[1] <= posicao_bola[1] <= posicao_paleta_direita[3]):
        dx *= -1

    root.after(velocidade_bola, mover_bola)

# Função para reiniciar o jogo
def reiniciar_jogo():
    canvas.coords(bola, largura_janela/2 - 15, altura_janela/2 - 15, largura_janela/2 + 15, altura_janela/2 + 15)
    global dx, dy
    dx = random.choice((1, -1)) * velocidade_bola
    dy = random.choice((1, -1)) * velocidade_bola

# Criar uma janela
root = tk.Tk()
root.title("Pong")

# Configurar o canvas
canvas = tk.Canvas(root, width=largura_janela, height=altura_janela, bg="black")
canvas.pack()

# Criar as paletas
paleta_esquerda = canvas.create_rectangle(20, altura_janela/2 - 60, 40, altura_janela/2 + 60, fill="white")
paleta_direita = canvas.create_rectangle(largura_janela - 40, altura_janela/2 - 60, largura_janela - 20, altura_janela/2 + 60, fill="white")

# Criar a bola
bola = canvas.create_oval(largura_janela/2 - 15, altura_janela/2 - 15, largura_janela/2 + 15, altura_janela/2 + 15, fill="white")

# Inicializar a direção da bola de forma aleatória
dx = random.choice((1, -1)) * velocidade_bola
dy = random.choice((1, -1)) * velocidade_bola

# Vincular eventos de teclado para mover as paletas
root.bind("<Key>", mover_paletas)

# Iniciar o movimento da bola
mover_bola()

# Iniciar o loop de eventos
root.mainloop()
