#instalação: SpeechRecognition e PyAudio


import speech_recognition as sr

rec = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    rec.adjust_for_ambient_noise(source)
    print("Diga algo")
    audio = rec.listen(source)
    print("Reconhecendo...")
    try:
        text = rec.recognize_google(audio, language="pt-BR")
        print("Você disse: {}".format(text))
    except:
        print("Não entendi")

#Se o úsuario falar que horas são, o programa vai responder com a hora atual
if text == "que horas são":
    import datetime
    now = datetime.datetime.now()
    print("São {} horas e {} minutos".format(now.hour, now.minute))

#Se o úsuario falar que dia é hoje, o programa vai responder com o dia atual
if text == "que dia é hoje":
    import datetime
    now = datetime.datetime.now()
    print("Hoje é dia {}".format(now.day))

#Se o úsuario pedir uma senha forte o programa vai gerar uma senha forte
if text == "gera uma senha forte":
    import random
    import string
    chars = string.ascii_letters + string.digits + '!@#$%&*()'
    size = random.randint(8, 16)
    password = ''.join(random.choice(chars) for x in range(size))
    print("Sua senha é: {}".format(password))

#se o úsuario pedir para Contar até 10 o programa vai contar até 10
if text == "conta até 10":
    for i in range(1, 11):
        print(i)

#Se o úsuario pedir um número aleatório o programa vai gerar um número aleatório
if text == "gera um número aleatório":
    import random
    print(random.randint(0, 100))

#Se o úsuario pedir para abrir o google o programa vai abrir o google
if text == "abre o google":
    import webbrowser
    webbrowser.open("https://www.google.com.br/")
    print("Abrindo o google")

#Se o úsuario pedir para abrir o youtube o programa vai abrir o youtube
if text == "abre o youtube":
    import webbrowser
    webbrowser.open("https://www.youtube.com.br/")
    print("Abrindo o youtube")

#se pedir para abrir o site da ufca o programa vai abrir o site da ufca
if text == "abre o site da ufca":
    import webbrowser
    webbrowser.open("https://www.ufca.edu.br/")
    print("Abrindo o site da ufca")
    


