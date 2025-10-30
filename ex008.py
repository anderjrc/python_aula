medida = float(input('Uma distãncia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida} corresponde a \n{km}km\n{hm}hm\n{dam}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')
