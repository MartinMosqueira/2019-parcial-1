from exadecimal import exadecimal_f

def main():
    decimal=input("ingrese un numero decimal: ")
    print(funcion(decimal))

def funcion(data):
    try:
        n=str(data)
        return exadecimal_f(n)
    except:
        return "Disculpe,solo acepto numeros"

main()