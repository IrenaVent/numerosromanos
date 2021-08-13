import unittest
from romanclass import RomanNumber

class RomanNumberClassTest(unittest.TestCase):
    def test_crear_Numero_romano(self):
        uno = RomanNumber(1)
        self.assertEqual(uno.valor, 1)
        self.assertEqual(uno.cadena,"I")

        with self.assertRaises(ValueError):
            cuatromil = RomanNumber(4000)
        
        dos = RomanNumber("II")
        self.assertEqual(dos.valor, 2)
        self.assertEqual(dos.cadena, "II")

        with self.assertRaises(ValueError):
            cuatromil = RomanNumber("MMMM")
    
    def test_metodos_magicos_representaciones(self):
        uno = RomanNumber(1)

        self.assertEqual(uno, "I")

    def test_metodos_magicos_comparaciones(self):
        uno = RomanNumber(1) # estamos creando un objeto de la class RomanNumber, objeto que asignamos a una variable llamada "uno", estamos instancionado objetos
        dos = RomanNumber(2)

        self.assertEqual(uno, 1)
        self.assertEqual(uno, 1.0)
        self.assertEqual(uno, "I")
        with self.assertRaises(ValueError):
            self.assertEqual(uno, {})
        
        self.assertNotEqual(uno, 2)
        self.assertNotEqual(uno, 1.1)
        self.assertNotEqual(uno, 2.0)
        self.assertNotEqual(uno, "II")
        with self.assertRaises(ValueError):
            self.assertEqual(uno, {}) #podríamos implemente indicar "uno == {}", igual que más abajo, porque comparamos una igualdad

        self.assertTrue(dos > uno)
        self.assertTrue(dos > 1)
        self.assertTrue(dos > 1.3)
        self.assertFalse(dos > "DI")
        with self.assertRaises(ValueError):
            dos > {}

        self.assertTrue(dos >= uno)
        self.assertTrue(uno >= 1)
        self.assertTrue(dos >= 1.3)
        self.assertFalse(dos >= "DI")
        with self.assertRaises(ValueError):
            dos > {}

        self.assertFalse(dos < uno)
        self.assertFalse(dos < 1)
        self.assertFalse(dos < 1.3)
        self.assertFalse(dos > "DI")
        with self.assertRaises(ValueError):
            dos > {}

        self.assertFalse(dos <= uno)
        self.assertFalse(dos <= 1)
        self.assertFalse(dos <= 1.3)
        self.assertTrue(dos <= "DI")
        with self.assertRaises(ValueError):
            dos > {}

    def test_metodos_magicos_aritmeticos(self):
        uno = RomanNumber(1)
        dos = RomanNumber(2)
        cinco = RomanNumber(5)

        # __add__
        self.assertEqual(dos, uno + 1)
        self.assertEqual(dos, uno + uno)
        self.assertEqual(dos, uno + "I")
        # self.assertEqual(RomanNumber(2), uno += 1)
        self.assertEqual(dos, 1 + uno)
        self.assertEqual(dos, "I" + uno)
        with self.assertRaises(ValueError):
            uno + 1.3
            uno + {}

        # __sub__
        self.assertEqual(uno, dos - 1)
        self.assertEqual(uno, dos - uno)
        self.assertEqual(uno, dos - "I")
        self.assertEqual(uno, 2 - uno)
        self.assertEqual(uno, "II" - uno)
        # self.assertEqual(RomanNumber(1), dos -= 1)
        with self.assertRaises(ValueError):
            dos - 1.3
            dos - {}
            2 - uno

        # __sub__
        self.assertEqual(dos, dos * 1)
        self.assertEqual(dos, dos * uno)
        self.assertEqual(dos, dos * "I")
        self.assertEqual(dos, 2 * uno)
        self.assertEqual(dos, "II" * uno)
        with self.assertRaises(ValueError):
            dos * 1.3
            dos * {}
            dos * -4

        # __truediv__
        self.assertEqual(dos, dos / 1)
        self.assertEqual(dos, dos / uno)
        self.assertEqual(dos, dos / "I")
        self.assertEqual(cinco, 10 / dos)
        self.assertEqual(dos, "II" / uno)
        with self.assertRaises(ValueError):
            dos / 1.3
            dos / {}
            dos / -4

        # __floordiv__
        self.assertEqual(dos, cinco // 2)
        self.assertEqual(dos, cinco // dos)
        self.assertEqual(dos, cinco // "II")
        self.assertEqual(dos, 5 // dos)
        self.assertEqual(dos, "V" // dos)
        with self.assertRaises(ValueError):
            dos // 1.3
            dos // {}
            dos // -4
        
        # __mod__
        self.assertEqual(uno, cinco % 2)
        self.assertEqual(uno, cinco % dos)
        self.assertEqual(uno, cinco % "II")
        self.assertEqual(uno, 5 % dos)
        self.assertEqual(uno, "V" % dos) # error: not all arguments converted during string formatting / error de interpretación...falta resolver
        with self.assertRaises(ValueError):
            dos % 1.3
            dos % {}
            dos % -4
    



