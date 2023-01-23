from ast import main

def potencia(base,exponente):
    if exponente < 0:
        return "nil"
    else:
        resultado = 1
        for i in range(exponente): #Bucle que se repite el numero de veces del exponente
            resultado = resultado * base
        return resultado


print(potencia(-5,3))


if __name__ == "__main__":
  main()