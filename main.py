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

def display_welcome():
    """Mostrar mensaje de bienvenida con formato mejorado y tabla de comandos en español"""
    if RICH_AVAILABLE:
        from rich.table import Table
        
        # Header
        welcome_text = Text("🚖 Taxímetro Digital Profesional 🚕", style="bold yellow")
        console.print(Panel.fit(welcome_text, title="¡Bienvenido!"))
        
        # Commands table
        table = Table(title="📋 Comandos Disponibles", show_header=True, header_style="bold cyan")
        table.add_column("Comando", style="green", width=12)
        table.add_column("Descripción", style="white")
        table.add_column("Uso", style="yellow")
        
        table.add_row("🚀 start", "Iniciar un nuevo viaje", "Escribe: start")
        table.add_row("🛑 stop", "Poner taxi en estado parado", "Escribe: stop")
        table.add_row("🏃 move", "Poner taxi en movimiento", "Escribe: move")
        table.add_row("🏁 finish", "Terminar viaje y calcular tarifa", "Escribe: finish")
        table.add_row("❓ help", "Mostrar esta tabla de comandos", "Escribe: help")
        table.add_row("🚪 exit", "Salir de la aplicación", "Escribe: exit")
        
        console.print(table)
        console.print("\n[bold cyan]💡 Consejo:[/] Alterna entre 'stop' y 'move' durante tu viaje, luego usa 'finish' para obtener la tarifa total.")
        
    elif COLORS_AVAILABLE:
        print(f"\n{Back.YELLOW}{Fore.BLACK} 🚖 TAXÍMETRO DIGITAL PROFESIONAL 🚕 {Style.RESET_ALL}")
        print(f"{Back.CYAN}{Fore.WHITE} 📋 TABLA DE COMANDOS {Style.RESET_ALL}")
        print("╭──────────────────────────────────────────────────────────╮")
        print("│ Comando  │ Descripción                  │ Uso           │")
        print("├──────────────────────────────────────────────────────────┤")
        print(f"│ {Fore.GREEN}🚀 start{Style.RESET_ALL}  │ Iniciar un nuevo viaje       │ Escribe: start│")
        print(f"│ {Fore.RED}🛑 stop{Style.RESET_ALL}   │ Poner taxi en estado parado  │ Escribe: stop │")
        print(f"│ {Fore.GREEN}🏃 move{Style.RESET_ALL}   │ Poner taxi en movimiento     │ Escribe: move │")
        print(f"│ {Fore.CYAN}🏁 finish{Style.RESET_ALL} │ Terminar viaje y calc tarifa │ Escribe: finish│")
        print(f"│ {Fore.YELLOW}❓ help{Style.RESET_ALL}   │ Mostrar esta tabla           │ Escribe: help │")
        print(f"│ {Fore.MAGENTA}🚪 exit{Style.RESET_ALL}   │ Salir de la aplicación       │ Escribe: exit │")
        print("╰──────────────────────────────────────────────────────────╯")
        print(f"{Fore.CYAN}💡 Consejo: Alterna entre 'stop' y 'move' durante tu viaje, luego 'finish'{Style.RESET_ALL}\n")
    else:
        print("\n🚖 TAXÍMETRO DIGITAL PROFESIONAL 🚕")
        print("=" * 60)
        print("📋 TABLA DE COMANDOS")
        print("=" * 60)
        print("| Comando  | Descripción                  | Uso           |")
        print("|----------|------------------------------|---------------|")
        print("| 🚀 start  | Iniciar un nuevo viaje       | Escribe: start|")
        print("| 🛑 stop   | Poner taxi en estado parado  | Escribe: stop |")
        print("| 🏃 move   | Poner taxi en movimiento     | Escribe: move |")
        print("| 🏁 finish | Terminar viaje y calc tarifa | Escribe: finish|")
        print("| ❓ help   | Mostrar esta tabla           | Escribe: help |")
        print("| 🚪 exit   | Salir de la aplicación       | Escribe: exit |")
        print("=" * 60)
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
        if COLORS_AVAILABLE:
            command = input(f"{Fore.BLUE}🚖 > {Style.RESET_ALL}").strip().lower()
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
        else:
            logging.warning(f"Comando inválido recibido: '{command}'")
            if COLORS_AVAILABLE:
                print(f"{Fore.RED}❓ Comando inválido. Usa 'start', 'stop', 'move', 'finish', 'help', o 'exit'.{Style.RESET_ALL}")
            else:
                print("❓ Comando inválido. Usa 'start', 'stop', 'move', 'finish', 'help', o 'exit'.")

if __name__ == "__main__":
    logging.info("🚀 Iniciando Taxímetro Digital")
    taximeter()