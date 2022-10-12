import random as rnd
print("Pedra, papel e tesoura")
print("Escolha papel, pedra ou tesoura:")
player1 = input()
player2 = rnd.randint(1,3)
result_robo = {1: "pedra", 2: "papel", 3: "tesoura"}
print("Resultado do robo: "+ result_robo[player2])

result = {"pedra":1, "papel":2, "tesoura":3}
player1 = result[player1]
if player1 == player2:  
    print("Empate")
elif player1 == 1 and player2 == 2: 
    print("Player 2 ganhou")
elif player1 == 2 and player2 == 3: 
    print("Player 2 ganhou")
elif player1 == 3 and player2 == 1:
    print("Player 2 ganhou")
else:
    print("Player 1 ganhou")