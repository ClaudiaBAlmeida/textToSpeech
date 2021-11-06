#importando as bibliotecas que serão utilizadas. A gtts é um módulo do Google que transforma texto em fala.
#text-to-speech
import gtts
#playsound vai "tocar" o som que iremos gerar agora com a gtts.
from playsound import playsound

#chamando o arquivo de texto.
with open('speech.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('frase_tech_recruiters.mp3')
        playsound('frase_tech_recruiters.mp3')