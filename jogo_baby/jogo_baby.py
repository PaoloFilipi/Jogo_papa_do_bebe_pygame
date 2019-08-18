import pygame as pg
import os #para centralizar a tela
import sys
import random
import time
import sys
from tkinter import *
from tkinter import messagebox

#Paolo   Tia: 41880171
#Edivan  Tia: 41882091



#Variáveis globais
score = 0
cont = 0
inicio = 0
fim = 0
duracao = 0
vidas = 3
flag = 0
seg = 200
seg2 = 500
estado_bebe = 0

#Display do cronômetro e score
fundoDisplay = pg.image.load("img/displays/retangulo_tempo_pontos.png")

#Fonte usada
pg.font.init()
fonte = "Love Like This"
fonteText = pg.font.SysFont(fonte, 35)

#Colheres
colher = pg.image.load("img/colheres/colher.png")
risca_colher = pg.image.load("img/colheres/colher1.png")

#Objetos não comestível
chave = pg.image.load("img/comidas/absurdos/chave.png")
globo = pg.image.load("img/comidas/absurdos/globo.png")
lampada = pg.image.load("img/comidas/absurdos/lampada.png")
lente = pg.image.load("img/comidas/absurdos/lente.png")
livro = pg.image.load("img/comidas/absurdos/livro.png")
pote_racao = pg.image.load("img/comidas/absurdos/pote_racao.png")
quimica = pg.image.load("img/comidas/absurdos/quimica.png")
rato = pg.image.load("img/comidas/absurdos/rato.png")
relogio = pg.image.load("img/comidas/absurdos/relogio.png")
trofeu = pg.image.load("img/comidas/absurdos/trofeu.png")
veneno = pg.image.load("img/comidas/absurdos/veneno.png")

#Alimentos não saudáveis
batata_frita = pg.image.load("img/comidas/nao_saudaveis/batata_frita.png")
bolo = pg.image.load("img/comidas/nao_saudaveis/brigadeiro.png")
brigadeiro = pg.image.load("img/comidas/nao_saudaveis/batata_frita.png")
chocolate = pg.image.load("img/comidas/nao_saudaveis/chocolate.png")
cupcake = pg.image.load("img/comidas/nao_saudaveis/cupcake.png")
gummie = pg.image.load("img/comidas/nao_saudaveis/gummie.png")
hotdog = pg.image.load("img/comidas/nao_saudaveis/hotdog.png")
pirulito = pg.image.load("img/comidas/nao_saudaveis/pirulito.png")
pizza = pg.image.load("img/comidas/nao_saudaveis/pizza.png")
refrigerante = pg.image.load("img/comidas/nao_saudaveis/refrigerante.png")
rosquinhas = pg.image.load("img/comidas/nao_saudaveis/rosquinhas.png")
salgadinho = pg.image.load("img/comidas/nao_saudaveis/salgadinho.png")
sorvete = pg.image.load("img/comidas/nao_saudaveis/sorvete.png")

#Alimentos saudáveis
abacate = pg.image.load("img/comidas/saudaveis/abacate.png")
banana = pg.image.load("img/comidas/saudaveis/banana.png")
beringela = pg.image.load("img/comidas/saudaveis/beringela.png")
brocolis = pg.image.load("img/comidas/saudaveis/brocolis.png")
cenoura = pg.image.load("img/comidas/saudaveis/cenoura.png")                        
churrasco = pg.image.load("img/comidas/saudaveis/churrasco.png")
coco = pg.image.load("img/comidas/saudaveis/coco.png")
kiwi = pg.image.load("img/comidas/saudaveis/kiwi.png")
laranja = pg.image.load("img/comidas/saudaveis/laranja.png")
leite = pg.image.load("img/comidas/saudaveis/leite.png")
limao = pg.image.load("img/comidas/saudaveis/limao.png")
maca = pg.image.load("img/comidas/saudaveis/maca.png")
maca2 = pg.image.load("img/comidas/saudaveis/maca2.png")
melancia = pg.image.load("img/comidas/saudaveis/melancia.png")
milho = pg.image.load("img/comidas/saudaveis/milho.png")
morango = pg.image.load("img/comidas/saudaveis/morango.png")
ovo = pg.image.load("img/comidas/saudaveis/ovo.png")
pedaco_melancia = pg.image.load("img/comidas/saudaveis/pedaco_melancia.png")
pera = pg.image.load("img/comidas/saudaveis/pera.png")
queijo = pg.image.load("img/comidas/saudaveis/queijo.png")
salada = pg.image.load("img/comidas/saudaveis/salada.png")

