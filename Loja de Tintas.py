#Para 108 metros quadrados precisa de 18L de tinta

#1l = 6m
#uma lata = 18L = R$80,00
#um galão = 3,6L = R$25,00

#18L = 108m2
#3,6 = 21,6m2 (utilzart float)

import math

area = (float(input("Digite a área a ser pintada : ")))

tinta_necessaria = (area / 6)
tinta_necessaria_folga = tinta_necessaria * 1.10

print("Preços das Tintas:")
print("Galões: 3,6L - R$25")
print("Latas: 18L - R$80")
print()

galao = 3.6
lata = 18

print(f"COBERTURA DA TINTA: {tinta_necessaria}")
print("\033[32mOPÇÕES:\033[0m")
print("1 - Comprar somente galões")
print("2 - Comprar somente latas")
print("3 - Comprar ambos")
decisao = input("Digite a opção \033[31mdesejada\033[0m: ")
print()

if decisao == "1":
   qntd_galao = math.ceil(tinta_necessaria / galao)
   tinta_comprada = galao * qntd_galao
   preco_total = 25 * qntd_galao
   print(f"Quantidade de galões precisos: \033[32m{qntd_galao}\033[0m")
   print(f"Cobertura do lugar: \033[32m{tinta_necessaria}\033[0m")
   print(f"Quantidade de tinta comprada: \033[32m{tinta_comprada}\033[0m")
   print(f"Preço Total: \033[32mR${preco_total}\033[0m")
    
elif decisao == "2":
   qntd_lata = math.ceil(tinta_necessaria / lata)
   tinta_comprada = lata * qntd_lata
   preco_total = 80 * qntd_lata
   print(f"Quantidade de latas precisas: \033[32m{qntd_lata}\033[0m")
   print(f"Cobertura do lugar: \033[32m{tinta_necessaria}\033[0m")
   print(f"Quantidade de tinta comprada: \033[32m{tinta_comprada}\033[0m")
   print(f"Preço Total: \033[32mR${preco_total}\033[0m")

elif decisao == "3":
   qntd_lata = (tinta_necessaria_folga // lata)
   sobra = tinta_necessaria_folga % lata
   qntd_galao = math.ceil(sobra / galao) 

   litros_galao = galao * qntd_galao
   litros_lata = lata * qntd_lata

   total_tinta_comprada = litros_galao + litros_lata
   preco_total = (qntd_lata * 80) + (qntd_galao * 25)
   
   print(f"Cobertura do lugar: \033[32m{tinta_necessaria}\033[0m")
   print(f"Quantidade de latas necessárias: \033[32m{qntd_lata}\033[0m")
   print(f"Quantidade de galões necessários: \033[32m{qntd_galao}\033[0m")
   print(f"Quantidade total de tinta comprada: \033[32m{total_tinta_comprada}\033[0m")
   print(f"Preço Total: \033[32mR${preco_total:.2f}\033[0m")