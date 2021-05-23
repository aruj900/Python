A = [5, 17, 1000, 11]
B = 3
lista = []
iteraciones = [0]
def permutate(l, k):
    if k == len(l):
        if not l in lista:
            lista.append(l)
        return
    for i in l:
        aux = l[:]
        aux.remove(i)
        result = permutate(aux, k)
        iteraciones[0] += 1
        if not result in lista and result:
            lista.append(result)

permutate(A,B)
for i in lista:
    if sum(i) <= 1000:
        print(i)