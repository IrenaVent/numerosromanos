simbolos = {
    "unidades": ["","I","II","III","IV","V","VI","VII","VIII","IX"],
    "decenas": ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
    "centenas": ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
    "millares": ["","M", "MM", "MMM"] }

def validar (n):                                            # restricciones: 0 < n < 4000, que sea un entero
    if not isinstance(n, int):                                  # para comprobar el dato, "n" el dato que ponemos e "int" que debe comprobar
        raise ValueError("{} debe ser un entero".format(n)) # lanzamos una excepcion
    if 0 > n or n > 3999:
        raise ValueError("{} debe estar entre 0 y 3999".format(n))


def a_romano(n):

    # después descomponer 
    # traducir
    # finalizas concatenando

    validar (n)
    c = str (n)

    unidades = decenas = centenas = millares = 0

    if len(c) >= 1:
        unidades = int(c[-1])
    
    if len(c) >= 2:
        decenas = int(c[-2])

    if len(c) >= 3:
       centenas = int(c[-3])

    if len(c) >= 4:
       millares = int(c[-4])

    componentes = (millares, centenas, decenas, unidades)

    return simbolos["millares"][millares] + simbolos["centenas"][centenas]

  
