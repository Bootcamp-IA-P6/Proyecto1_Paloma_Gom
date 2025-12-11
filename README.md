# Digital Taximeter 🚕

```
╔══════════════════════════════════════════════════════════════╗
║                    DIGITAL TAXIMETER                         ║
║                  Sistema de Taxímetro Digital                ║
║                         🚕 v2.0 🚕                          ║
╚══════════════════════════════════════════════════════════════╝
```

Un sistema de taxímetro digital profesional desarrollado en Python que simula el funcionamiento de un taxímetro real con diferentes estados, múltiples perfiles de tarifas, historial de viajes y una interfaz visual mejorada.

## 📋 Descripción

Digital Taximeter es una aplicación de consola que simula el comportamiento de un taxímetro tradicional. El sistema calcula automáticamente las tarifas basándose en el tiempo que el taxi permanece detenido versus el tiempo que está en movimiento, aplicando tarifas diferenciadas para cada estado.

## 🚀 Características

### 🚕 **Funcionalidades Principal del Taxímetro:**
- **Control de viaje**: Iniciar, pausar y finalizar viajes
- **Estados dinámicos**: Alternar entre estado "detenido" y "en movimiento"
- **Cálculo de tarifas**: Sistema de tarifas diferenciadas por estado
- **Resumen de viaje**: Información detallada al finalizar cada viaje
- **Interfaz intuitiva**: Comandos simples y claros

### 🎨 **Experiencia Visual Mejorada:**
- **Interfaz colorida**: Terminal con colores dinámicos usando `colorama`
- **Animación de bienvenida**: Taxi moviéndose al iniciar la aplicación
- **Prompts dinámicos**: El prompt cambia según el estado del taxi (parado/movimiento)
- **Tablas visuales**: Comandos organizados en diseños atractivos
- **Emojis y símbolos**: Interfaz moderna y visual

### 💰 **Sistema de Tarifas Dinámicas:**
- **Múltiples perfiles**: 5 perfiles de tarifas diferentes
- **Cambio en tiempo real**: Cambiar tarifas durante la operación
- **Comando `precios`**: Ver y cambiar perfiles fácilmente
- **Adaptación situacional**: Tarifas para diferentes escenarios

### 📜 **Historial y Registro:**
- **Historial de viajes**: Guarda automáticamente todos los viajes
- **Comando `history`**: Ver últimos 5 viajes con diseño colorido
- **Sistema de logging**: Registro automático de actividades para trazabilidad
- **Persistencia de datos**: Los viajes se guardan en archivos de texto

### 🔧 **Características Técnicas:**
- **Compatibilidad multiplataforma**: Windows, Linux, macOS
- **Codificación UTF-8**: Soporte completo para caracteres especiales
- **Manejo de errores**: Validaciones robustas y mensajes claros
- **Suite de tests**: 12 tests unitarios completos

## 💰 Sistema de Tarifas Dinámicas

El sistema incluye **5 perfiles de tarifas** diferentes para adaptarse a distintas situaciones:

### 📋 **Perfiles Disponibles:**

| Perfil | Descripción | Parado (€/s) | Movimiento (€/s) | Comando |
|--------|-------------|--------------|------------------|---------|
| 🟢 **Normal** | Condiciones normales de tráfico | €0.02 | €0.05 | `normal` |
| 🔴 **Alta** | Zona concurrida / Alta demanda | €0.03 | €0.08 | `alta` |
| 🌙 **Nocturna** | Tarifa nocturna (22:00-06:00) | €0.025 | €0.06 | `nocturna` |
| ✈️ **Aeropuerto** | Aeropuerto / Estaciones | €0.04 | €0.10 | `aeropuerto` |
| 🎉 **Festivo** | Días festivos / Fin de semana | €0.035 | €0.09 | `festivo` |

### 🔄 **Cambio de Tarifas:**
```bash
# Ver todas las tarifas disponibles
🚖 > precios

# Cambiar directamente a una tarifa
🚖 > alta
🚖 > nocturna
🚖 > aeropuerto
```

### ✨ **Características del Sistema:**
- **Cambio en tiempo real**: Puedes cambiar tarifas durante un viaje
- **Persistencia**: El perfil seleccionado se mantiene entre viajes
- **Visual**: Interfaz colorida para mostrar todas las opciones
- **Validación**: Verificación automática de comandos válidos

## 🛠️ Instalación

### **Requisitos previos:**
- Python 3.6 o superior

### **Instalación básica:**
```bash
# Clonar o descargar el repositorio
git clone https://github.com/Pal-cloud/Digital-Taximeter.git
cd Digital-Taximeter

# Instalar dependencias (recomendado)
pip install -r requirements.txt

# O ejecutar sin dependencias (funcionalidad básica)
python main.py
```

### **Dependencias incluidas:**
- **`colorama`** - Colores en terminal (multiplataforma)
- **`rich`** - Terminal rica con formato avanzado  
- **`pytest`** - Framework de testing moderno (opcional)
- **`pytest-cov`** - Reportes de cobertura (opcional)

