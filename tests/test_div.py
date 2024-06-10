# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import div

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operacióndiv
    def test_div(self):
        assertdiv(4,2) == 2
        assertdiv(100,10) == 10
        assertdiv(-72,8) == -9
        assertdiv(10,-2) == -20
