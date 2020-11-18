from functions import *


num = input("Digite um número: ")

num_out = "menos " if int(num)<0 else ""

num = str(abs(int(num)))

if len(num)<=3:
    num_out += numero_extenso(num)
else:
    num_out += numero_extenso(num[:-3]) + " mil e "
    num_out += numero_extenso(num[-3:])

print(num_out)