#Bebê feliz
bebe_feliz1 = pg.image.load("img/bb_feliz/bb_feliz_1.png")
bebe_feliz2 = pg.image.load("img/bb_feliz/bb_feliz_2.png")
bebe_feliz3 = pg.image.load("img/bb_feliz/bb_feliz_3.png")
bebe_feliz4 = pg.image.load("img/bb_feliz/bb_feliz_4.png")
bebe_feliz5 = pg.image.load("img/bb_feliz/bb_feliz_5.png")
bebe_feliz6 = pg.image.load("img/bb_feliz/bb_feliz_6.png")
bebe_feliz7 = pg.image.load("img/bb_feliz/bb_feliz_7.png")
bebe_feliz8 = pg.image.load("img/bb_feliz/bb_feliz_8.png")

#Bebê indiferente
bebe_indiferente1 = pg.image.load("img/bb_indiferente/bebe_indiferente1.png")
bebe_indiferente2 = pg.image.load("img/bb_indiferente/bebe_indiferente2.png")
bebe_indiferente3 = pg.image.load("img/bb_indiferente/bebe_indiferente3.png")
bebe_indiferente4 = pg.image.load("img/bb_indiferente/bebe_indiferente4.png")
bebe_indiferente5 = pg.image.load("img/bb_indiferente/bebe_indiferente5.png")
bebe_indiferente6 = pg.image.load("img/bb_indiferente/bebe_indiferente6.png")
bebe_indiferente7 = pg.image.load("img/bb_indiferente/bebe_indiferente7.png")
bebe_indiferente8 = pg.image.load("img/bb_indiferente/bebe_indiferente8.png")

#Bebê triste
bebe_triste1 = pg.image.load("img/bb_triste/bb_triste1.png")
bebe_triste2 = pg.image.load("img/bb_triste/bb_triste2.png")
bebe_triste3 = pg.image.load("img/bb_triste/bb_triste3.png")
bebe_triste4 = pg.image.load("img/bb_triste/bb_triste4.png")
bebe_triste5 = pg.image.load("img/bb_triste/bb_triste5.png")
bebe_triste6 = pg.image.load("img/bb_triste/bb_triste6.png")
bebe_triste7 = pg.image.load("img/bb_triste/bb_triste7.png")
bebe_triste8 = pg.image.load("img/bb_triste/bb_triste8.png")

#Bebê normal
bebe_normal1 = pg.image.load("img/bb_normal/bebe_normal1.png")
bebe_normal2 = pg.image.load("img/bb_normal/bebe_normal2.png")
bebe_normal3 = pg.image.load("img/bb_normal/bebe_normal3.png")
bebe_normal4 = pg.image.load("img/bb_normal/bebe_normal4.png")
bebe_normal5 = pg.image.load("img/bb_normal/bebe_normal5.png")
bebe_normal6 = pg.image.load("img/bb_normal/bebe_normal6.png")
bebe_normal7 = pg.image.load("img/bb_normal/bebe_normal7.png")
bebe_normal8 = pg.image.load("img/bb_normal/bebe_normal8.png")
bebe_normal9 = pg.image.load("img/bb_normal/bebe_normal9.png")
bebe_normal10 = pg.image.load("img/bb_normal/bebe_normal10.png")
bebe_normal11 = pg.image.load("img/bb_normal/bebe_normal11.png")
bebe_normal12 = pg.image.load("img/bb_normal/bebe_normal12.png")

#Imagens de fundo
background_jogar = pg.image.load("img/telas_fundo/fundo_fase.jpg")
background_auxiliar = pg.image.load("img/telas_fundo/auxiliar_fundo.png")
background_comojogar = pg.image.load("img/telas_fundo/menu_selecionado_comojogar.jpg")
background_image = pg.image.load("img/telas_fundo/menu.jpg")
background_feliz = pg.image.load("img/fim_feliz/fim_feliz.jpg")
background_triste= pg.image.load("img/fim_triste/fim_triste.jpg")

#Como jogar
mouse = pg.image.load("img/como_jogar/mouse.png")
mouse_clique = pg.image.load("img/como_jogar/mouse_clique.png")
tela_comojogar = pg.image.load("img/como_jogar/tela_como_jogar.png")
tela_comojogar_100 = pg.image.load("img/como_jogar/tela_como_jogar_100.png")
tela_comojogar_50 = pg.image.load("img/como_jogar/tela_como_jogar_50_pontos.png")
tela_comojogar_erro = pg.image.load("img/como_jogar/tela_como_jogar_erro.png")

