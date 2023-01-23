from ast import main
#Generar todas las permutaciones de la palabra dada.

def permutaciones(palabra):
    if len(palabra) <= 1:
        return palabra
    else:
        tmp = []
        for perm in permutaciones(palabra[1:]):
            for i in range(len(perm)+1):
                tmp.append(perm[:i] + palabra[0:1] + perm[i:])
        return tmp

print(permutaciones("AAAB"))

#Eliminar las permutaciones repetidas.
 
def eliminar_repetidos(lista):
    lista.sort()
    for i in range(len(lista)-1, 0, -1):
        if lista[i] == lista[i-1]:
            del lista[i]
    return lista

print(eliminar_repetidos(permutaciones("AAAB")))

#Encontrar la posición partiendo de 1 de la palabra dada en la lista de permutaciones ordenadas

def posicion(palabra, lista):
    resultado = lista.index(palabra) + 1
    print(palabra,"=",resultado)

print(posicion("PREGUNTA", eliminar_repetidos(permutaciones("PREGUNTA"))))

if __name__ == "__main__":
  main()