import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} A palavra “Islam” tem origem na língua árabe e traz consigo alguns significados interessantes: “rendição”, “submissão” ou “entrega” voluntária a Deus.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} O Alcorão é o livro sagrado dos muçulmanos. O termo “Alcorão” vem da tradução da palavra árabe “al Qur’an”, que significa “a recitação”. Isso explica o fato dos muçulmanos se esforçarem para memorizar os versículos do Alcorão e recitá-los desde os primórdios do Islam.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Muhammad (Que a bênção e a paz de Deus estejam sobre ele) Foi o o último mensageiro de Deus para a humanidade.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} Primeiro pilar - O Testemunho - al-Shahadah, Segundo pilar - A Oração al-Salah, Terceiro pilar - A Doação - al-Zakah, Quarto pilar - O Jejum - al-Saum, Quinto pilar - A Peregrinação - al-Hajj {os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print('Assalamu alaikum! Bem-vindo ao MuslimBot')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - O que é o Islam?{os.linesep}[2] - O que é o Alcorão Sagrado?{os.linesep}[3] - Quem foi o Profeta Muhammad (S.A.A.S)?{os.linesep}[4] - Quais são os pilares do Islam?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()