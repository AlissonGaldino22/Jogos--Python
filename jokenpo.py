print("JO-KEN-PÔ")
play1 = input("Digite sua jogada, pedra, papel ou tesoura: ").lower()
play2 = input("Digite sua jogada, pedra, papel ou tesoura: ").lower()

if play1 == play2:
    print("Empate!")
elif play1 == "pedra":
    if play2 == "papel":
        print("Vitória do Player 2!")
    elif play2 == "tesoura":
        print("Vitória do Player 1!")
    else:
        print("Jogada inválida!")
elif play1 == "papel":
    if play2 == "pedra":   
        print("Vitória do Player 1!")
    elif play2 == "tesoura":
        print("Vitória do Player 2!")
    else:
        print("Jogada inválida!")
elif play1 == "tesoura":
    if play2 == "papel":
        print("Vitória do Player 1!")
    elif play2 == "pedra":
        print("Vitória do Player 2!")
    else:
        print("Jogada inválida!")
else:
    print("Jogada inválida!")