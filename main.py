# -*- coding: utf-8 -*-
import time
import logging
import os
import sys

# Set UTF-8 encoding for Windows compatibility
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Terminal enhancement libraries
try:
    from colorama import init, Fore, Back, Style
    import colorama
    colorama.init(autoreset=True)
    COLORS_AVAILABLE = True
    print(f"{Fore.GREEN}✓ Colores de terminal activados 🎨{Style.RESET_ALL}")
except ImportError:
    COLORS_AVAILABLE = False
    print("⚠ Colores no disponibles. Instala con: pip install colorama")

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    console = None

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Configuración de logging mejorada
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/taximeter.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def calculate_fare(seconds_stopped, seconds_moving):
    """
    Función para calcular la tarifa total en euros
    stopped: 0.02€/s
    moving: 0.05€/s
    """
    logging.info(f"Calculando tarifa: parado={seconds_stopped:.1f}s, movimiento={seconds_moving:.1f}s")
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    # Redondear a 2 decimales para evitar problemas de precisión con dinero
    fare = round(fare, 2)
    
    if COLORS_AVAILABLE:
        print(f"{Fore.YELLOW}💰 Total calculado: {Fore.GREEN}€{fare} 🎯{Style.RESET_ALL}")
    else:
        print(f"💰 Total calculado: €{fare} 🎯")
    
    return fare

def save_trip_to_history(stopped_time, moving_time, total_fare):
    """Guardar viaje en historial de forma simple"""
    try:
        from datetime import datetime
        
        # Crear línea del historial
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        duration_total = stopped_time + moving_time
        
        trip_line = f"{now} | Parado: {stopped_time:.1f}s | Movimiento: {moving_time:.1f}s | Total: {duration_total:.1f}s | Tarifa: €{total_fare:.2f}\n"
        
        # Guardar en archivo
        with open('logs/historial_viajes.txt', 'a', encoding='utf-8') as f:
            f.write(trip_line)
            
    except Exception as e:
        logging.warning(f"Error guardando historial: {e}")

