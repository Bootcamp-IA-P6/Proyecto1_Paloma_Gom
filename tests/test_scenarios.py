"""
Tests de integración para validar escenarios completos del taxímetro.
"""
import unittest
import sys
import os

# Agregar el directorio principal al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import calculate_fare


class TestTaximeterScenarios(unittest.TestCase):
    """Tests de escenarios reales del taxímetro."""
    
    def test_viaje_urbano_corto(self):
        """Escenario: Viaje urbano corto con varias paradas."""
        # 2 min parado en semáforos + 8 min movimiento
        tiempo_parado = 2 * 60  # 120 segundos
        tiempo_movimiento = 8 * 60  # 480 segundos
        
        resultado = calculate_fare(tiempo_parado, tiempo_movimiento)
        esperado = (120 * 0.02) + (480 * 0.05)  # 2.40 + 24.00 = 26.40€
        
        self.assertEqual(resultado, esperado)
        self.assertGreater(resultado, 20)  # Mínimo razonable
        self.assertLess(resultado, 50)     # Máximo razonable
    
    def test_viaje_autopista(self):
        """Escenario: Viaje por autopista, poco tiempo parado."""
        # 30 segundos parado + 25 min movimiento
        tiempo_parado = 30
        tiempo_movimiento = 25 * 60  # 1500 segundos
        
        resultado = calculate_fare(tiempo_parado, tiempo_movimiento)
        esperado = (30 * 0.02) + (1500 * 0.05)  # 0.60 + 75.00 = 75.60€
        
        self.assertEqual(resultado, esperado)
        self.assertGreater(resultado, 70)  # Viaje largo
    
    def test_viaje_trafico_pesado(self):
        """Escenario: Mucho tráfico, más tiempo parado que movimiento."""
        # 15 min parado + 10 min movimiento
        tiempo_parado = 15 * 60     # 900 segundos
        tiempo_movimiento = 10 * 60  # 600 segundos
        
        resultado = calculate_fare(tiempo_parado, tiempo_movimiento)
        esperado = (900 * 0.02) + (600 * 0.05)  # 18.00 + 30.00 = 48.00€
        
        self.assertEqual(resultado, esperado)
    
    def test_tarifas_correctas(self):
        """Verificar que las tarifas están bien configuradas."""
        # Las tarifas deben ser las esperadas
        tarifa_parado = 0.02     # €/segundo
        tarifa_movimiento = 0.05  # €/segundo
        
        # Test con 1 segundo de cada tipo
        resultado = calculate_fare(1, 1)
        esperado = tarifa_parado + tarifa_movimiento
        
        self.assertEqual(resultado, esperado)
        
        # El movimiento debe costar más que estar parado
        self.assertGreater(tarifa_movimiento, tarifa_parado)
    
    def test_precision_decimales(self):
        """Verificar que los cálculos mantienen precisión adecuada."""
        # Tiempo que resulte en decimales
        tiempo_parado = 33      # 33 * 0.02 = 0.66
        tiempo_movimiento = 47  # 47 * 0.05 = 2.35
        
        resultado = calculate_fare(tiempo_parado, tiempo_movimiento)
        esperado = 3.01  # 0.66 + 2.35 = 3.01€
        
        self.assertEqual(resultado, esperado)
        
        # Verificar que el resultado está redondeado correctamente a 2 decimales
        self.assertEqual(resultado, round(resultado, 2))


if __name__ == '__main__':
    unittest.main()
