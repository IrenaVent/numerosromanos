class RomanNumber():
    def __init__(self,valor):
        
        if isinstance(valor, int): # que sea un integer
            self.valor = 9
            self.cadena = a_romano(valor)

    def a_numero(self):
            pass # falta traerse desde el otro lado el programa

    def a_romano(self):

        self.validar (self.valor)
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

        return simbolos["millares"][millares] + simbolos["centenas"][centenas] + simbolos["decenas"][decenas] + simbolos["unidades"][unidades]
        