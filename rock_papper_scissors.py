import random

def computer_move():
    move = random.randint(1,3)
    return move

def rules(computer_move, player_move):
    if computer_move == player_move:
        print('Empate')
    elif (computer_move == 1 and player_move == 3) or (computer_move == 2 and player_move == 1) or (computer_move == 3 and player_move == 2):
        print('Computador ganhou')
        return 1
    elif (player_move == 1 and computer_move == 3) or (player_move == 2 and computer_move == 1) or (player_move == 3 and computer_move == 2):
        print('Você ganhou')
        return 2

def single_game():
    print('Escolha sua jogada:')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    player_move = int(input())
    return rules(player_move,computer_move())

def best_three():
    computer_points = user_points = 0
    for i in range(1,4):
        print('\nRodada ',i)
        result = single_game()
        if result == 1:
            computer_points += 1
        elif result == 2:
            user_points += 1
    print('\nPlacar: {} Computador X {} Usuário'.format(computer_points, user_points))


print('*****Bem Vindo ao Jogo Pedra, Papel e Tesoura******')
valide = False
while not valide:
    print('1 - Para jogo solo')
    print('2 - Melhor de Três')
    choice = int(input())
    if choice == 1:
        single_game()
        valide = True
    elif choice == 2:
        best_three()
        valide = True
    else:
        print('Digite uma opção válida!')
        valide = False
    
