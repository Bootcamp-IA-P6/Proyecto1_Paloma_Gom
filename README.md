# Digital Taximeter 🚕

```
╔══════════════════════════════════════════════════════════════╗
║                    DIGITAL TAXIMETER                         ║
║                  Sistema de Taxímetro Digital                ║
║                         🚕 v1.0 🚕                          ║
╚══════════════════════════════════════════════════════════════╝
```

Un sistema de taxímetro digital desarrollado en Python que simula el funcionamiento de un taxímetro real con diferentes estados y cálculo de tarifas.

## 📋 Descripción

Digital Taximeter es una aplicación de consola que simula el comportamiento de un taxímetro tradicional. El sistema calcula automáticamente las tarifas basándose en el tiempo que el taxi permanece detenido versus el tiempo que está en movimiento, aplicando tarifas diferenciadas para cada estado.

## 🚀 Características

- **Control de viaje**: Iniciar, pausar y finalizar viajes
- **Estados dinámicos**: Alternar entre estado "detenido" y "en movimiento"
- **Cálculo de tarifas**: Sistema de tarifas diferenciadas por estado
- **Resumen de viaje**: Información detallada al finalizar cada viaje
- **Interfaz intuitiva**: Comandos simples y claros
- **Sistema de logging**: Registro automático de actividades para trazabilidad

## 💰 Sistema de Tarifas

- **Tiempo detenido**: €0.02 por segundo
- **Tiempo en movimiento**: €0.05 por segundo

## 🛠️ Instalación

### **Requisitos previos:**
- Python 3.6 o superior

### **Instalación básica:**
1. Clona o descarga este repositorio
2. No se requieren dependencias externas para `main.py`

### **Para usar Jupyter Notebook (opcional):**
```bash
# Instalar Jupyter
pip install jupyter

# Verificar instalación
jupyter --version
```

## 📖 Uso

### 🚕 **Ejecutar versión de producción (main.py):**
```bash
python main.py
```

### 📓 **Ejecutar versión interactiva (Jupyter Notebook):**

#### **Opción 1: VS Code (Recomendado)**
1. Abrir VS Code en el directorio del proyecto
2. Instalar extensión de Python (si no está instalada)
3. Abrir `taximeter.ipynb`
4. Ejecutar celdas con `Shift + Enter`

#### **Opción 2: Jupyter Notebook clásico**
```bash
# Instalar Jupyter (solo la primera vez)
pip install jupyter

# Navegar al directorio del proyecto
cd "ruta/del/proyecto/Digital-Taximeter"

# Iniciar Jupyter Notebook
jupyter notebook

# Se abrirá en el navegador, hacer clic en 'taximeter.ipynb'
```

### Comandos Disponibles

- `start` - Iniciar un nuevo viaje (estado inicial: detenido)
- `stop` - Cambiar el estado a "detenido"
- `move` - Cambiar el estado a "en movimiento"
- `finish` - Finalizar el viaje y mostrar el resumen con la tarifa total
- `exit` - Salir de la aplicación

### Ejemplo de Uso

```
Welcome to Digital Taxi
Available commands:'start', 'stop', 'move', 'finish', 'exit'

> start
Trip started. Initial state: 'stopped'

> move
State changed to 'moving'.

> stop
State changed to 'stopped'.

> finish
Este es el total: 1.25€

--- Trip Summary ---
Stopped time: 15.3 seconds
Moving time: 20.1 seconds
Total fare: €1.31
---------------------
```

## 🏗️ Estructura del Proyecto

```
Digital-Taximeter/
├── main.py                 # 🚕 Programa principal (ejecutable)
├── taximeter.ipynb         # 📓 Versión interactiva en Jupyter
├── logs/                   # 📋 Directorio de archivos de log
│   └── taximeter.log       # 📄 Registro de actividades
├── tests/                  # 🧪 Tests unitarios
│   ├── __init__.py         # 📦 Paquete de tests
│   ├── test_calculate_fare.py  # 🧮 Tests de cálculo de tarifas
│   ├── test_scenarios.py   # 🌟 Tests de escenarios reales
│   └── run_tests.py        # ▶️ Script para ejecutar tests
└── README.md               # 📖 Documentación del proyecto
```

### 📋 **Descripción de archivos:**
- **`main.py`**: Versión de producción, optimizada para ejecutar desde terminal
- **`taximeter.ipynb`**: Versión educativa e interactiva para experimentación
- **`logs/taximeter.log`**: Registro automático de todas las actividades
- **`README.md`**: Documentación completa del proyecto

## 🧪 Testing

Tests unitarios completos usando `unittest` de Python.

### **📂 Estructura de Tests:**

```
tests/
├── __init__.py                    # Paquete de tests
├── test_calculate_fare.py         # Tests de función calculate_fare
├── test_scenarios.py              # Tests de escenarios reales
└── run_tests.py                   # Script para ejecutar todos los tests
```

