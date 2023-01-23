from ast import main

def potencia_de_cuatro(num):
    if type(num) != int or num <= 0:
        return False
    while num > 1:
        if num % 4 != 0:
            return False
        num = num / 4
    return True

if __name__ == "__main__":
  main()