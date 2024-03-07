largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
litro_tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m^2.'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(litro_tinta))