### **🚀 Ejecutar Tests:**

```bash
# Ejecutar todos los tests
python -m unittest discover tests -v

# Tests específicos por módulo
python -m unittest tests.test_calculate_fare -v
python -m unittest tests.test_scenarios -v

# Ejecutar con script personalizado
python tests/run_tests.py
```

### **📊 Tests Incluidos:**

#### **🧮 Tests Básicos (`test_calculate_fare.py`):**
- ✅ Solo tiempo detenido
- ✅ Solo tiempo en movimiento  
- ✅ Tiempo mixto (combinado)
- ✅ Tiempo cero (caso edge)
- ✅ Números decimales (precisión)
- ✅ Viaje corto (1 segundo)
- ✅ Viaje largo (1 hora)

#### **🌟 Tests de Escenarios (`test_scenarios.py`):**
- ✅ Viaje urbano corto (semáforos y tráfico normal)
- ✅ Viaje por autopista (poco tiempo parado)
- ✅ Tráfico pesado (más tiempo parado que movimiento)
- ✅ Verificación de tarifas correctas
- ✅ Precisión de decimales en cálculos

### **📈 Resultado esperado:**
```
test_solo_tiempo_parado ... ok
test_solo_tiempo_movimiento ... ok
test_tiempo_mixto ... ok
test_tiempo_cero ... ok
test_numeros_decimales ... ok
test_viaje_corto ... ok
test_viaje_largo ... ok
test_viaje_urbano_corto ... ok
test_viaje_autopista ... ok
test_viaje_trafico_pesado ... ok
test_tarifas_correctas ... ok
test_precision_decimales ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.003s

OK
```

### **🎯 Tipos de Tests:**

- **Unitarios**: Funciones individuales (`calculate_fare`)
- **Integración**: Escenarios completos de uso real
- **Validación**: Tarifas y precisión monetaria
- **Edge cases**: Casos límite y situaciones especiales

## 📓 Dual Development Strategy

Este proyecto mantiene **dos versiones sincronizadas**:

### 🚕 **main.py - Versión de Producción**
- **Propósito**: Uso diario, aplicación final
- **Ejecución**: `python main.py`
- **Características**: Optimizado, robusto, completo

### 📓 **taximeter.ipynb - Versión Interactiva**  
- **Propósito**: Experimentación, educación, desarrollo
- **Ejecución**: Jupyter Notebook
- **Características**: Visual, documentado, modular

### ✅ **Ventajas de esta estrategia:**
- **Flexibilidad**: Diferentes herramientas para diferentes necesidades
- **Educación**: Aprender desarrollo iterativo
- **Experimentación**: Probar cambios sin riesgo
- **Presentación**: Demostrar funcionalidades visualmente
- **Backup**: Redundancia de código principal

## �🔧 Funciones Principales

### `calculate_fare(seconds_stopped, seconds_moving)`
Calcula la tarifa total basándose en los segundos detenido y en movimiento.

### `taximeter()`
Función principal que maneja la interfaz de usuario y la lógica del taxímetro.

## 📊 Sistema de Logging

El proyecto incluye un sistema de logging simple para la trazabilidad:

- **Archivo de logs**: `logs/taximeter.log` (creado automáticamente)
- **Formato**: Timestamp + mensaje
- **Ubicación**: Directorio `logs/` dentro del proyecto
- **Salida dual**: Archivo + consola
- **Codificación**: UTF-8 para caracteres especiales

### Eventos Registrados

#### **Logs de Sistema (INFO):**
- Inicio del programa
- Salida de la aplicación

#### **Logs de Viaje (INFO):**
- Inicio de un viaje
- Cambios de estado (stop/move)
- Finalización de viaje con tiempos
- Cálculo de tarifas

#### **Logs de Errores (WARNING):**
- Intento de iniciar viaje con trip activo
- Comandos de estado sin viaje activo
- Intento de finalizar viaje sin trip activo
- Comandos inválidos

**Total: 12 tipos de eventos registrados automáticamente**

## 🎯 Casos de Uso

- **Educativo**: Aprender sobre sistemas de tiempo real y cálculo de tarifas
- **Simulación**: Entender el funcionamiento de un taxímetro
- **Prototipo**: Base para desarrollar sistemas de facturación más complejos

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 🛡️ Manejo de Errores

El sistema incluye validaciones para:
- Intentar usar comandos sin haber iniciado un viaje
- Intentar iniciar un viaje cuando ya hay uno en progreso
- Comandos inválidos con mensajes de ayuda

## 🔮 Futuras Mejoras

- [ ] Interfaz gráfica con tkinter
- [ ] Guardado de historial de viajes
- [ ] Configuración de tarifas personalizables
- [ ] Integración con GPS para detección automática de movimiento
- [ ] Exportación de reportes en CSV/PDF
- [ ] Expansión del sistema de logging para más eventos

---
*Desarrollado con ❤️ en Python*