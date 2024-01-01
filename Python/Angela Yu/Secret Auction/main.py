from clear_screen import clear_screen
from art import logo

print(logo)

bids_log = []

print("Bem-Vind@ ao leilão secreto!")

def get_bidder():
    bids_log.append({
      "nome" : input("Qual o seu nome? "),
      "valor" : input("Qual o seu lance? R$ ")
    })

def get_winner():
    highest_bid = 0
    winner = ""
    for bid in bids_log:
        if float(bid["valor"]) > highest_bid:
            highest_bid = float(bid["valor"])
            winner = bid["nome"]
    print(f"O vencedor é {winner} com o lance de R$ {highest_bid}")

def get_more_bidders():
    more_bidders = input("Há mais alguém para dar um lance? Digite 'sim' ou 'não' ").lower()
    if more_bidders == "sim":
        clear_screen()
        get_bidder()
        get_more_bidders()
    else:
        get_winner()

get_bidder()
get_more_bidders()
