#OLD_045
#21
from random import randint
from time import sleep

cpu_player = randint(0,2)
itens = ('Rock','Paper', 'Scissors')
player = int(input('[0] -> Rock\n'+
      '[1] -> Paper\n'+
      '[2] -> Scissors\n' +
      'Choose a Number: '))

print('1')
sleep(1)
print('2')
sleep(1)
print('3')

print('-=' * 12)
print('You choose: {}'.format(itens[player]))
print('The CPU choose: {}'.format(itens[cpu_player]))
print('-=' * 12)

if cpu_player == 0:
    if player == 0:
        print('TIE!')
    elif player == 1:
        print('PLAYERS WINS!')

    elif player == 2:
        print('CPU WINS!')
    
    else:
        print('Invalid play!')
elif cpu_player == 1:
    if player == 0:
        print('CPU WINS!')

    elif player == 1:
        print('TIE!')
    elif player == 2:
        print('PLAYERS WINS!')
    else:
        print('Invalid play!')

elif cpu_player == 2:
    if player == 0:
        print('PLAYERS WINS!')
    elif player == 1:
        print('CPU WINS!')
    elif player == 2:
        print('TIE!')
    else:
        print('Invalid play!')
print('-=' * 12)