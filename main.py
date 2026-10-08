meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "RUSHAR": "Avançar para cima de um inimigo",
            "KITAR": "Sair do jogo/ligação",
            "MUTADO": "Estar com o microfone desligado",
            "BOT": "Robô",
            "SPEEDRUN": "Terminar algo muito rápido",
            "BANGAR": "Cegar os adversários",
            "KIKAR": "Expulsar alguém"
            }

word = input("Qual palavra quer saber o sigificado?").upper()
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Não encontrado")
