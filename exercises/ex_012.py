price = float(input("Insert the product's price? R$"))

new_price = price - price*(5/100)

print('The new price is R${:.2f}, you have off 5%'.format(new_price))