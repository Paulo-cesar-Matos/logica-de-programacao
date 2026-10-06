# imports
import turtle
import subprocess
import os
import tkinter as tk

# variaveis do six tema
#Redes
instagram = "https://www.instagram.com/oliveiramatosp15/"
facebook = "https://www.facebook.com/profile.php?id=100080909483358"
linkedin = "https://www.linkedin.com/in/paulo-c%C3%A9sar-matos-658324315/?isSelfProfile=true"

# rickroll 
rickroll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Houseparty
houseparty_url = "https://www.youtube.com/watch?v=4lQDepOPeiE"

# pergunta
pergunta = "https://dontpad.com/nao-sei"

# cat slap
cat_slap = "https://youtu.be/iym4Y88-a8E?si=nhBxPPms-mDb0wNr"

# exec_tudo - abre todos os exercícios de script
exec_tudo = f"C:\\Users\\{os.getlogin()}\\Documents\\GitHub\\aprendendo-python\\logica\\powershell\\exec-tudo.ps1"

# spiderman_theme
spiderman_theme = "https://youtu.be/RWa6YaPH4jY?si=Akbd1XLcCWmOfET8&t=74"

# executaveis
chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# caminho do arquivo
arquivo = f"C:\\Users\\{os.getlogin()}\\Documents\\Nova pasta\\meu primo.txt"

# enrique meme audio
enrique = "https://youtu.be/UztEVUvBtkA?si=zFjxUyAK9DCp904Q&t=4"

figure09 = "https://youtu.be/LpC0SKU6O00?si=ZqcaHlEeg3PjX8bI&t=48"

print("Sistema Integrado de Preguiça e Desprezo (SIPD)")
print("Selecione uma das opções abaixo:")
print("1 - Procurando o meu primo")
print("2 - O vídeo mais importante do mundo")
print("3 - Playlist de 2 Horas de música de houseparty")
print("4 - Qual a pergunta mais dificil do mundo?")
print("5 - Pessoas quando veem q vc fez a maior merda até agora")
print("6 - Executar todos os execícios de lógica de programação")
print("7 - Desenhar o Homem-Aranha")
print("8 - Enrique")
print("9 - Veja como eu sou um polar bear")
print("98 - Abrir as redes sociais do criador do script")
print("99 - Sair do sistema")

def abrir_navegador(*urls: str):
    if os.path.exists(chrome):
        subprocess.run([chrome] + list(urls))
    elif os.path.exists(firefox):
        subprocess.run([firefox] + list(urls))
    elif os.path.exists(edge):
        subprocess.run([edge] + list(urls))
    else:
        print("Nenhum navegador suportado foi encontrado.")

# Global variables for animation
x, y = 0, 0
dx, dy = 4, 4
frame_idx = 0

while True:
    teclado = input("\nDigite a opção desejada: ").strip()
    
    if teclado == '1':
        # Cria um arquivo de texto com o nome "arquivo.txt"
        os.makedirs(os.path.dirname(arquivo), exist_ok=True)
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write("Você me achou :)))))")
        print("Me acha aí agora kkkk")
        
    elif teclado == '2':
        abrir_navegador(rickroll)
        
    elif teclado == '3':
        abrir_navegador(houseparty_url)
        
    elif teclado == '4':
        abrir_navegador(pergunta)
        
    elif teclado == '5':
        abrir_navegador(cat_slap)
        
    elif teclado == '6':
        #Atenção
        if os.path.exists(exec_tudo):
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", exec_tudo])
        else:
            print(f"Arquivo não encontrado: {exec_tudo}")
            
    elif teclado == '7':
        abrir_navegador(spiderman_theme)

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
        
    elif teclado == '8':
        abrir_navegador(enrique)
        
    elif teclado == '9':
        abrir_navegador(figure09)
        # Janela
        janela = tk.Tk()
        janela.overrideredirect(True)
        janela.wm_attributes("-topmost", True) # type: ignore

        frames = []
        i = 0

        while True:
            try:
                frames.append(tk.PhotoImage(file="C:\\Users\\paulomatos\\Documents\\GitHub\\aprendendo-python\\logica\\python\\teste.gif", format=f"gif -index {i}"))  # type: ignore
                i += 1
            except tk.TclError:
                break

        if not frames:
            print("Não foi possível carregar a imagem teste.gif")
            janela.destroy()
            continue

        label = tk.Label(janela)
        label.pack()

        # Permite fechar a janela ao clicar nela, evitando que fique presa na tela
        janela.bind("<Button-1>", lambda e: janela.destroy())
        label.bind("<Button-1>", lambda e: janela.destroy())

        x, y = 0, 0 
        dx, dy = 4, 4 
        frame_idx = 0

        def mover():
            global x, y, dx, dy, frame_idx
            
            # Se a janela foi destruída, para a animação
            if not janela.winfo_exists():
                return

            w = janela.winfo_screenwidth()
            h = janela.winfo_screenheight()

            img = frames[frame_idx] # type: ignore
            iw = img.width() # type: ignore
            ih = img.height() # type: ignore

            x += dx
            y += dy

            if x <= 0 or x + iw >= w:
                dx *= -1

            if y <= 0 or y + ih >= h:
                dy *= -1

            frame_idx = (frame_idx + 1) % len(frames) # type: ignore
            label.config(image=frames[frame_idx]) # type: ignore

            janela.geometry(f"+{x}+{y}")
            janela.after(20, mover)

        mover()
        janela.mainloop()
        
    elif teclado == '98':
        abrir_navegador(instagram, facebook, linkedin)
        
    elif teclado == '99':
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")