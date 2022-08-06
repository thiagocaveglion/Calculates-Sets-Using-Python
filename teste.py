texto = open("teste.txt", "r")
data = texto.read()
lista = list()
lista2 = list()
lista3 = list()
u = list()
i = list()
d = list()
c = list()
s = None
# u = uniao
# i = interseccao
# d = diferenca
# c = produto cartesiano
for char in data.split("\n"):
        lista.append(char)
for linha in lista:
    if linha == lista[0]:
        num = linha[0]
        continue
    if len(linha) == 1 and linha[0] in "UIDC":
        s = 2
        operacao = linha[0]
    else:
        s -= 1
    if (s == 0 or s == 1):
        lista2.append(linha.split(","))
        if s == 0:
            if operacao == "U":
                lista3 = lista2[0][:] + lista2[1][:]
                lista2.clear()
                u.append(lista3[:])
                lista3.clear()
                
            elif operacao == "I":
                for inteiro in lista2[0]:
                    if inteiro in lista2[1]:
                        lista3.append(inteiro)
                lista2.clear()
                i.append(lista3[:])
                lista3.clear()

            elif operacao == "D":
                for inteiro in lista2[0]:
                    if inteiro not in lista2[1]:
                        lista3.append(inteiro)
                lista2.clear()
                d.append(lista3[:])
                lista3.clear()

            elif operacao == "C":
                for char in lista2[0]:
                    for char2 in lista2[1]:
                        if char in "0123456789" and char2 in "0123456789":
                            lista3.append(str(int(char) * int(char2)))
                        else:
                            lista3.append(char + char2)
                lista2.clear()
                c.append(lista3[:])
                lista3.clear()

print(f"serão realizadas {num} operações")
print("operações de união geraram a(s) lista(s): ")
for j in u: print(j)
print("operações de intersecção geraram a(s) lista(s): ")
for j in i: print(j)
print("operações de diferença geraram a(s) lista(s): ")
for j in d: print(j)
print("operações de produto cartesiano geraram a(s) lista(s): ")
for j in c: print(j)