#Cria a lista de posições do eixo x dos alimentos
alimentos = [100, 316, 532, 749]

def musica_menu():
        pg.mixer.music.load('musicas/musica_menu.mp3') #Carregando a música
        pg.mixer.music.play (- 1 )# o - 1 é para a musica não parar de tocar
        pg.mixer.music.set_volume(0.5)

def musica_como_jogar():
        pg.mixer.music.load('musicas/Pop_Goes_The_Weasel.mp3') #Carregando a música
        pg.mixer.music.play (- 1 )# o - 1 é para a musica não parar de tocar
        pg.mixer.music.set_volume(0.5)

def musica_fase1():
        pg.mixer.music.load('musicas/Cuckoo_Clock.mp3') #Carregando a música
        pg.mixer.music.play (- 1 )# o - 1 é para a musica não parar de tocar
        pg.mixer.music.set_volume(0.5)
        
'''def musica_tela_final_triste():
        pg.mixer.music.load('musicas/Toy_Piano.mp3') #Carregando a música
        pg.mixer.music.play (- 1 )# o - 1 é para a musica não parar de tocar'''
        

def como_jogar(screen):
    obj = 0
    posx = 1000
    posy = 700
    pg.mixer.music.stop()
    musica_como_jogar()
    x = 0
    y = 0
    while True:
        pg.time.delay(15)
        screen.blit(tela_comojogar, [0, 0])  
        posi_mouse = pg.mouse.get_pos()
        screen.blit(mouse, [posx, posy])
        pg.display.flip()
        if(obj == 0):
                posx-=3
                posy-=0.7
                if(posy <= 570):
                        efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                        efeito_mouse.play()
                        screen.blit(tela_comojogar_100, [0, 0])
                        screen.blit(mouse_clique, [442, 570])
                        pg.display.flip()
                        pg.time.delay(3000)
                        posx = 1000
                        posy = 700
                        obj = 1
                        
        elif(obj == 1):
                posx-=3
                posy-=1.1
                if(posy <=570):
                        efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                        efeito_mouse.play()
                        screen.blit(tela_comojogar_50, [0, 0])
                        screen.blit(mouse_clique, [655, 585])
                        pg.display.flip()
                        pg.time.delay(3000)
                        posx = 1000
                        posy = 700
                        obj = 2
        elif(obj == 2):
                posx-=3
                posy-=2.3
                if(posy <=570):
                        efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                        efeito_mouse.play()
                        screen.blit(tela_comojogar_erro, [0, 0])
                        screen.blit(mouse_clique, [840, 580])
                        pg.display.flip()
                        pg.time.delay(3000)
                        posx = 1000
                        posy = 700
                        obj = 0

                        
        for event in pg.event.get():
           if event.type == pg.MOUSEBUTTONDOWN:
               x= posi_mouse[0]
               y= posi_mouse[1]
               if(x > 5 and x < 75 and y > 5 and y < 75):
                   pg.mixer.music.stop()
                   menu() 
        pg.display.flip()
    pg.display.flip()

def tela_creditos():
    pg.init()
    #Trocar formato do cursor
    pg.mouse.set_cursor(*pg.cursors.arrow)
    os.environ['SDL_VIDEO_CENTERED'] = '1' # Centralizando tela 
    screen = pg.display.set_mode((1024,768))
    pg.display.set_caption("Papa do Bebê")
    screen.fill((255,255,255))
    pg.display.flip()
    pg.mixer.music.stop()
    pg.mixer.music.stop()
    pg.mixer.music.load('musicas/Ukulele_Beach.mp3') #Carregando a música
    pg.mixer.music.play (- 1 )# o - 1 é para a musica não parar de tocar
    while True:
        for event in pg.event.get():
           posi_mouse = pg.mouse.get_pos()
           x= posi_mouse[0]
           y= posi_mouse[1]
           background_image = pg.image.load("img/telas_fundo/tela_creditos.png")
           
           #Eventos de cliques
           if event.type == pg.MOUSEBUTTONDOWN:
                if (x >= 13 and x < 77   and y >= 6 and y <= 68): #se clicar em iniciar  
                    efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                    efeito_mouse.play()
                    pg.mixer.music.stop()
                    menu()                   
                        
        screen.blit(background_image, [0, 0])                        
        pg.display.flip()
    pg.display.flip()
  
        

