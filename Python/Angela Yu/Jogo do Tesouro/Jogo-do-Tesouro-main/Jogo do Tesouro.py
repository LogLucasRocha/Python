print("     .       .    )        .           .\n    .       *             .         .\n                .                      .\n   .       .                   .\n                                *        .\n      .   '               .              .\n              _.---._   .            .     *\n    *       .'       '.\n        _.-~===========~-._\n       (___________________)       .   *\n  __  .'     \_______/   .'  ______        __\n    |              .'  .'   |      |      |  |\n    |             '         |      |      |  |\n    |                       |      |   ___|  |_\n  __|_______________________|__..--~~~~ GTA VI    ~--.\n                    /|\\\n                   /   \\\n                  /  |  \\\n                 /       \\\n   \|/          /    |    \\\n               /           \\\n              /      |      \\\n             /               \\\n")

print("Olá, seja bem vindo a Ilha do Tesouro! \nSua missão é encontrar o tesouro. ")

caminho_inicial = input("Você está em uma encruzilhada, qual caminho você quer seguir? Esquerda ou Direita? \n").lower()

if caminho_inicial == "esquerda":
    esperar_ou_nadar = input("Você chegou em um lago. Tem uma ilha no meio do lago. Escreva 'esperar' para esperar por um barco ou 'nadar' para nadar até a ilha: \n").lower()
    if esperar_ou_nadar == "esperar":
       porta = input("Você chegou na ilha sem problemas. Nessa ilha, existe uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual porta você escolhe? \n").lower()
       if porta == "vermelha":
          print("Você foi queimado pelo fogo. GAME OVER!")
       elif porta == "amarela":
          print("Você venceu! PARABÉNS!")
       elif porta == "azul":
          print("Você foi comido por um LEÃO. GAME OVER!")
       else:
          print("Você evaporou, GAME OVER!")
    else: 
      print("Você foi atacado por um tubarão, GAME OVER!")
else: 
  print("Você caiu em um burcao, GAME OVER!")