x = float(input('Insert some Distance in Meters: '))

km = x /1000

hm = x / 100

dam = x / 10

cm = x * 100

mili = x * 1000


print('Km: {:.0f}\nHm: {:.0f}\nDam: {:.0f}\nM: {:.0f}\nCm: {:.0f}\nMm: {:.0f}'.format(km, hm, dam, x, cm, mili))