### **Para usar Jupyter Notebook (opcional):**
```bash
# Instalar Jupyter
pip install jupyter

# Verificar instalación
jupyter --version
```

## 📖 Uso

### 🚕 **Ejecutar versión de producción:**
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

### 🚕 **Comandos Principales:**
- `start` - Iniciar un nuevo viaje (estado inicial: detenido)
- `stop` - Cambiar el estado a "detenido"
- `move` - Cambiar el estado a "en movimiento"
- `finish` - Finalizar el viaje y mostrar el resumen con la tarifa total
- `exit` - Salir de la aplicación

### 📋 **Comandos de Información:**
- `help` - Mostrar la lista completa de comandos
- `history` - Ver historial de los últimos 5 viajes
- `precios` - Ver y cambiar perfiles de tarifas

### 💰 **Comandos de Tarifas:**
- `normal` - Cambiar a tarifa normal
- `alta` - Cambiar a tarifa de demanda alta
- `nocturna` - Cambiar a tarifa nocturna
- `aeropuerto` - Cambiar a tarifa de aeropuerto
- `festivo` - Cambiar a tarifa de día festivo

### 🎨 **Experiencia Visual:**
La aplicación incluye una interfaz completamente colorida con:
- 🚖 **Animación de bienvenida**: Taxi moviéndose al iniciar
- 🚕 **Animación de despedida**: Taxi alejándose al salir
- 🎨 **Prompts dinámicos**: El símbolo cambia según el estado
- 📋 **Tablas organizadas**: Comandos en diseños visuales atractivos
- 🌈 **Colores dinámicos**: Diferentes colores para cada tipo de información

### Ejemplo de Uso

```
🚕 Cargando Taxímetro Digital...
🚖💨🚖💨🚖💨🚖💨🚖💨🚖💨¡Listo! ✨

 🚖 TAXÍMETRO DIGITAL PROFESIONAL 🚕 
 📋 COMANDOS DISPONIBLES 

============================================================
                    COMANDOS DEL TAXÍMETRO
============================================================

  🚀 start    → Iniciar un nuevo viaje
  🛑 stop     → Poner taxi en estado parado
  🏃 move     → Taxi en movimiento
  🏁 finish   → Finalizar viaje y calcular tarifa
  📜 history  → Ver historial de viajes
  💰 precios  → Ver y cambiar tarifas
  ❓ help     → Mostrar esta lista de comandos
  🚪 exit     → Salir de la aplicación

============================================================

 💡 Consejo: Usa 'start' → 'stop'/'move' → 'finish' 

🚖 > start
✅ ¡Viaje iniciado! Estado inicial: 'parado' 🛑

🚖 🛑 PARADO > move
🏃 Estado cambiado a: 'en movimiento'

🚖 🏃💨 EN MOVIMIENTO > stop
🛑 Estado cambiado a: 'parado'

🚖 🛑 PARADO > precios

 💰 PERFILES DE TARIFAS DISPONIBLES 💰 

➤ Normal           (ACTIVO)
  Comando: normal     🛑 €0.02/s  🏃 €0.05/s

  Demanda Alta   
  Comando: alta       🛑 €0.03/s  🏃 €0.08/s

💡 Para cambiar: escribe el comando del perfil (ej: 'alta', 'nocturna')

🚖 🛑 PARADO > alta

 💼 PERFIL CAMBIADO 💼 
✅ Nuevo perfil: Demanda Alta
🛑 Tarifa parado: €0.03/segundo
🏃 Tarifa movimiento: €0.08/segundo

🚖 🛑 PARADO > finish

💰 Total calculado: €2.45 🎯
📊 Perfil activo: Demanda Alta

 🧾 --- RESUMEN DEL VIAJE --- 🧾 
🛑 Tiempo parado: 15.3 segundos
🏃 Tiempo en movimiento: 20.1 segundos
💰 Tarifa total: €2.45
 🎯 -------------------------- 🎯 

🚖 > history

 📜 HISTORIAL DE VIAJES (últimos 1) 📜 

# 1 📅 2025-12-11 12:45:30
    🛑 Parado: 15.3s  🏃 Movimiento: 20.1s
    ⏱️  Total: 35.4s  💰 Tarifa: €2.45

💼 Total de viajes registrados: 1
```

## 🏗️ Estructura del Proyecto

```
Digital-Taximeter/
├── main.py                 # 🚕 Programa principal (optimizado v2.0)
├── taximeter.ipynb         # 📓 Versión interactiva en Jupyter
├── requirements.txt        # 📦 Dependencias del proyecto
├── pytest.ini             # ⚙️ Configuración de pytest
├── logs/                   # 📋 Directorio de archivos de log
│   ├── taximeter.log       # 📄 Registro de actividades
│   └── historial_viajes.txt # 📜 Historial de viajes completados
├── tests/                  # 🧪 Tests unitarios (12 tests)
│   ├── __init__.py         # 📦 Paquete de tests
│   ├── test_calculate_fare.py  # 🧮 Tests de cálculo de tarifas
│   ├── test_scenarios.py   # 🌟 Tests de escenarios reales
│   └── run_tests.py        # ▶️ Script para ejecutar tests
└── README.md               # 📖 Documentación completa
```

