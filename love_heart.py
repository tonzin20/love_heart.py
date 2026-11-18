import turtle
import random
import math
import time

frases = [
    "I love you", "Te amo", "Ti amo",
    "Je t'aime", "Love you", "Amo-te",
    "Ich liebe dich", "Te quiero",
    "Kocham cie", "Saranghae",
    "Ik hou van jou", "Eu te amo",
    "Seni seviyorum", "Anh yeu em",
]

cores = ["red", "tomato", "coral", "salmon", "crimson", "orangered"]

tela = turtle.Screen()
tela.setup(1900, 900)
tela.bgcolor("black")
tela.title("LOVE HEART ❤️")
tela.tracer(0)

caneta = turtle.Turtle()
caneta.hideturtle()
caneta.penup()

ESCALA = 300      # tamanho base do coração
DESLOC_Y = -30    # centraliza verticalmente
PASSO_X = 95      # espaço horizontal entre frases
PASSO_Y = 17      # espaço vertical entre linhas
BATIMENTO = 1.0   # duração de um ciclo (segundos)
FPS_MS = 33       # ~30 quadros por segundo


def dentro_coracao(x, y):
    return (x * x + y * y - 1) ** 3 - x * x * y ** 3 <= 0
 

# Gera os pontos UMA vez (posição normalizada, texto e cor fixos)
pontos = []
linha = 0
for y in range(-330, 400, PASSO_Y):
    inicio = -400 + (PASSO_X // 2 if linha % 2 else 0)
    for x in range(inicio, 401, PASSO_X):
        px = x / ESCALA
        py = (y - DESLOC_Y) / ESCALA
        if dentro_coracao(px, py):
            pontos.append((px, py, random.choice(frases), random.choice(cores)))
    linha += 1


def pulso(t):
    """Duas batidas seguidas ("tum-tum") e depois um descanso."""
    f = (t % BATIMENTO) / BATIMENTO
    b1 = math.exp(-((f - 0.10) / 0.05) ** 2)
    b2 = 0.7 * math.exp(-((f - 0.30) / 0.06) ** 2)
    return 1 + 0.10 * (b1 + b2)


inicio_tempo = time.time()
rodando = True


def quadro():
    if not rodando:
        return
    s = pulso(time.time() - inicio_tempo)
    tamanho = max(6, round(8 * s))

    caneta.clear()
    for px, py, frase, cor in pontos:
        caneta.goto(px * ESCALA * s, py * ESCALA * s + DESLOC_Y)
        caneta.color(cor)
        caneta.write(frase, align="center", font=("Arial", tamanho, "bold"))
    tela.update()
    tela.ontimer(quadro, FPS_MS)


def sair():
    global rodando
    rodando = False
    tela.bye()


tela.listen()
tela.onkey(sair, "Escape")   # ESC fecha a janela
quadro()
turtle.done()