number = int(input('Type a number to see the multiplication table: '))

print('-'*20)
for n in range(1,11):
    print('| {:3} x {:3} = {:3} |'.format(number, n, number*n))
print('-'*20)

print('-'*20)
print('| {} x 1 = {:4} |'.format(number, number*1))
print('| {} x 2 = {:4} |'.format(number, number*2))
print('| {} x 3 = {:4} |'.format(number, number*3))
print('| {} x 4 = {:4} |'.format(number, number*4))
print('| {} x 5 = {:4} |'.format(number, number*5))
print('| {} x 6 = {:4} |'.format(number, number*6))
print('| {} x 7 = {:4} |'.format(number, number*7))
print('| {} x 8 = {:4} |'.format(number, number*8))
print('| {} x 9 = {:4} |'.format(number, number*9))
print('| {} x 10 = {:4}|'.format(number, number*10))
print('-'*20)