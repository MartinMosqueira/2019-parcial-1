def exadecimal_f(numero):
    exadecimal="0123456789ABCDEF"
    texto=""

    if numero <10:
        return numero
    else:
        while numero > 16:
            resto=int(numero/16)
        for letra in resto:
            digito1=str(exadecimal.find(letra))

        digito2=numero-(16*resto)
        for letra in digito2:
            digito2=str(exadecimal.find(letra))

        texto=digito1 + digito2
        return texto

