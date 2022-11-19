#instalação: SpeechRecognition e PyAudio e pyttsx3

import speech_recognition as sr
import os
import pyttsx3

#faz um loping para o usuario falar algo e reconhecer ate que ele diga "sair" a cada resposta do robo ele pergunta se deseja mais algo

def Conervete_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
rec = sr.Recognizer()

mic = sr.Microphone()

while True:

       
        with mic as source:
    
            rec.adjust_for_ambient_noise(source)
    
            print("Diga algo: ")
            Conervete_voz("Diga algo")
    
            audio = rec.listen(source)
    
            print("Processando...")
    
            try:
                
                text = rec.recognize_google(audio, language='pt-BR')
    
                print("Você disse: {}".format(text))
    
                if text == "sair":
    
                    print("Até mais!")
                    Conervete_voz("Até mais")
                    break
                #se o usuario perguntar o nome do robo ele responde com um audio
                elif text == "qual o seu nome":
    
                    print("Meu nome é Walileo é meu criador é o Igor Gabriel")
                    Conervete_voz("Meu nome é Walileo é meu criador é o Igor Gabriel")
                #se o usuario perguntar a idade do robo ele responde com um audio
                elif text == "qual a sua idade":
    
                    print("Eu acabei de nascer, mas meu criador me disse que eu tenho 1 semana")
                    Conervete_voz("Eu tenho 1 semana, mais meu criador me disse que eu tenho 1 semana")
                #se o usuario perguntar a data ele verifica a data do sistema e responde com um audio
                elif text == "qual a data de hoje":
                        date = os.popen('date').read()
                        print(date)
                        Conervete_voz(date)
                #se o usuario perguntar a hora ele verifica a hora do sistema e responde com um audio
                elif text == "qual a hora":
                        time = os.popen('time').read()
                        print(time)
                        Conervete_voz(time)
                #abre o site da ufca
                elif text == "abrir ufca":
                        os.system("firefox https://www.ufca.edu.br/")
                #abre o site do google
                elif text == "abrir google":
                        os.system("firefox https://www.google.com/")
                #abre o instagram do seu criador
                elif text == "abrir instagram do seu criador":
                        os.system("https://www.instagram.com/ig_gab1el/")
                #abre o site do youtube
                elif text == "abrir youtube":
                        os.system("firefox https://www.youtube.com/")
                #gerar um número aleatorio
                elif text == "gerar um número aleatorio":
                        import random
                        numero = random.randint(0, 100)
                        print(numero)
                        Conervete_voz(numero)
                #realiza operações matematica falando a operção e os numeros
                elif text == "somar":
                        print("Qual o primeiro numero")
                        Conervete_voz("Qual o primeiro numero")
                        audio = rec.listen(source)
                        text = rec.recognize_google(audio, language='pt-BR')
                        numero1 = int(text)
                        print("Qual o segundo numero")
                        Conervete_voz("Qual o segundo numero")
                        audio = rec.listen(source)
                        text = rec.recognize_google(audio, language='pt-BR')
                        numero2 = int(text)
                        soma = numero1 + numero2
                        print(soma)
                        Conervete_voz(soma)
                elif text == "subtrair":
                        print("Qual o primeiro numero")
                        Conervete_voz("Qual o primeiro numero")
                        audio = rec.listen(source)
                        text = rec.recognize_google(audio, language='pt-BR')
                        numero1 = int(text)
                        print("Qual o segundo numero")
                        Conervete_voz("Qual o segundo numero")
                        audio = rec.listen(source)
                        text = rec.recognize_google(audio, language='pt-BR')
                        numero2 = int(text)
                        subtracao = numero1 - numero2
                        print(subtracao)
                        Conervete_voz(subtracao)
                elif text == "multiplicar":
                        print("Qual o primeiro numero")
                        Conervete_voz("Qual o primeiro numero")
                        audio = rec.listen(source)
                        text = rec.recognize_google(audio, language='pt-BR')
                        numero1 = int(text)
                        print("Qual o segundo numero")
                        Conervete_voz("Qual o segundo numero")
                        audio = rec.listen(source)
                        text = rec.recognize_google(audio, language='pt-BR')
                        numero2 = int(text)
                        multiplicacao = numero1 * numero2
                        print(multiplicacao)
                        Conervete_voz(multiplicacao)
                #pede para desenhar um coração na tela
                elif text == "desenhar um coração":
                    from turtle import *
                    color ("red")
                    begin_fill()
                    pensize(3)
                    left(50)
                    forward(133)
                    circle(50,200)
                    right(140)
                    circle(50,200)
                    forward(133)
                    end_fill()
                elif text == "desenhar um quadrado":
                    from turtle import *
                    color ("red")
                    begin_fill()
                    pensize(3)
                    forward(100)
                    left(90)
                    forward(100)
                    left(90)
                    forward(100)
                    left(90)
                    forward(100)
                    end_fill()
                #pede para abrir o sigaa da ufca
                elif text == "abrir sigaa":
                    os.system("firefox https://sigaa.ufca.edu.br/sigaa/public/home.jsf")
                
                #voce está bem
                elif text == "voce está bem":
                    print("Estou bem, e você?")
                    Conervete_voz("Estou bem, e você?")
                
                #voce esta me ouvindo interogação
                elif text == "voce esta me ouvindo":
                    print("Sim, estou te ouvindo")
                    Conervete_voz("Sim, estou te ouvindo")

                #porque voce não faz mais coisas
                elif text == "porque voce não faz mais coisas":
                    print("Porque eu ainda estou sendo desenvolvido")
                    Conervete_voz("Porque eu ainda estou sendo desenvolvido pelo meu criador")
                    print("Mas ele me disse que em breve eu vou fazer mais coisas")
                    Conervete_voz("Mas ele me disse que em breve eu vou fazer mais coisas")
                    print ("Cobre ele para que ele me desenvolva mais rápido estou com muita vontade de fazer mais coisas o nome dele é Igor Gabriel o link do instagram dele é ")
                    Conervete_voz("Cobre ele para que ele me desenvolva mais rápido estou com muita vontade de fazer mais coisas o nome dele é Igor Gabriel o link do instagram dele é ")
                    print("======================================")
                    print("https://www.instagram.com/ig_gab1el/")
               
                #voce esta me vendo interogação
                elif text == "voce esta me vendo":
                    print("Sim, estou te vendo")
                    Conervete_voz("Sim, estou te vendo")
                

               
                #se o usuario perguntar o que ele pode fazer ele responde com um audio
                elif text == "o que você pode fazer":
                    print("Eu posso abrir o google")
                    Conervete_voz("Eu posso abrir o google")
                    print("Eu posso abrir o youtube")
                    Conervete_voz("Eu posso abrir o youtube")
                    print("Eu posso abrir o instagram do meu criador")
                    Conervete_voz("Eu posso abrir o instagram do meu criador")
                    print("Eu posso abrir o site da ufca")
                    Conervete_voz("Eu posso abrir o site da ufca")
                    print("Eu posso abrir o sigaa da ufca")
                    Conervete_voz("Eu posso abrir o sigaa da ufca")
                    print("Eu posso gerar um número aleatorio")
                    Conervete_voz("Eu posso gerar um número aleatorio")
                    print("Eu posso somar")
                    Conervete_voz("Eu posso somar")
                    print("Eu posso subtrair")
                    Conervete_voz("Eu posso subtrair")
                    print("Eu posso multiplicar")
                    Conervete_voz("Eu posso multiplicar")
                    print("Eu posso desenhar um coração")
                    Conervete_voz("Eu posso desenhar um coração")
                    print("Eu posso desenhar um quadrado")
                    Conervete_voz("Eu posso desenhar um quadrado")
                    print("Eu posso dizer a hora")
                    Conervete_voz("Eu posso dizer a hora")
                    print("Eu posso dizer a data")
                    Conervete_voz("Eu posso dizer a data")

            except  sr.UnknownValueError:
              print("Não entendi")
              Conervete_voz("Não entendi")
                   
                    







 
                    







 
