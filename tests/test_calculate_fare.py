"""
Tests para la función calculate_fare del taxímetro digital.
"""
import unittest
import sys
import os

# Agregar el directorio principal al path para importar main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import calculate_fare


class TestCalculateFare(unittest.TestCase):
    """Tests unitarios para la función calculate_fare."""
    
    def test_solo_tiempo_parado(self):
        """Test: Solo tiempo detenido, sin movimiento."""
        resultado = calculate_fare(100, 0)  # 100 segundos parado
        esperado = 100 * 0.02  # 2.00€
        self.assertEqual(resultado, esperado)
    
    def test_solo_tiempo_movimiento(self):
        """Test: Solo tiempo en movimiento, sin paradas."""
        resultado = calculate_fare(0, 100)  # 100 segundos movimiento
        esperado = 100 * 0.05  # 5.00€
        self.assertEqual(resultado, esperado)
    
    def test_tiempo_mixto(self):
        """Test: Combinación de tiempo parado y en movimiento."""
        resultado = calculate_fare(60, 120)  # 60s parado + 120s movimiento
        esperado = (60 * 0.02) + (120 * 0.05)  # 1.20 + 6.00 = 7.20€
        self.assertEqual(resultado, esperado)
    
    def test_tiempo_cero(self):
        """Test: Sin tiempo parado ni en movimiento."""
        resultado = calculate_fare(0, 0)
        esperado = 0.0
        self.assertEqual(resultado, esperado)
    
    def test_numeros_decimales(self):
        """Test: Manejo de números decimales."""
        resultado = calculate_fare(30.5, 45.7)  # Decimales
        esperado = round((30.5 * 0.02) + (45.7 * 0.05), 2)  # Resultado redondeado
        self.assertEqual(resultado, esperado)
    
    def test_viaje_corto(self):
        """Test: Viaje muy corto (1 segundo de cada tipo)."""
        resultado = calculate_fare(1, 1)
        esperado = (1 * 0.02) + (1 * 0.05)  # 0.02 + 0.05 = 0.07€
        self.assertEqual(resultado, esperado)
    
    def test_viaje_largo(self):
        """Test: Viaje largo (1 hora = 3600 segundos)."""
        resultado = calculate_fare(1800, 1800)  # 30 min parado + 30 min movimiento
        esperado = (1800 * 0.02) + (1800 * 0.05)  # 36 + 90 = 126€
        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()
