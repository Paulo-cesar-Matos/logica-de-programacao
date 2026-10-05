# imports
import turtle
import subprocess
import os

# variaveis do six tema
#Redes
instagram = ("https://www.instagram.com/oliveiramatosp15/")
facebook = ("https://www.facebook.com/profile.php?id=100080909483358")
linkedin = ("https://www.linkedin.com/in/paulo-c%C3%A9sar-matos-658324315/?isSelfProfile=true")

# rickroll 
rickroll = ("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Houseparty
houseparty = ("https://www.youtube.com/watch?v=4lQDepOPeiE")

# pergunta
pergunta = ("https://dontpad.com/nao-sei")

# cat slap
cat_slap = ("https://youtu.be/iym4Y88-a8E?si=nhBxPPms-mDb0wNr")

# exec_tudo - abre todos os exercícios de script
exec_tudo = (f"cmd.exe /c start logica/python/Exerc%C3%ADcios/25.%20procurando%20o%20meu%20primo.py & cmd.exe /c start logica/python/Exerc%C3%ADcios/26.%20for%20fim.py & cmd.exe /c start logica/python/07.%20p_e_q.py")

# spiderman_theme
spiderman_theme = ("https://youtube.com./watch?=Q31M-89uJTY?si=oxw8maPv_GOAp6tI")

# executaveis
chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# caminho do arquivo
arquivo = f"C:\\Users\\{os.getlogin()}\\Documents\\Nova pasta\\meu primo.txt"

# enrique meme audio
enrique = ("https://youtu.be/UztEVUvBtkA?si=zFjxUyAK9DCp904Q&t=4")


print("Sistema Integrado de Preguiça e Desprezo (SIPD)")
print("Selecione uma das opções abaixo:")
input("1 - Procurando o meu primo")
input("2 - O vídeo mais importante do mundo")
input("3 - Playlist de 2 Horas de música de houseparty")
input("4 - Qual a pergunta mais dificil do mundo?")
input("5 - Pessoas quando veem q vc fez a maior merda até agora")
input("6 - Executar todos os execícios de lógica de programação")
input("7 - Desenhar o Homem-Aranha")
input("8 - Enrique")
input("98 - Abrir as redes sociais do criador do script")
input("99 - Sair do sistema")

def gerar_arquivo_para_encontrar():
    # Cria um arquivo de texto com o nome "arquivo.txt"
    with open(arquivo, "w") as f:
        f.write("Você me achou :)))))")
    print("Me acha aí agora kkkk")

def abrir_rede_social():
    # verifica se algum dos navegadores está instalado e abre o link do tema do homem-aranha
    if os.path.exists(chrome):
        subprocess.run([chrome, instagram, facebook, linkedin])
    elif os.path.exists(firefox):
        subprocess.run([firefox, instagram, facebook, linkedin])
    elif os.path.exists(edge):
        subprocess.run([edge, instagram, facebook, linkedin])

def desenhe_o_homem_aranha():
    # creditos: 
    # https://www.youtube.com/shorts/pYJidzHSaME

    # verifica se algum dos navegadores está instalado e abre o link do tema do homem-aranha
    if os.path.exists(chrome):
        subprocess.run([chrome, spiderman_theme])
    elif os.path.exists(firefox):
        subprocess.run([firefox, spiderman_theme])
    elif os.path.exists(edge):
        subprocess.run([edge, spiderman_theme])

    # Set the turtle object
    t = turtle.Turtle()
    scr = turtle.Screen()
    scr.bgcolor("black")
    t.color("red")
    t.speed(5)

    # Draw the head
    t.goto(0, 0)
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    # Draw the body
    t.penup()
    t.setheading(270)
    t.left(60)
    t.pendown()
    t.begin_fill()
    t.forward(20)
    t.right(80)
    t.forward(70)
    t.right(147)
    t.forward(70)
    t.right(80)
    t.forward(20)
    t.penup()
    t.end_fill()

    # Right upper first upper leg
    t.pendown()
    t.goto(10, 35)
    t.pendown()
    t.begin_fill()
    t.left(20)
    t.forward(25)
    t.right(60)
    t.forward(50)
    t.left(120)
    t.forward(80)
    t.right(175)
    t.forward(95)
    t.right(127)
    t.forward(63)
    t.left(60)
    t.forward(18)
    t.end_fill()

    # Right upper second leg
    t.pendown()
    t.goto(13, 25)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.left(90)
    t.forward(20)
    t.right(60)
    t.forward(80)
    t.left(125)
    t.forward(130)
    t.right(175)
    t.forward(145)
    t.right(128)
    t.forward(95)
    t.left(60)
    t.forward(20)
    t.end_fill()
    t.penup()

    # Left first upper leg of the spider
    t.pendown()
    t.goto(-10, 35)
    t.pendown()
    t.begin_fill()
    t.right(80)
    t.forward(25)
    t.left(60)
    t.forward(50)
    t.right(120)
    t.left(175)
    t.forward(95)
    t.left(127)
    t.forward(63)
    t.right(60)
    t.forward(18)
    t.end_fill()

    # Left second upper leg of the spider
    t.pendown()
    t.goto(-13, 25)
    t.pendown()
    t.begin_fill()
    t.right(90)
    t.right(90)
    t.forward(20)
    t.left(60)
    t.forward(80)
    t.right(125)
    t.forward(130)
    t.left(175)
    t.forward(145)
    t.left(128)
    t.forward(95)
    t.right(60)
    t.forward(20)
    t.end_fill()
    t.penup()

    # Right first lower leg of spider
    t.pendown()
    t.goto(15, 12)
    t.left(60)
    t.begin_fill()
    t.forward(20)
    t.right(40)
    t.forward(95)
    t.right(100)
    t.right(135)
    t.right(175)
    t.right(120)
    t.left(90)
    t.forward(80)
    t.left(40)
    t.forward(20)
    t.end_fill()

    # Right second lower leg of the spider
    t.pendown()
    t.goto(11, 8)
    t.left(150)
    t.begin_fill()
    t.forward(25)
    t.right(10)
    t.forward(65)
    t.right(95)
    t.forward(70)
    t.right(175)
    t.right(60)
    t.left(85)
    t.forward(65)
    t.left(15)
    t.forward(15)
    t.end_fill()

    # Left lower first leg of the spider
    t.pendown()
    t.goto(-15, 14)
    t.right(3)
    t.begin_fill()
    t.forward(20)
    t.left(40)
    t.forward(95)
    t.left(100)
    t.left(135)
    t.left(175)
    t.left(120)
    t.right(90)
    t.forward(80)
    t.right(40)
    t.forward(20)
    t.end_fill()
    t.penup()

    # Left lower second leg of the spider
    t.pendown()
    t.goto(-11, 8)
    t.right(90)
    t.right(60)
    t.begin_fill()
    t.forward(25)
    t.left(10)
    t.forward(65)
    t.left(95)
    t.forward(70)
    t.left(175)
    t.left(85)
    t.forward(65)
    t.right(15)
    t.forward(15)
    t.end_fill()

    turtle.hideturtle()
    turtle.done()

    print("ficou horrível, eu sei")