def tela_inicio():
    global inicio
    inicio = time.time()
    #Trocar formato do cursor
    pg.display.list_modes()   
    os.environ['SDL_VIDEO_CENTERED'] = '1' # Centralizando tela
    pg.init()
    screen = pg.display.set_mode((1024,768))
    pg.display.set_caption("Papa do Bebê")
    screen.fill((255,255,255))
    screen.blit(background_jogar, [0, 0])
    pg.display.flip()
    selecionador_de_fase(screen)
    
def selecionador_de_fase(screen):
    #Trocar formato do cursor
    pg.display.list_modes()
    pg.display.set_caption("Papa do Bebê")
    
    global cont
    while True:
        screen.blit(background_auxiliar, [0, 0])
        pg.display.flip()
        #Chama a função jogo 
        if(cont == 0):
                cont+=1
                insere_vidas(screen)
        elif(cont == 1):
                cont+=1
                insere_vidas(screen)
        elif(cont == 2):
                cont+=1
                insere_vidas(screen)
        elif(cont == 3):
                cont+=1
                insere_vidas(screen)
        elif(cont == 4):
                cont+=1
                insere_vidas(screen)
        elif(cont == 5):
                cont+=1
                insere_vidas(screen)
        elif(cont == 6):
                cont+=1
                insere_vidas(screen)
        elif(cont == 7):
                cont+=1
                insere_vidas(screen)
        elif(cont == 8):
                cont+=1
                insere_vidas(screen)
        elif(cont == 9):
                cont+=1
                insere_vidas(screen)
        else:
                calculo(screen, 0)                
    pg.display.flip()

def calculo(screen, ganhou):
        global duracao
        global score
        global vidas
        global cont
        global inicio
        global fim        
        minutos = 0
        segundos = duracao
        segundos = int(round(segundos))
        if(segundos > 59):
             minutos = segundos//60
             segundos = segundos%60
        if(segundos < 10):
             segundos = "0" + str(segundos)
        if(minutos < 10):
             minutos = "0" + str(minutos)

        result = str(minutos) + ":" + str(segundos)
        pontos = score
        cont = 0
        vidas = 3
        score = 0
        inicio = 0
        duracao = 0
        fim = 0
        if(ganhou == 0):
                Tk().wm_withdraw()
                messagebox.showinfo('٩(^‿^)۶','Duração do jogo: ' + str(result) + '\n Pontuação final: ' + str(pontos) + ' pontos')
                fim_jogo_feliz(screen)
        elif(ganhou == 1):
                Tk().wm_withdraw()
                messagebox.showinfo('.·´¯`(>▂<)´¯`·.','Duração do jogo: ' + str(result) + '\n Pontuação final: ' + str(pontos) + ' pontos')
                fim_jogo_triste(screen)
        elif(ganhou == 2):
                Tk().wm_withdraw()
                messagebox.showinfo('.·´¯`(>▂<)´¯`·.','Já está indo?\n Pontuação final: ' + str(pontos) + ' pontos')
                menu()
        
def insere_vidas(screen):
     #Insere as colheres na tela
     x = 895
     y = 80
     if(vidas>0):
            for i in range(vidas, 0, -1):
                     screen.blit(colher, [x, y])
                     x-=40
                     pg.display.flip()
     pontuador(screen)

def remove_colher(screen):
        if(vidas == 2):
                screen.blit(risca_colher, [815, 80])
        elif(vidas == 1):
                screen.blit(risca_colher, [855, 80])
        elif(vidas == 0):
                screen.blit(risca_colher, [895, 80])
                pg.display.flip()
                pg.time.delay(1000)
                calculo(screen, 1)
        pg.display.flip()
        pg.time.delay(1000)
        selecionador_de_fase(screen)
     
def pontuador(screen):
     #Insere layout do cronômetro, texto indicador da fase e layout do score
     screen.blit(fundoDisplay, [795, -5])
     text = fonteText.render("PONTOS: " + str(score), True, (255,255,255))
     screen.blit(text, [820, 60])
     cronometro(screen)

def cronometro(screen):
     global seconds
     #Insere layout do cronômetro, texto indicador da fase e layout do score
     text = fonteText.render("FASE " + str(cont), True, (255,255,255))
     screen.blit(text, [850, 20])
     if(cont == 1):
             seconds = 30
     elif(cont == 2):
             seconds = 25
     elif(cont == 3):
             seconds = 20
     elif(cont == 4):
             seconds = 15
     elif(cont == 5):
             seconds = 10
     elif(cont == 6):
             seconds = 8
     elif(cont == 7):
             seconds = 6
     elif(cont == 8):
             seconds = 5
     elif(cont == 9):
             seconds = 4
     elif(cont == 10):
             seconds = 3             
     jogo(screen, seconds, (seconds+1))

