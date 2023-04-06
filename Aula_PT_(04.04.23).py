# tabuada com estrutura de aninhamento

tabuada=1
while tabuada <= 10:
    número = 1
   
    while número <= 10:
        print("%d x %d = %d" % (tabuada, número, tabuada * número))
        número+=1
    tabuada+=1

#-------------------------------------------------------------------------------------

#tabuada igual o codigo acima porem sem as estruturas de aninhamento

tabuada = 1
numero = 1

while tabuada <= 10:
    print("%d x %d = %d"% (tabuada, numero, tabuada * numero));
    numero += 1
    if numero == 11:
         numero = 1
         tabuada += 1

#fazer os exercicios slides 225/226/227

#---------------------------------------------------------------------------------
#listas

lista = [1, 10, 100];

print(lista[0]);
print(lista[1]);
print(lista[2]);

print(len(lista));#usando comando lenght(len) para estabelecer qual o temanho da minha lista

#exemplo de lista

notas = [8, 6, 4, 5, 9]
soma = 0
x = 0

while x <5:
    soma += notas[x]
    x += 1
print("Média:%5.2f"% (soma/x))

#-----------------------------------------------------------------------------------
#Exemplo 2
notas1 = [0, 0, 0, 0, 0,]
soma1 = 0
x1 = 0

while x1 < 5:
    notas1[x1] = float(input("nota %d:"% x1));
    soma1 += notas1[x1]
    x1 += 1  

x1 = 0

while x1 < 5:
    print("Nota %d:%5.2f"%(x1, notas1[x1]))
    x1 += 1
print("Média:%6.2f"%(soma1/x1))

#----------------------------------------------------------

#Adicionando valores a lista ja com as casa estabelicadas e depois selecionando um elemento dentro da lista
números = [0, 0, 0, 0, 0,]
x = 0

while x < 5:
    números[x] = int(input("Numero %d: " %(x+1)));
    x +=1

while True:
    escolhido = int(input("o numero da lista voce quer imprimir(0 para sair):"))
    if escolhido == 0 :
        break
    print("você escolheu o numero:%d "%números[escolhido-1])
   
#------------------------------------------------------------------------------
   
#Listagem 6.15 – Adição de elementos à lista
L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)#append, para adiconar valores dentro de uma lista

x = 0
while x < len(L):
    print(L[x])
x=x+1  
#---------------------------------------------------------------------

#Adiçao de listas
L = []
L = L + [1]
L += [2]
print(L)

#----------------------------------------------------------------------

#Adição de elimentos e listas a listas

L = ["a"]
L.append("b")
print (L)
L.extend(["c"])
print(L)

L.append(["d, e"])#adicionando uma lista dentro de outra lista
print(L)

# Faezr EX. slide 251(6.2/6.3/6.4)
# ----------------------------------------------------------------------
# Removendo elementos da lista
#apos deletar uma parte da sua lista, voce deve selecionar os fatores dentro da sua lista sem o numero que foi deletado, significa que a ordem deles é reordenada
L = ["a , b, c"]
print(L)
   
del L[1] # retirando o elemento localizado na posição 1 da minha lsita neste caso o "b"

print(L)

#deletandpo uma fatia inteira dentro da lista

Lista = list(range(101))
print(Lista)
del Lista[1:99]
print(Lista)

#----------------------------------------------------------------

#estudar o slide 256 e reescrever o codigo

último = 10
fila = list(range(1,último+1  ))
print(fila)
último +=1
fila.append(último)
print(fila)

# Estudar o silde 259 e reescrever o codigo nele
# arrumar a linha if opreçao =="D"


#===============================================================
# slide 262
#----------------------------------------------------------------


L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar"))
achou = False
x = 0

while x < len(L):
    if L[x] == p:
        achou = True
        break
   
    x += 1
   
if achou:
    print("%d achado na posição %d" % (p,x))
else:
    print("%d não encontrado" % p)

# ---------------------------------------------------------
# Ex slides 266
#----------------------------------------------------------------

# utilizando for e e para ´printar todos os elementos dentro da minha lista
L = [10,25 ,36, 54]
for e in L:
    print(e)

#o comando e faz com que o programa passe por todos os elementos dentro da lista apartir do zero
L = [1, 12, 123, 1234, 12345]
P = int(input("Digite o numero que voê quer encontrar: "))
for e in L:
    if e == P:
        print("Elemento encontrado")
# --------------------------------------------------------------------------------------

# EX 6.11

# ----------------------------------------------------------------------------------

#range usmaospara estabelecer o intervalo dentro de listas, por exemplo

for v in range (10):
    print (v)

for v in range(1, 10):
    print(v)
   
for v in range (20000):
    print(v)
#-----------------------------------------------------------------------------

for t in range(3, 33, 3):
    print(t, end = "")
    print()

#----------------------------------------------------------------------------------

#Enumerate
#imprimindo uma lista com e sem enumerate

L = [5, 9, 13]
x = 0
for e in L:
    print("[%d] %d" %(x,e))
    x += 1

# Com enumerate---------------------------------------------------------------------------------------------
L = [5, 9, 13]
for x, e in  enumerate(L):
    print("[%d] %d" %(x,e))

# ------------------------------------------------------------------------------