### 📋 **Descripción de archivos:**
- **`main.py`**: Versión de producción v2.0 con interfaz colorida, tarifas dinámicas e historial
- **`taximeter.ipynb`**: Versión educativa e interactiva para experimentación
- **`logs/taximeter.log`**: Registro automático de todas las actividades del sistema
- **`logs/historial_viajes.txt`**: Historial persistente de todos los viajes completados
- **`README.md`**: Documentación completa con todas las nuevas características

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
# Opción 1: unittest (estándar)
python -m unittest discover tests -v

# Opción 2: pytest (mejorado, recomendado)
pytest tests/ -v

# Con coverage report
pytest tests/ --cov=main --cov-report=html

# Tests específicos
python -m unittest tests.test_calculate_fare -v
pytest tests/test_calculate_fare.py -v

# Script personalizado
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

### 🎓 **Educativo:**
- Aprender sobre sistemas de tiempo real y cálculo de tarifas
- Entender programación orientada a eventos
- Estudiar manejo de archivos y persistencia de datos
- Practicar testing unitario y desarrollo basado en pruebas

### 🚕 **Simulación:**
- Simular el funcionamiento real de un taxímetro
- Probar diferentes escenarios de tráfico y tarifas
- Entrenar operadores de taxi con diferentes perfiles de tarifa
- Analizar costos de viajes en diferentes horarios y zonas

### 🔧 **Prototipo:**
- Base para desarrollar sistemas de facturación más complejos
- Framework para aplicaciones de transporte
- Plantilla para sistemas de medición de tiempo
- Fundación para aplicaciones móviles de taxi

## 📈 Novedades v2.0

### 🆕 **Características Nuevas:**

#### 🎨 **Interfaz Visual Completamente Rediseñada:**
- **Animación de bienvenida** con taxi moviéndose
- **Animación de despedida** con taxi alejándose al salir
- **Colores dinámicos** en toda la interfaz usando `colorama`
- **Prompts inteligentes** que cambian según el estado del taxi
- **Tablas visuales** organizadas y atractivas
- **Emojis y símbolos** para una experiencia moderna

#### 💰 **Sistema de Tarifas Dinámicas:**
- **5 perfiles de tarifas** diferentes (Normal, Alta, Nocturna, Aeropuerto, Festivo)
- **Comando `precios`** para ver y cambiar tarifas fácilmente
- **Cambio en tiempo real** durante los viajes
- **Visualización colorida** de todas las opciones disponibles

#### 📜 **Historial de Viajes Completo:**
- **Guardado automático** de todos los viajes en `logs/historial_viajes.txt`
- **Comando `history`** para ver los últimos 5 viajes
- **Formato visual colorido** con separadores y emojis
- **Persistencia de datos** entre sesiones

#### 🔧 **Mejoras Técnicas:**
- **Compatibilidad mejorada** con Windows (UTF-8)
- **Manejo robusto de errores** con validaciones
- **Logging expandido** con más eventos registrados
- **Código optimizado** y mejor estructurado

### 🏆 **Beneficios de la v2.0:**
- ✨ **Experiencia de usuario profesional** con interfaz colorida
- 🎯 **Flexibilidad operativa** con múltiples perfiles de tarifas
- 📊 **Trazabilidad completa** con historial y logs detallados
- 🛡️ **Mayor robustez** con mejor manejo de errores
- 🚀 **Facilidad de uso** con comandos intuitivos

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

### ✅ **Completado en v2.0:**
- [x] ~~Configuración de tarifas personalizables~~ → **5 perfiles implementados**
- [x] ~~Guardado de historial de viajes~~ → **Sistema completo con comando `history`**
- [x] ~~Expansión del sistema de logging~~ → **Logging completo de eventos**
- [x] ~~Interfaz visual mejorada~~ → **Colores, animaciones y diseño profesional**

### 🚀 **Próximas funcionalidades:**
- [ ] Interfaz gráfica con tkinter o PyQt
- [ ] Integración con GPS para detección automática de movimiento
- [ ] Exportación de reportes en CSV/PDF
- [ ] Base de datos SQLite para historial avanzado
- [ ] API REST para integración con otras aplicaciones
- [ ] Sistema de usuarios y autenticación
- [ ] Dashboard web con métricas y estadísticas
- [ ] Integración con servicios de mapas (Google Maps API)
- [ ] Notificaciones push y alertas
- [ ] Sistema de facturación automática

---
*Desarrollado con ❤️ en Python*