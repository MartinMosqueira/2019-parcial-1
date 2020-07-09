def exadecimal_f(numero):
    lista=[]

    if numero <= 16:
        if numero < 10:
            lista.append(str(numero))
        if numero == 10:
            lista.append('A')
        if numero == 11:
            lista.append('B')
        if numero == 12:
            lista.append('C')
        if numero == 13:
            lista.append('D')
        if numero == 14:
            lista.append('E')
        if numero == 15:
            lista.append('F')
        if numero == 16:
            lista.append('10')               
    else:
        while numero > 16:
            numero=numero/16
            decimal=abs(numero)-abs(int(numero))
            exa=decimal*16
            if exa >= 10:
                if exa == 10:
                    lista.append('A')
                if exa == 11:
                    lista.append('B')
                if exa == 12:
                    lista.append('C')
                if exa == 13:
                    lista.append('D')
                if exa == 14:
                    lista.append('E')
                if exa == 15:
                    lista.append('F')
            else:
                lista.append(int(exa))
                
            numero=int(numero)
            if numero < 16:
                lista.append(numero)
    lista.reverse()
    exadecimal=''.join([str(_) for _ in lista])
    return exadecimal
