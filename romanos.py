simbolos = {
    "unidades": ["","I","II","III","IV","V","VI","VII","VIII","IX"],
    "decenas": ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
    "centenas": ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
    "millares": ["","M", "MM", "MMM"] }

digitos_romanos = {
    "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def a_numero (cadena):
    acumulador = 0
    valor_ant = 0
    for caracter in cadena:
        valor = digitos_romanos[caracter]
        if valor > valor_ant:
            if valor_ant in (5,50,500):
                raise ValueError("No se pueden restrar V, L o D")
            
            if valor_ant > 0 or valor > 10 * valor_ant:
                raise ValueError("No se pueden restas entre digitos 10veces mayores")
            
            acumulador = acumulador - valor_ant
            acumulador = acumulador + valor - valor_ant
        else:
            acumulador += valor
        
        valor_ant = valor

    return acumulador

def validar (n):                                           
    if not isinstance(n, int): # para comprobar el dato, "n" el dato que ponemos e "int" que debe comprobar
        raise ValueError("{} debe ser un entero".format(n)) 
        # lanzamos una excepcion
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

    # otra forma de solventar is "if"
    # c= {:04d}.format(n)
    # unidades = int(c[-1])
    # decenas = int(c[-2])
    # centenas = int(c[-3])
    # millares = int(c[-4])

    return simbolos["millares"][millares] + simbolos["centenas"][centenas] + simbolos["decenas"][decenas] + simbolos["unidades"][unidades]


  
