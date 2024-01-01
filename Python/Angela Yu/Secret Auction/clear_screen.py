import os

def clear_screen():
    # Verifica o sistema operacional
    if os.name == 'posix':  # Unix/Linux/MacOS/BSD
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')

# Use a função para limpar a tela
clear_screen()