def show_trip_history():
    """Mostrar últimos 5 viajes del historial con diseño simple y colorido"""
    try:
        if not os.path.exists('logs/historial_viajes.txt'):
            if COLORS_AVAILABLE:
                print(f"\n{Back.YELLOW}{Fore.BLACK} 📭 HISTORIAL VACÍO 📭 {Style.RESET_ALL}")
                print(f"{Fore.CYAN}No hay viajes registrados aún.{Style.RESET_ALL}")
                print(f"{Fore.GREEN}💡 Realiza tu primer viaje con: {Fore.YELLOW}start{Style.RESET_ALL}\n")
            else:
                print("📭 No hay viajes en el historial aún.")
            return
            
        with open('logs/historial_viajes.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            if COLORS_AVAILABLE:
                print(f"\n{Back.YELLOW}{Fore.BLACK} 📭 HISTORIAL VACÍO 📭 {Style.RESET_ALL}")
                print(f"{Fore.CYAN}No hay viajes registrados aún.{Style.RESET_ALL}")
                print(f"{Fore.GREEN}💡 Realiza tu primer viaje con: {Fore.YELLOW}start{Style.RESET_ALL}\n")
            else:
                print("📭 No hay viajes en el historial aún.")
            return
            
        # Mostrar últimos 5 viajes con diseño simple
        recent_trips = lines[-5:]
        
        if COLORS_AVAILABLE:
            print(f"\n{Back.BLUE}{Fore.WHITE} 📜 HISTORIAL DE VIAJES (últimos {len(recent_trips)}) 📜 {Style.RESET_ALL}\n")
            
            for i, trip in enumerate(recent_trips, 1):
                # Parsear la línea del viaje para extraer información
                parts = trip.strip().split(' | ')
                if len(parts) >= 5:
                    date_time = parts[0]
                    stopped_info = parts[1]
                    moving_info = parts[2] 
                    total_info = parts[3]
                    fare_info = parts[4]
                    
                    # Alternar colores por viaje
                    if i % 2 == 1:
                        number_color = Fore.GREEN
                        highlight_color = Fore.WHITE
                    else:
                        number_color = Fore.YELLOW
                        highlight_color = Fore.CYAN
                    
                    print(f"{number_color}#{i:2} {Fore.MAGENTA}📅 {highlight_color}{date_time}{Style.RESET_ALL}")
                    print(f"    {Fore.RED}🛑 {highlight_color}{stopped_info}{Style.RESET_ALL}  {Fore.GREEN}🏃 {highlight_color}{moving_info}{Style.RESET_ALL}")
                    print(f"    {Fore.BLUE}⏱️  {highlight_color}{total_info}{Style.RESET_ALL}  {Fore.YELLOW}💰 {highlight_color}{fare_info}{Style.RESET_ALL}")
                    if i < len(recent_trips):
                        print(f"{Fore.CYAN}    ─────────────────────────────────────────{Style.RESET_ALL}")
                else:
                    # Fallback para formato simple
                    if i % 2 == 1:
                        color = Fore.GREEN
                    else:
                        color = Fore.CYAN
                    print(f"{color}#{i}: {trip.strip()}{Style.RESET_ALL}")
                    if i < len(recent_trips):
                        print(f"{Fore.CYAN}    ─────────────────────────────────────────{Style.RESET_ALL}")
            
            print(f"\n{Fore.GREEN}💼 Total de viajes registrados: {len(lines)}{Style.RESET_ALL}\n")
        else:
            print("\n📜 HISTORIAL DE VIAJES (últimos 5):")
            for i, trip in enumerate(recent_trips, 1):
                print(f"{i}. {trip.strip()}")
        print()
        
    except Exception as e:
        logging.warning(f"Error leyendo historial: {e}")
        if COLORS_AVAILABLE:
            print(f"{Fore.RED}❌ Error leyendo historial.{Style.RESET_ALL}")
        else:
            print("❌ Error leyendo historial.")

def display_welcome():
    """Mostrar mensaje de bienvenida con formato mejorado y tabla de comandos en español"""
    # Forzar el uso de la tabla azul con líneas continuas
    if COLORS_AVAILABLE:
        # Animación del taxi moviéndose
        print(f"\n{Fore.YELLOW}🚕 Cargando Taxímetro Digital...{Style.RESET_ALL}")
        time.sleep(0.3)
        for i in range(20):
            print(f"\r{' ' * i}🚖💨", end='', flush=True)
            time.sleep(0.1)
        print(f"\r{' ' * 20}¡Listo! ✨")
        time.sleep(0.5)
        
        print(f"\n{Back.YELLOW}{Fore.BLACK} 🚖 TAXÍMETRO DIGITAL PROFESIONAL 🚕 {Style.RESET_ALL}")
        print(f"{Back.CYAN}{Fore.WHITE} 📋 COMANDOS DISPONIBLES {Style.RESET_ALL}\n")
        
        # Diseño visual sin tabla - lista con colores y separadores
        print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}                    COMANDOS DEL TAXÍMETRO{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}\n")
        
        print(f"  {Fore.GREEN}🚀 start{Style.RESET_ALL}    {Fore.CYAN}→{Style.RESET_ALL} Iniciar un nuevo viaje")
        print(f"  {Fore.RED}🛑 stop{Style.RESET_ALL}     {Fore.CYAN}→{Style.RESET_ALL} Poner taxi en estado parado") 
        print(f"  {Fore.GREEN}🏃 move{Style.RESET_ALL}     {Fore.CYAN}→{Style.RESET_ALL} Taxi en movimiento")
        print(f"  {Fore.BLUE}🏁 finish{Style.RESET_ALL}   {Fore.CYAN}→{Style.RESET_ALL} Finalizar viaje y calcular tarifa")
        print(f"  {Fore.MAGENTA}📜 history{Style.RESET_ALL}  {Fore.CYAN}→{Style.RESET_ALL} Ver historial de viajes")
        print(f"  {Fore.YELLOW}❓ help{Style.RESET_ALL}     {Fore.CYAN}→{Style.RESET_ALL} Mostrar esta lista de comandos")
        print(f"  {Fore.MAGENTA}🚪 exit{Style.RESET_ALL}     {Fore.CYAN}→{Style.RESET_ALL} Salir de la aplicación")
        
        print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
        print(f"\n{Back.CYAN}{Fore.WHITE} 💡 Consejo: Usa 'start' → 'stop'/'move' → 'finish' {Style.RESET_ALL}\n")
    else:
        print("\n" + "="*65)
        print("🚖 TAXÍMETRO DIGITAL PROFESIONAL 🚕".center(65))
        print("="*65)
        print("📋 TABLA DE COMANDOS".center(65))
        print("="*65)
        print("| Comando  | Descripción                    | Uso           |")
        print("|----------|--------------------------------|---------------|")
        print("| 🚀 start  | Iniciar un nuevo viaje         | start         |")
        print("| 🛑 stop   | Poner taxi en estado parado    | stop          |")
        print("| 🏃 move   | Poner taxi en movimiento       | move          |")
        print("| 🏁 finish | Terminar viaje y calc tarifa   | finish        |")
        print("| 📜 history| Ver historial de viajes        | history       |")
        print("| ❓ help   | Mostrar esta tabla de comandos | help          |")
        print("| 🚪 exit   | Salir de la aplicación         | exit          |")
        print("="*65)
        print("💡 Consejo: Alterna entre 'stop' y 'move' durante tu viaje, luego 'finish'\n")

