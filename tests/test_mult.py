# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import mult

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación mult
    def test_mult(self):
        assertmult(4,5) == 20
        assertmult(-1,-2) == 2
        assertmult(-7,5) == -35
        assertmult(-7,9) == -63
