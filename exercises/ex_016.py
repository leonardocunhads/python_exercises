size_input = input('How big is your House? (in square feet)\n')

square_feet = int(size_input)

square_metres = square_feet / 10.8

print(f"{square_feet} square feet is {square_metres:.2f} square metres.")