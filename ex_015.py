# F-STRING

name = 'José'

greeting = 'Hello, Bruno'

print(greeting)
print('-' * 12)

# -------------------------------

print(f'Hello, {name}')
print('-' * 12)

print('Hello, {}'.format(name))
print('-' * 12)

greeting = 'Hello, {}'

with_name = greeting.format("Marcos")

print(with_name)

# -------------------------------
print('-' * 12)
longer_phrase = 'Hello, {}. Today is {}'

formatted = longer_phrase.format('Junior', "Saturday")

print(formatted)