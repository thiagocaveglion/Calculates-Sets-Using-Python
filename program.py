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
o = 0
num = "algumas"
# u = uniao
# i = interseccao
# d = diferenca
# c = produto cartesiano
for char in data.split("\n"):
    lista.append(char.strip())

for indice, linha in enumerate(lista):
    if linha != "":
        if linha == lista[0] and linha in "0123456789":
            num = linha[0]
            continue
        elif len(linha) == 1 and linha.strip().upper() in "UIDC":
            s = 2
            operacao = linha.strip()
            continue
        else:
            try: s -= 1
            except: print(f"o termo {linha.strip()} é inválido, remova-o do arquivo txt na linha {indice+1}")
          
        if (s == 0 or s == 1):
            lista2.append(linha.split(","))
            if s == 0:
              
                if operacao == "U":
                    o += 1
                    lista3 = lista2[0][:] + lista2[1][:]
                    lista2.clear()
                    u.append(lista3[:])
                    lista3.clear()

                elif operacao == "I":
                    o += 1
                    for inteiro in lista2[0]:
                        if inteiro in lista2[1]:
                            lista3.append(inteiro)
                    lista2.clear()
                    i.append(lista3[:])
                    lista3.clear()

                elif operacao == "D":
                    o += 1
                    for inteiro in lista2[0]:
                        if inteiro not in lista2[1]:
                            lista3.append(inteiro)
                    lista2.clear()
                    d.append(lista3[:])
                    lista3.clear()

                elif operacao == "C":
                    o += 1
                    for char in lista2[0]:
                        for char2 in lista2[1]:
                            if char in "0123456789" and char2 in "0123456789":
                                lista3.append(str(int(char) * int(char2)))
                            else:
                                lista3.append(char + char2)
                    lista2.clear()
                    c.append(lista3[:])
                    lista3.clear()

if "" in lista: print("tente evitar os espaços em branco no arquivo txt")
print("-"*60)
if num != "algumas": print(f"foi informada a realização de {num} operações")
else: print(f"{num} operações serão realizadas")
print("operações de união geraram a(s) lista(s): ")
print("-"*60)
for j in u: 
    print(j)
    print("-"*60)
print("operações de intersecção geraram a(s) lista(s): ")
print("-"*60)
for j in i:
    print(j)
    print("-"*60)
print("operações de diferença geraram a(s) lista(s): ")
print("-"*60)
for j in d: 
    print(j)
    print("-"*60)
print("operações de produto cartesiano geraram a(s) lista(s): ")
print("-"*60)
for j in c: 
    print(j)
    print("-"*60)
print(f"foram realizadas {o} operações")
if str(o) != num: print("tente inserir o número correto de operações no txt")
print("-"*60)
