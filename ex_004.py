coisa = input('Insert something: ')
# type() -> checks the variable's type 
print('The tpyte is: ', type(coisa))
# isspace() -> checks if what was entered contains only spaces
print('Are there only spaces?', coisa.isspace())
# isnumeric() -> checks if what was entered is a number
print('Is it a number? ', coisa.isnumeric())
# isalpha() -> checks if what was entered is alphabetical
print('Is it alphabetical? ', coisa.isalpha())
# isalnum() -> checks if what was entered is alphanumeric
print('Is it alphanumerical? ', coisa.isalnum())
# isalnum() -> checks if what was entered is upper
print('Is it upper? ', coisa.isupper())
# isalnum() -> checks if what was entered is upper
print('Is it lower? ', coisa.islower())
# istitle() -> checks if what was entered is capitalized
print('Is it Capitalized? ', coisa.istitle())