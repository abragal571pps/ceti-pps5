
import random
import string

try:
    # =================================================================
    # PALINDROMO
    # =================================================================
    cadena = "radarx"
    print(cadena == cadena[::-1])


    # =================================================================
    # CADENA MAS LARGA
    # =================================================================
    cadenas = ['aaa', 'bbbb', 'ccccc']

    #for i in range(5):
     #   cadenas.append(input('Dame tu palabra chula: '))

    aux = None;
    for i in cadenas:
        length = len(i)

        if(aux == None):          aux = i
        elif (length < len(aux)): aux = i

    print(len(aux))

    print(cadenas)
    print(sorted(cadenas))
    print(sorted(cadenas, key=str.lower))

    print(cadenas)
    print(cadenas.sort())
    print(max(cadenas))
    print(min(cadenas))


except TypeError as e :
    print("ERROR: ", e)