def feliz(screen):
        screen.blit(bebe_feliz1, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_feliz2, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_feliz3, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_feliz4, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_feliz5, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_feliz6, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_feliz7, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_feliz8, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        selecionador_de_fase(screen)

def indiferente(screen):
        screen.blit(bebe_indiferente1, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_indiferente2, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_indiferente3, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_indiferente4, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_indiferente5, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_indiferente6, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_indiferente7, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_indiferente8, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        selecionador_de_fase(screen)

def triste(screen):
        efeito_mouse = pg.mixer.Sound('efeitos_sonoros/erro.wav')
        efeito_mouse.play()
        screen.blit(bebe_triste1, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_triste2, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_triste3, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_triste4, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_triste5, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_triste6, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_triste7, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        screen.blit(bebe_triste8, [0, 0])
        pg.display.flip()
        pg.time.delay(seg)
        remove_colher(screen)

def fim_jogo_feliz(screen):
        global background_feliz
        pg.init()
        #Trocar formato do cursor
        pg.mouse.set_cursor(*pg.cursors.arrow)
        os.environ['SDL_VIDEO_CENTERED'] = '1' # Centralizando tela 
        screen = pg.display.set_mode((1024,768))
        pg.display.set_caption("Papa do Bebê")
        screen.fill((255,255,255))
        pg.display.flip()
        pg.mixer.music.stop()
        pg.mixer.music.load('musicas/The_Alphabet_Song.mp3') #Carregando a música
        pg.mixer.music.play (- 1 )# o - 1 é para a musica não parar de tocar
        x = 0
        y = 0
        while True:     
                for event in pg.event.get():
                   posi_mouse = pg.mouse.get_pos()  
                   if event.type == pg.MOUSEMOTION:
                       x= posi_mouse[0]
                       y= posi_mouse[1]
                       if (x >= 171 and x <= 398 and y >= 494 and y <= 552): 
                           background_feliz = pg.image.load("img/fim_feliz/fim_feliz_recomecar.jpg")
                           pg.display.flip()
                       elif (x >= 419 and x <= 645 and y >= 494 and y <= 552): 
                           background_feliz = pg.image.load("img/fim_feliz/fim_feliz_menu.jpg")
                           pg.display.flip()
                       elif (x >= 659 and x <= 887 and y >= 494 and y <= 552):
                           background_feliz = pg.image.load("img/fim_feliz/fim_feliz_sair.jpg")
                           pg.display.flip()
                       else:
                           background_feliz = pg.image.load("img/fim_feliz/fim_feliz.jpg")
                           pg.display.flip()
                   if event.type == pg.MOUSEBUTTONDOWN:
                       if (x >= 171 and x <= 398 and y >= 494 and y <= 552):
                           pg.mixer.music.stop()
                           musica_fase1()
                           tela_inicio()
                       elif (x >= 419 and x <= 645 and y >= 494 and y <= 552):
                           menu()
                       elif (x >= 659 and x <= 887 and y >= 494 and y <= 552): 
                           pg.quit()
                           
                screen.blit(background_feliz, [0, 0])                        
                pg.display.flip()
        pg.display.flip()

def fim_jogo_triste(screen):
        global background_triste
        pg.init()
        #Trocar formato do cursor
        pg.mouse.set_cursor(*pg.cursors.arrow)
        os.environ['SDL_VIDEO_CENTERED'] = '1' # Centralizando tela 
        screen = pg.display.set_mode((1024,768))
        pg.display.set_caption("Papa do Bebê")
        screen.fill((255,255,255))
        pg.display.flip()
        pg.mixer.music.stop()
        pg.mixer.music.load('musicas/Toy_Piano.mp3') #Carregando a música
        pg.mixer.music.play (- 1 )# o - 1 é para a musica não parar de tocar
        x = 0
        y = 0
        while True:
                for event in pg.event.get():
                   posi_mouse = pg.mouse.get_pos()  
                   if event.type == pg.MOUSEMOTION:
                       x= posi_mouse[0]
                       y= posi_mouse[1]
                       if (x >= 171 and x <= 398 and y >= 494 and y <= 552): 
                           background_triste = pg.image.load("img/fim_triste/fim_triste_recomecar.jpg")
                           pg.display.flip()
                       elif (x >= 419 and x <= 645 and y >= 494 and y <= 552): 
                           background_triste = pg.image.load("img/fim_triste/fim_triste_menu.jpg")
                           pg.display.flip()
                       elif (x >= 659 and x <= 887 and y >= 494 and y <= 552):
                           background_triste = pg.image.load("img/fim_triste/fim_triste_sair.jpg")
                           pg.display.flip()
                       else:
                           background_triste = pg.image.load("img/fim_triste/fim_triste.jpg")
                           pg.display.flip()
                   if event.type == pg.MOUSEBUTTONDOWN:
                       if (x >= 171 and x <= 398 and y >= 494 and y <= 552):
                           pg.mixer.music.stop()
                           musica_fase1()
                           tela_inicio()
                       elif (x >= 419 and x <= 645 and y >= 494 and y <= 552):
                           menu()
                       elif (x >= 659 and x <= 887 and y >= 494 and y <= 552): 
                           pg.quit()
                           
                screen.blit(background_triste, [0, 0])                        
                pg.display.flip()
        pg.display.flip()

def jogo(screen, seconds, tempo):
     global score
     global vidas
     global cont
     global fim
     global duracao
     global inicio
     global flag
     x = 0
     y = 0
     #Carrega todas as comidas
     nao_comestiveis = [chave, globo, lampada, lente, livro, pote_racao, quimica, rato, relogio, trofeu, veneno]
     nao_saudaveis = [batata_frita, bolo, brigadeiro, chocolate, cupcake, gummie, hotdog, pirulito, pizza, refrigerante, rosquinhas, salgadinho, sorvete]
     saudaveis = [abacate, banana, beringela, brocolis, cenoura, churrasco, coco, kiwi, laranja, leite, limao, maca, maca2, melancia, milho, morango, ovo, pedaco_melancia, pera, queijo, salada]

     #Embaralha os alimentos dos vetores
     random.shuffle(alimentos)
     random.shuffle(saudaveis)
     random.shuffle(nao_saudaveis)
     random.shuffle(nao_comestiveis)
     screen.blit(bebe_normal1, [0, 0])
     #Ordena os alimentos
     if(alimentos[0] == 100 or alimentos[0] == 749):
          obj0 = 500
     else:
          obj0 = 515
     if(alimentos[1] == 100 or alimentos[1] == 749):
          obj1 = 500
     else:
          obj1 = 515
     if(alimentos[2] == 100 or alimentos[2] == 749):
          obj2 = 500
     else:
          obj2 = 515
     if(alimentos[3] == 100 or alimentos[3] == 749):
         obj3 = 500
     else:
         obj3 = 515
     
     if(cont <= 2):
             screen.blit(saudaveis[0], [alimentos[0], obj0])    
             screen.blit(saudaveis[1], [alimentos[1], obj1])
             screen.blit(saudaveis[2], [alimentos[2], obj2])
             screen.blit(nao_saudaveis[0], [alimentos[3], obj3])
     elif(cont <= 4):
             screen.blit(saudaveis[0], [alimentos[0], obj0])    
             screen.blit(saudaveis[1], [alimentos[1], obj1])
             screen.blit(nao_saudaveis[0], [alimentos[2], obj2])
             screen.blit(nao_saudaveis[1], [alimentos[3], obj3])
     elif(cont <= 6):
             screen.blit(saudaveis[0], [alimentos[0], obj0])    
             screen.blit(nao_saudaveis[1], [alimentos[1], obj1])
             screen.blit(nao_comestiveis[0], [alimentos[2], obj2])
             screen.blit(nao_comestiveis[1], [alimentos[3], obj3])
     elif(cont > 6):
             screen.blit(saudaveis[0], [alimentos[0], obj0])    
             screen.blit(nao_comestiveis[0], [alimentos[1], obj1])
             screen.blit(nao_comestiveis[1], [alimentos[2], obj2])
             screen.blit(nao_comestiveis[2], [alimentos[3], obj3])
     pg.display.flip()
     while True:  
             pg.time.delay(seg2)
             screen.blit(fundoDisplay, [795, -5])
             display = "TEMPO: {}".format(seconds)
             text = fonteText.render(display, True, (255,255,255))
             screen.blit(text, [830, 20])
             text = fonteText.render("PONTOS: " + str(score), True, (255,255,255))
             screen.blit(text, [820, 60])
             tempo = tempo-(seg2/1000)
             flag+=1
             if(flag == (1000/seg2)):
                seconds = seconds-1
                flag = 0
             if(seconds == -1):
                     Tk().wm_withdraw()
                     messagebox.showinfo('(⊙﹏⊙)','Tempo esgotado.')
                     vidas-=1
                     remove_colher(screen)
                
            
             pg.display.flip()
             for event in pg.event.get():
                   posi_mouse = pg.mouse.get_pos()
                   global inicio
                   global fim
                   global duracao
                   fim = time.time()
                   duracao = fim - inicio
                   global estado_bebe
                   if(estado_bebe == 0):
                           screen.blit(bebe_normal1, [0, 0])
                           pg.time.delay(50)
                   elif(estado_bebe == 1):
                           screen.blit(bebe_normal2, [0, 0])
                           pg.time.delay(50)
                   elif(estado_bebe == 2):
                           screen.blit(bebe_normal3, [0, 0])
                   elif(estado_bebe == 3):
                           screen.blit(bebe_normal4, [0, 0])
                   elif(estado_bebe == 4):
                           screen.blit(bebe_normal5, [0, 0])
                   elif(estado_bebe == 5):
                           screen.blit(bebe_normal7, [0, 0])
                   elif(estado_bebe == 6):
                           screen.blit(bebe_normal9, [0, 0])
                   elif(estado_bebe == 7):
                           screen.blit(bebe_normal10, [0, 0])
                   elif(estado_bebe == 8):
                           screen.blit(bebe_normal12, [0, 0])
                           estado_bebe = -1
                   estado_bebe += 1
                   if event.type == pg.MOUSEBUTTONDOWN:
                       x= posi_mouse[0]
                       y= posi_mouse[1]
                       if(x > 5 and x < 75 and y > 5 and y < 75):
                               calculo(screen, 2)
                       #Caso clique em algum ítem retorna um popup e inicia a fase 2
                       if(cont <= 2):
                               if(x > alimentos[0] and x < (alimentos[0]+175) and y > obj0 and y < (obj0+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('٩(^‿^)۶','Parabéns\n+100 pontos!')
                                    score+=100
                                    feliz(screen)
                               elif(x > alimentos[1] and x < (alimentos[1]+175) and y > obj1 and y < (obj1+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('٩(^‿^)۶','Parabéns\n+100 pontos!')
                                    score+=100
                                    feliz(screen)
                               elif(x > alimentos[2] and x < (alimentos[2]+175) and y > obj2 and y < (obj2+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('٩(^‿^)۶','Parabéns\n+100 pontos!')
                                    score+=100
                                    feliz(screen)
                               elif(x > alimentos[3] and x < (alimentos[3]+175) and y > obj3 and y < (obj3+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('｡◕‿◕｡','Ótimo\n+50 pontos!')
                                    score+=50
                                    indiferente(screen)

                       elif(cont <= 4):
                               if(x > alimentos[0] and x < (alimentos[0]+175) and y > obj0 and y < (obj0+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('٩(^‿^)۶','Parabéns\n+100 pontos!')
                                    score+=100
                                    feliz(screen)
                               elif(x > alimentos[1] and x < (alimentos[1]+175) and y > obj1 and y < (obj1+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('٩(^‿^)۶','Parabéns\n+100 pontos!')
                                    score+=100
                                    feliz(screen)
                               elif(x > alimentos[2] and x < (alimentos[2]+175) and y > obj2 and y < (obj2+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('｡◕‿◕｡','Ótimo\n+50 pontos!')
                                    score+=50
                                    indiferente(screen)
                               elif(x > alimentos[3] and x < (alimentos[3]+175) and y > obj3 and y < (obj3+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('｡◕‿◕｡','Ótimo\n+50 pontos!')
                                    score+=50
                                    indiferente(screen)
                       elif(cont <= 6):
                               if(x > alimentos[0] and x < (alimentos[0]+175) and y > obj0 and y < (obj0+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('٩(^‿^)۶','Parabéns\n+100 pontos!')
                                    score+=100
                                    feliz(screen)
                               elif(x > alimentos[1] and x < (alimentos[1]+175) and y > obj1 and y < (obj1+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('｡◕‿◕｡','Ótimo\n+50 pontos!')
                                    score+=50
                                    indiferente(screen)
                               elif(x > alimentos[2] and x < (alimentos[2]+175) and y > obj2 and y < (obj2+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('.·´¯`(>▂<)´¯`·.','Você errou.')
                                    vidas-=1
                                    triste(screen)
                               elif(x > alimentos[3] and x < (alimentos[3]+175) and y > obj3 and y < (obj3+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('.·´¯`(>▂<)´¯`·.','Você errou.')
                                    vidas-=1
                                    triste(screen)
                       elif(cont <= 10):
                               if(x > alimentos[0] and x < (alimentos[0]+175) and y > obj0 and y < (obj0+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('٩(^‿^)۶','Parabéns\n+100 pontos!')
                                    score+=100
                                    feliz(screen)
                               elif(x > alimentos[1] and x < (alimentos[1]+175) and y > obj1 and y < (obj1+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('.·´¯`(>▂<)´¯`·.','Você errou.')
                                    vidas-=1
                                    triste(screen)
                               elif(x > alimentos[2] and x < (alimentos[2]+175) and y > obj2 and y < (obj2+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('.·´¯`(>▂<)´¯`·.','Você errou.')
                                    vidas-=1
                                    triste(screen)
                               elif(x > alimentos[3] and x < (alimentos[3]+175) and y > obj3 and y < (obj3+165)):
                                    Tk().wm_withdraw()
                                    messagebox.showinfo('.·´¯`(>▂<)´¯`·.','Você errou.')
                                    vidas-=1
                                    triste(screen)

def menu():
    global background_image
    pg.init()
    #Trocar formato do cursor
    pg.mouse.set_cursor(*pg.cursors.arrow)
    os.environ['SDL_VIDEO_CENTERED'] = '1' # Centralizando tela 
    screen = pg.display.set_mode((1024,768))
    pg.display.set_caption("Papa do Bebê")
    screen.fill((255,255,255))
    pg.display.flip()
    pg.mixer.music.stop()
    musica_menu()
    x = 0
    y = 0
    while True:
       
        for event in pg.event.get():
           posi_mouse = pg.mouse.get_pos()  
           if event.type == pg.MOUSEMOTION:
               x= posi_mouse[0]
               y= posi_mouse[1]
               if (x >= 353 and x <= 668 and y >= 440 and y <= 515): #trocar a cor do iniciar
                   background_image = pg.image.load("img/telas_fundo/menu_selecionado_iniciar.jpg")
                   pg.display.flip()
               elif (x >= 353 and x <= 668 and y >= 540 and y <= 617): #trocar a cor do como jogar
                   background_image = pg.image.load("img/telas_fundo/menu_selecionado_comojogar.jpg")
                   pg.display.flip()
               elif (x >= 353 and x <= 668 and y >= 644 and y <= 722): #trocar a cor do creditos
                   background_image = pg.image.load("img/telas_fundo/menu_selecionado_creditos.jpg")
                   pg.display.flip()
               elif (x >= 86 and x <= 136 and y >= 705 and y <= 752): #trocar a cor stop
                   background_image = pg.image.load("img/telas_fundo/menu_selecionado_stop.jpg")
                   pg.display.flip()
               elif (x >= 148 and x <= 199 and y >= 704 and y <= 754): # trocar a cor play
                   background_image = pg.image.load("img/telas_fundo/menu_selecionado_play.jpg")
                   pg.display.flip()
               elif (x >= 949 and x <= 1002 and y >= 12 and y <= 62): #trocar cor botão fechar
                   background_image = pg.image.load("img/telas_fundo/menu_selecionado_fechar.jpg")
                   pg.display.flip()
                   
               #Quando tirar o mouse de cima da do botão ele volta pro backgorund principal
               else:
                   background_image = pg.image.load("img/telas_fundo/menu.jpg")
                   pg.display.flip()

                #Eventos de cliques
           if event.type == pg.MOUSEBUTTONDOWN:
                if (x >= 353 and x < 668   and y >= 440 and y <= 515): #se clicar em iniciar  
                    efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                    efeito_mouse.play()
                    menu == False
                    pg.mixer.music.stop() #pra parar a música do menu
                    musica_fase1() #começar a tocar a musica da fase 1
                    tela_inicio()
                elif (x >= 353 and x < 668 and y >= 540 and y <= 617): #se clicar em como jogar
                    efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                    efeito_mouse.play()
                    como_jogar(screen)
                elif (x >= 353 and x < 668 and y >= 644 and y <= 722): #se clicar em creditos
                    efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                    efeito_mouse.play()
                    tela_creditos()
                elif (x >= 86 and x <= 136 and y >= 705 and y <= 752): #se clicar em stop
                   efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                   efeito_mouse.play()
                   pg.mixer.music.stop()
                elif (x >= 148 and x <= 199 and y >= 704 and y <= 754): #se clicar em play
                   efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                   efeito_mouse.play()
                   musica_menu()
                elif (x >= 949 and x <= 1002 and y >= 12 and y <= 62): #se clicar em fechar
                   efeito_mouse = pg.mixer.Sound('efeitos_sonoros/clique_mouse.wav')
                   efeito_mouse.play()
                   pg.quit()
                   
        screen.blit(background_image, [0, 0])                        
        pg.display.flip()
    pg.display.flip()

menu()