def taximeter():
    """
    Función principal del taxímetro: manejar y mostrar opciones.
    """
    display_welcome()
    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        # Mostrar prompt dinámico con estado del taxi
        if COLORS_AVAILABLE:
            if trip_active:
                if state == 'stopped':
                    command = input(f"{Fore.BLUE}🚖{Style.RESET_ALL} {Fore.RED}🛑 PARADO{Style.RESET_ALL} {Fore.BLUE}> {Style.RESET_ALL}").strip().lower()
                else:
                    command = input(f"{Fore.BLUE}🚖{Style.RESET_ALL} {Fore.GREEN}🏃💨 EN MOVIMIENTO{Style.RESET_ALL} {Fore.BLUE}> {Style.RESET_ALL}").strip().lower()
            else:
                command = input(f"{Fore.BLUE}🚖 > {Style.RESET_ALL}").strip().lower()
        else:
            if trip_active:
                if state == 'stopped':
                    command = input("🚖 🛑 PARADO > ").strip().lower()
                else:
                    command = input("🚖 🏃💨 EN MOVIMIENTO > ").strip().lower()
            else:
                command = input("🚖 > ").strip().lower()

        if command == 'start':
            if trip_active:
                logging.warning("Intento de iniciar viaje con trip activo")
                if COLORS_AVAILABLE:
                    print(f"{Fore.RED}❌ Error: Ya hay un viaje en progreso.{Style.RESET_ALL}")
                else:
                    print("❌ Error: Ya hay un viaje en progreso.")
                continue
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'
            state_start_time = time.time()
            logging.info("Viaje iniciado")
            if COLORS_AVAILABLE:
                print(f"{Fore.GREEN}✅ ¡Viaje iniciado! Estado inicial: 'parado' 🛑{Style.RESET_ALL}")
            else:
                print("✅ ¡Viaje iniciado! Estado inicial: 'parado' 🛑")

        elif command in ("stop", "move"):
            if not trip_active:
                logging.warning("Comando de estado sin viaje activo")
                if COLORS_AVAILABLE:
                    print(f"{Fore.RED}❌ Error: No hay viaje activo. Usa 'start' para comenzar.{Style.RESET_ALL}")
                else:
                    print("❌ Error: No hay viaje activo. Usa 'start' para comenzar.")
                continue
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            state = "stopped" if command == "stop" else "moving"
            state_start_time = time.time()
            logging.info(f"Estado cambiado a: {state}")
            
            if COLORS_AVAILABLE:
                if state == 'stopped':
                    print(f"{Fore.RED}🛑 Estado cambiado a: 'parado'{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}🏃 Estado cambiado a: 'en movimiento'{Style.RESET_ALL}")
            else:
                if state == 'stopped':
                    print("� Estado cambiado a: 'parado'")
                else:
                    print("🏃 Estado cambiado a: 'en movimiento'")

        elif command == 'finish':
            if not trip_active:
                logging.warning("Intento de finalizar viaje sin trip activo")
                if COLORS_AVAILABLE:
                    print(f"{Fore.RED}❌ Error: No hay viaje activo para terminar.{Style.RESET_ALL}")
                else:
                    print("❌ Error: No hay viaje activo para terminar.")
                continue
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            total_fare = calculate_fare(stopped_time, moving_time)
            logging.info(f"Viaje finalizado - Tiempo parado: {stopped_time:.1f}s, Tiempo movimiento: {moving_time:.1f}s")
            logging.info(f"Tarifa total calculada: €{total_fare:.2f}")
            
            # Guardar en historial
            save_trip_to_history(stopped_time, moving_time, total_fare)
            
            if COLORS_AVAILABLE:
                print(f"\n{Back.BLUE}{Fore.WHITE} 🧾 --- RESUMEN DEL VIAJE --- 🧾 {Style.RESET_ALL}")
                print(f"{Fore.YELLOW}🛑 Tiempo parado: {stopped_time:.1f} segundos{Style.RESET_ALL}")
                print(f"{Fore.GREEN}🏃 Tiempo en movimiento: {moving_time:.1f} segundos{Style.RESET_ALL}")
                print(f"{Fore.CYAN}💰 Tarifa total: €{total_fare:.2f}{Style.RESET_ALL}")
                print(f"{Back.BLUE}{Fore.WHITE} 🎯 -------------------------- 🎯 {Style.RESET_ALL}\n")
            else:
                print("\n🧾 --- RESUMEN DEL VIAJE ---")
                print(f"🛑 Tiempo parado: {stopped_time:.1f} segundos")
                print(f"🏃 Tiempo en movimiento: {moving_time:.1f} segundos")
                print(f"💰 Tarifa total: €{total_fare:.2f}")
                print("🎯 --------------------------\n")

            trip_active = False
            state = None

        elif command == 'exit':
            logging.info("Usuario salió de la aplicación")
            if COLORS_AVAILABLE:
                print(f"{Fore.MAGENTA}👋 ¡Saliendo del Taxímetro Digital! ¡Hasta luego! 🚖✨{Style.RESET_ALL}")
            else:
                print("👋 ¡Saliendo del Taxímetro Digital! ¡Hasta luego! 🚖✨")
            break
        elif command in ['help', 'h', '?']:
            display_welcome()
        elif command in ['history', 'hist']:
            show_trip_history()
        else:
            logging.warning(f"Comando inválido recibido: '{command}'")
            if COLORS_AVAILABLE:
                print(f"{Fore.RED}❓ Comando inválido. Usa 'start', 'stop', 'move', 'finish', 'history', 'help', o 'exit'.{Style.RESET_ALL}")
            else:
                print("❓ Comando inválido. Usa 'start', 'stop', 'move', 'finish', 'history', 'help', o 'exit'.")

if __name__ == "__main__":
    logging.info("🚀 Iniciando Taxímetro Digital")
    taximeter()