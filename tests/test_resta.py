# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import resta

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operaciónresta
    def test_resta(self):
        assertresta(4,5) == -1
        assertresta(-1,-2) == 1
        assertresta(-7,5) == -12
        assertresta(-7,9) == -16
