class RomanNumber():
    simbolos = {
        "unidades": ["","I","II","III","IV","V","VI","VII","VIII","IX"],
        "decenas": ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
        "centenas": ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
        "millares": ["","M", "MM", "MMM"] }
    
    digitos_romanos = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    def __init__(self,valor):    
        
        if isinstance(valor, int):
            self.valor = valor 
            self.cadena = self.a_romano() 

        elif isinstance(valor, str):
            self.cadena = valor 
            self.valor = self.a_numero()
        
        else:
            raise ValueError ("Solo admite int y cadena")

    def validar (self):                                           
        if not isinstance(self.valor, int): # para comprobar el dato, "n" el dato que ponemos e "int" que debe comprobar
            raise ValueError("{} debe ser un entero".format(self.valor)) 
            # lanzamos una excepcion
        if self.valor < 0 or self.valor > 3999:
            raise ValueError("{} debe estar entre 0 y 3999".format(self.valor))

    def a_romano(self):

        self.validar()
        c = str (self.valor)

        unidades = decenas = centenas = millares = 0

        if len(c) >= 1:
            unidades = int(c[-1])
        if len(c) >= 2:
            decenas = int(c[-2])
        if len(c) >= 3:
            centenas = int(c[-3])
        if len(c) >= 4:
            millares = int(c[-4])

        return self.simbolos["millares"][millares] + self.simbolos["centenas"][centenas] + self.simbolos["decenas"][decenas] + self.simbolos["unidades"][unidades]
        
    def a_numero (self):

        acumulador = 0
        valor_ant = 0
        cuenta_repes = 0
        resta = 0
        for caracter in self.cadena:
            valor = self.digitos_romanos.get(caracter)
            
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

# métodos mágicos:

    def __str__(self): # método para transfromar en cadena tu clase
        return (f"Soy el número {self.cadena}")
    
    def __repr__(self): # método para ver el contenido/representación de la clase, llama a str
        return self.__str__()
    
    def __len__(self):
        return len(sel.cadena)
    
    def __eq__(self, other):
        if isinstance(other, RomanNumber):
            return self.valor == other.valor
        if isinstance(other, int):
            return self.valor == other
        if isinstance(other, float):
            return self.valor == other
        if isinstance(other, str):
            return self.cadena == other
        raise ValueError(f"{other} solo puede ser RomanNumber, int, float o str")

    def __ne__(self, other):
        if isinstance(other, RomanNumber):
            return other.valor != self.valor
        if isinstance(other, int):
            return self.valor != other
        if isinstance(other, float):
            return self.valor != other
        if isinstance(other, str):
            return self.cadena != other
        raise ValueError(f"{other} solo puede ser RomanNumber, int, float o str")

    def __gt__(self, other):
        if isinstance(other, RomanNumber):
            return self.valor > other.valor
        if isinstance(other, int):
            return self.valor > other
        if isinstance(other, float):
            return self.valor > other
        if isinstance(other, str):
            return self.valor > RomanNumber(other).valor
        raise ValueError(f"{other} solo puede ser RomanNumber, int, float o str")

    def __ge__(self, other):
        if isinstance(other, RomanNumber):
            return self.valor >= other.valor
        if isinstance(other, int):
            return self.valor >= other
        if isinstance(other, float):
            return self.valor >= other
        if isinstance(other, str):
            return self.valor >= RomanNumber(other).valor
        raise ValueError(f"{other} solo puede ser RomanNumber, int, float o str")

    def __lt__(self, other):
        if isinstance(other, RomanNumber):
            return self.valor < other.valor
        if isinstance(other, int):
            return self.valor < other
        if isinstance(other, float):
            return self.valor < other
        if isinstance(other, str):
            return self.valor < RomanNumber(other).valor
        raise ValueError(f"{other} solo puede ser RomanNumber, int, float o str")

    def __le__(self, other):
        if isinstance(other, RomanNumber):
            return self.valor <= other.valor
        if isinstance(other, int):
            return self.valor <= other
        if isinstance(other, float):
            return self.valor <= other
        if isinstance(other, str):
            return self.valor <= RomanNumber(other).valor
        raise ValueError(f"{other} solo puede ser RomanNumber, int, float o str")

    def __add__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.valor + other.valor)
        if isinstance(other, int):
            return RomanNumber(self.valor + other)
        if isinstance(other, float):
            raise ValueError(f"{other} solo puede ser RomanNumber, int, o str")
        if isinstance(other, str):
            return RomanNumber(self.valor + RomanNumber(other).valor)
        raise ValueError(f"{other} solo puede ser RomanNumber, int o str")
    
    def __radd__(self, other): #suma reversa
        return self.__add__(other)


    def __sub__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.valor - other.valor)
        if isinstance(other, int):
            return RomanNumber(self.valor - other)
        if isinstance(other, float):
            raise ValueError(f"{other} solo puede ser RomanNumber, int, o str")
        if isinstance(other, str):
            return RomanNumber(self.valor - RomanNumber(other).valor)
        raise ValueError(f"{other} solo puede ser RomanNumber, int o str")

    def __rsub__(self, other): #resta reversa
        if isinstance(other, int):
            return RomanNumber((self.valor - other)* -1)
        elif isinstance(other, str):
            return RomanNumber((self.valor - RomanNumber(other).valor)* -1)
        else:
            return self.__sub__(other)
        
