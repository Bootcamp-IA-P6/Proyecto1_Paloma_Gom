"""
Script para ejecutar todos los tests del proyecto Digital Taximeter.
"""
import unittest
import sys
import os

# Agregar el directorio principal al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_all_tests():
    """Ejecutar todos los tests del proyecto."""
    print("=" * 50)
    print("EJECUTANDO TESTS - DIGITAL TAXIMETER")
    print("=" * 50)
    
    # Descubrir y ejecutar todos los tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ TODOS LOS TESTS PASARON CORRECTAMENTE")
    else:
        print("❌ ALGUNOS TESTS FALLARON")
        print(f"Errores: {len(result.errors)}")
        print(f"Fallos: {len(result.failures)}")
    print("=" * 50)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    run_all_tests()
