import time
import logging
import os

# Terminal enhancement libraries
try:
    from colorama import init, Fore, Back, Style
    import colorama
    colorama.init(autoreset=True)
    COLORS_AVAILABLE = True
    print(f"{Fore.GREEN}✓ Terminal colors enabled{Style.RESET_ALL}")
except ImportError:
    COLORS_AVAILABLE = False
    print("⚠ Terminal colors not available. Install with: pip install colorama")

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
        print(f"{Fore.YELLOW}💰 Total: {Fore.GREEN}€{fare}{Style.RESET_ALL}")
    else:
        print(f"💰 Total: €{fare}")
    
    return fare

def display_welcome():
    """Mostrar mensaje de bienvenida con formato mejorado"""
    if RICH_AVAILABLE:
        welcome_text = Text("🚖 Digital Taximeter", style="bold yellow")
        commands_text = Text("Available commands: 'start', 'stop', 'move', 'finish', 'exit'", style="cyan")
        console.print(Panel.fit(welcome_text, subtitle=commands_text))
    elif COLORS_AVAILABLE:
        print(f"\n{Back.YELLOW}{Fore.BLACK} 🚖 Digital Taximeter {Style.RESET_ALL}")
        print(f"{Fore.CYAN}Available commands: 'start', 'stop', 'move', 'finish', 'exit'{Style.RESET_ALL}\n")
    else:
        print("\n🚖 Digital Taximeter")
        print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

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
            command = input(f"{Fore.BLUE}> {Style.RESET_ALL}").strip().lower()
        else:
            command = input("> ").strip().lower()

        if command == 'start':
            if trip_active:
                logging.warning("Intento de iniciar viaje con trip activo")
                if COLORS_AVAILABLE:
                    print(f"{Fore.RED}❌ Error: Trip already in progress.{Style.RESET_ALL}")
                else:
                    print("❌ Error: Trip already in progress.")
                continue
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'
            state_start_time = time.time()
            logging.info("Viaje iniciado")
            if COLORS_AVAILABLE:
                print(f"{Fore.GREEN}✅ Trip started. Initial state: 'stopped'{Style.RESET_ALL}")
            else:
                print("✅ Trip started. Initial state: 'stopped'")

        elif command in ("stop", "move"):
            if not trip_active:
                logging.warning("Comando de estado sin viaje activo")
                if COLORS_AVAILABLE:
                    print(f"{Fore.RED}❌ Error: No active trip. Use 'start' to begin.{Style.RESET_ALL}")
                else:
                    print("❌ Error: No active trip. Use 'start' to begin.")
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
                state_color = Fore.RED if state == 'stopped' else Fore.GREEN
                print(f"{state_color}🚦 State changed to '{state}'.{Style.RESET_ALL}")
            else:
                print(f"🚦 State changed to '{state}'.")

        elif command == 'finish':
            if not trip_active:
                logging.warning("Intento de finalizar viaje sin trip activo")
                if COLORS_AVAILABLE:
                    print(f"{Fore.RED}❌ Error: No active trip to finish.{Style.RESET_ALL}")
                else:
                    print("❌ Error: No active trip to finish.")
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
                print(f"\n{Back.BLUE}{Fore.WHITE} --- Trip Summary --- {Style.RESET_ALL}")
                print(f"{Fore.YELLOW}⏹️  Stopped time: {stopped_time:.1f} seconds{Style.RESET_ALL}")
                print(f"{Fore.GREEN}🚗 Moving time: {moving_time:.1f} seconds{Style.RESET_ALL}")
                print(f"{Fore.CYAN}💰 Total fare: €{total_fare:.2f}{Style.RESET_ALL}")
                print(f"{Back.BLUE}{Fore.WHITE} --------------------- {Style.RESET_ALL}\n")
            else:
                print("\n--- Trip Summary ---")
                print(f"⏹️  Stopped time: {stopped_time:.1f} seconds")
                print(f"🚗 Moving time: {moving_time:.1f} seconds")
                print(f"💰 Total fare: €{total_fare:.2f}")
                print("---------------------\n")

            trip_active = False
            state = None

        elif command == 'exit':
            logging.info("Usuario salió de la aplicación")
            if COLORS_AVAILABLE:
                print(f"{Fore.MAGENTA}👋 Exiting Digital Taxi. Goodbye!{Style.RESET_ALL}")
            else:
                print("👋 Exiting Digital Taxi. Goodbye!")
            break
        else:
            logging.warning(f"Comando inválido recibido: '{command}'")
            if COLORS_AVAILABLE:
                print(f"{Fore.RED}❓ Invalid command. Please use 'start', 'stop', 'move', 'finish', or 'exit'.{Style.RESET_ALL}")
            else:
                print("❓ Invalid command. Please use 'start', 'stop', 'move', 'finish', or 'exit'.")

if __name__ == "__main__":
    logging.info("Iniciando Digital Taximeter")
    taximeter()