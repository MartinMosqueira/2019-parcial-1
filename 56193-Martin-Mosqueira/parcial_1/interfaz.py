from exadecimal import exadecimal_f

def main():
    decimal=input("ingrese un numero decimal: ")
    print(funcion(decimal))

def funcion(data):
    try:
        n=int(data)
        return exadecimal_f(n)

    except TypeError:
        return 'Disculpe,solo acepto numeros enteros'

    except ValueError:
        return 'Disculpe,solo acepto numeros enteros'

main()