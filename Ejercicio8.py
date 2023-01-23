from ast import main

#Extraer en numero
def extraerNumero(cadena):
    for i in range(len(cadena)):
        if cadena[i].isdigit():
            numero = ""
            while i < len(cadena) and cadena[i].isdigit():
                numero += cadena[i]
                i += 1
            return int(numero)
        
#ordenar de mayor a menor en función de número extraido y separar en lineas
def ordenar(cadenas):
    cadenas.sort(key=extraerNumero,reverse=True)
    resultado = ""
    for i in range(len(cadenas)):
        resultado += cadenas[i] + "\n"
    return resultado

#Separar la cadena en lineas


cadenas = ["5 anillos de oro,", "4 pájaros cantando,", "3 gallinas francesas,", "2 tórtolas y", "10 señores un salto,", "9 damas bailando,", "8 criadas un ordeño,", "7 cisnes nadando,", "6 gansos una puesta,", "1 perdiz en un peral.", "tubería de 11 gaiteros,","El día 12 de Navidad mi verdadero amor me dio", "12 bateristas tocando el tambor,"]
print(ordenar(cadenas))




if __name__ == "__main__":
  main()