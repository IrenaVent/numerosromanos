class RomanNumber():
    def __init__(self,valor):
        
        if isinstance(valor, int): # comprobarción
            self.valor = valor # atricubto valor: {"valor": 2}
            self.cadena = a_romano(valor) # atributo cadena{"cadena":"II"} -> convertir valor en cadena 
   
    def a_numero (cadena):
        acumulador = 0
        valor_ant = 0
        cuenta_repes = 0
        resta = 0
        for caracter in self.cadena:
            valor = digitos_romanos.get(caracter)
            
            if not valor:
                raise ValueError("El mío")

            if valor_ant > 0 and valor > valor_ant: #valor_ant si lo dejamos sin informar su boolen is 0
                if resta > 0:
                    raise ValueError("No se pueden concatenar dos restas")

                if cuenta_repes > 0:
                    raise ValueError("No se puede restar dentro de repeticiones")

                if valor_ant in (5,50,500):
                    raise ValueError("No se pueden restrar V, L o D")
                
                if valor_ant > 0 and valor > 10 * valor_ant:
                    raise ValueError("No se pueden restas entre digitos 10veces mayores")
                
                acumulador = acumulador - valor_ant
                acumulador = acumulador + valor - valor_ant
                resta += 1
            else:
                acumulador += valor
                resta = 0

            if valor == valor_ant:
                if valor in (5,50,500):
                    raise ValueError("No se pueden repetir V, L o D")
                cuenta_repes += 1
                if cuenta_repes == 3: 
                    raise ValueError("Demsiadas repeticiones de {}".format(caracter))
            else:
                cuenta_repes = 0 
            
            valor_ant = valor

        return acumulador

    def validar (self,n):                                           
        if not isinstance(n, int): # para comprobar el dato, "n" el dato que ponemos e "int" que debe comprobar
            raise ValueError("{} debe ser un entero".format(n)) 
            # lanzamos una excepcion
        if n < 0 or n > 3999:
            raise ValueError("{} debe estar entre 0 y 3999".format(n))

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
        