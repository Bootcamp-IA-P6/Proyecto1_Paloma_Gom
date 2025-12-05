import time
import logging
import os
import sys

# Intentar importar librerías de terminal mejorado (opcional)
try:
    from colorama import init, Fore, Back, Style
    import colorama
    colorama.init()  # Para Windows
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False

# Configuración simple de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/taximeter.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# ASCII Art para el taxi
TAXI_FRAMES = [
    "    🚕💨     ",
    "   🚕💨      ",
    "  🚕💨       ",
    " 🚕💨        ",
    "🚕💨         ",
    " 🚕💨        ",
    "  🚕💨       ",
    "   🚕💨      "
]

TAXI_LOGO = """
╔════════════════════════════════════════════╗
║           🚕 DIGITAL TAXIMETER 🚕           ║
║                                            ║
║    Professional Fare Calculation System    ║
╚════════════════════════════════════════════╝
"""

HELP_MENU = """
📋 Available Commands:
┌─────────────────────────────────────────┐
│ 🚀 start   │ Begin a new trip           │
│ 🛑 stop    │ Set taxi to stopped state  │
│ 🚗 move    │ Set taxi to moving state   │
│ 🏁 finish  │ Complete trip & calculate  │
│ 🚪 exit    │ Exit the application       │
└─────────────────────────────────────────┘
"""

def print_colored(message, color=None, style=None, end='\n'):
    """Imprimir con colores si está disponible, sino texto normal."""
    if COLORS_AVAILABLE and color:
        color_code = getattr(Fore, color.upper(), '')
        style_code = getattr(Style, style.upper(), '') if style else ''
        reset = Style.RESET_ALL
        print(f"{style_code}{color_code}{message}{reset}", end=end)
    else:
        print(message, end=end)

def clear_screen():
    """Limpiar la pantalla de manera compatible."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_taxi():
    """Mostrar una pequeña animación del taxi en movimiento."""
    if not COLORS_AVAILABLE:
        print("🚕 Starting Digital Taximeter...")
        time.sleep(1)
        return
    
    print_colored("\n🚀 Starting Digital Taximeter...\n", "cyan", "bright")
    for i in range(2):  # 2 ciclos de animación
        for frame in TAXI_FRAMES:
            print(f"\r{frame}", end="", flush=True)
            time.sleep(0.15)
    print("\r" + " " * 20)  # Limpiar la línea

def show_welcome():
    """Mostrar la pantalla de bienvenida."""
    clear_screen()
    print_colored(TAXI_LOGO, "cyan", "bright")
    animate_taxi()
    print_colored(HELP_MENU, "yellow")
    print_colored("💡 Tip: Type 'help' anytime to see this menu again!", "green")
    print()

def show_status(trip_active, state, stopped_time, moving_time):
    """Mostrar el estado actual del viaje."""
    if trip_active:
        status_color = "green" if state == "moving" else "yellow"
        status_emoji = "🚗" if state == "moving" else "🛑"
        print_colored(f"\n📊 Current Status: {status_emoji} {state.upper()}", status_color, "bright")
        print(f"⏱️  Time stopped: {stopped_time:.1f}s | Time moving: {moving_time:.1f}s")
        estimated_fare = stopped_time * 0.02 + moving_time * 0.05
        print_colored(f"💰 Estimated fare: €{estimated_fare:.2f}", "magenta")
        print()
    else:
        print_colored("\n📍 Status: No active trip", "red")
        print_colored("💡 Use 'start' to begin a new trip", "yellow")
        print()

def calculate_fare(seconds_stopped, seconds_moving):
    """
    Funcion para calcular la tarifa total en euros
    stopped: 0.02€/s
    moving: 0.05€/s
    """
    logging.info(f"Calculando tarifa: parado={seconds_stopped:.1f}s, movimiento={seconds_moving:.1f}s")
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    # Redondear a 2 decimales para evitar problemas de precisión con dinero
    fare = round(fare, 2)
    print_colored(f"Este es el total: €{fare}", "green", "bright")
    return fare

def taximeter():
    """
    Funcion principal del taximetro: manejar y mostrar opciones.
    """
    show_welcome()
    
    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        # Mostrar prompt con estilo
        if trip_active:
            if state == "moving":
                prompt = "🚗 moving > "
            else:
                prompt = "🛑 stopped > "
            print_colored(prompt, "cyan", end="")
        else:
            print_colored("🚕 taxi > ", "yellow", end="")
        
        command = input().strip().lower()

        if command == 'help':
            print_colored(HELP_MENU, "yellow")
            continue

        elif command == 'status':
            show_status(trip_active, state, stopped_time, moving_time)
            continue

        elif command == 'start':
            if trip_active:
                logging.warning("Intento de iniciar viaje con trip activo")
                print_colored("❌ Error: Trip already in progress.", "red")
                print_colored("💡 Use 'finish' to complete current trip first.", "yellow")
                continue
            
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'
            state_start_time = time.time()
            logging.info("Viaje iniciado")
            
            print_colored("✅ Trip started successfully!", "green", "bright")
            print_colored("🛑 Initial state: STOPPED", "yellow")
            print_colored("💡 Use 'move' when the taxi starts moving", "cyan")

        elif command in ("stop", "move"):
            if not trip_active:
                logging.warning("Comando de estado sin viaje activo")
                print_colored("❌ Error: No active trip.", "red")
                print_colored("💡 Use 'start' to begin a new trip.", "yellow")
                continue
            
            # Calcular tiempo en estado anterior
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            state = "stopped" if command == "stop" else "moving"
            state_start_time = time.time()
            logging.info(f"Estado cambiado a: {state}")
            
            if state == "stopped":
                print_colored("🛑 State changed to: STOPPED", "yellow", "bright")
            else:
                print_colored("🚗 State changed to: MOVING", "cyan", "bright")
            
            show_status(trip_active, state, stopped_time, moving_time)

        elif command == 'finish':
            if not trip_active:
                logging.warning("Intento de finalizar viaje sin trip activo")
                print_colored("❌ Error: No active trip to finish.", "red")
                print_colored("💡 Use 'start' to begin a new trip.", "yellow")
                continue

            # Calcular tiempo final
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            total_fare = calculate_fare(stopped_time, moving_time)
            logging.info(f"Viaje finalizado - Tiempo parado: {stopped_time:.1f}s, Tiempo movimiento: {moving_time:.1f}s")
            logging.info(f"Tarifa total calculada: €{total_fare:.2f}")
            
            # Mostrar resumen visual del viaje
            print_colored("\n" + "="*50, "magenta", "bright")
            print_colored("🏁 TRIP COMPLETED - FARE SUMMARY", "magenta", "bright")
            print_colored("="*50, "magenta", "bright")
            print(f"⏱️  Time stopped:  {stopped_time:.1f} seconds  (€{stopped_time * 0.02:.2f})")
            print(f"🚗 Time moving:   {moving_time:.1f} seconds  (€{moving_time * 0.05:.2f})")
            print_colored("─" * 50, "white")
            print_colored(f"💰 TOTAL FARE:    €{total_fare:.2f}", "green", "bright")
            print_colored("="*50 + "\n", "magenta", "bright")

            trip_active = False
            state = None

        elif command == 'exit':
            if trip_active:
                print_colored("⚠️  Warning: You have an active trip!", "yellow")
                confirm = input("🤔 Do you want to finish the trip first? (y/n): ").strip().lower()
                if confirm == 'y':
                    # Auto-finish the trip
                    duration = time.time() - state_start_time
                    if state == 'stopped':
                        stopped_time += duration
                    else:
                        moving_time += duration
                    total_fare = calculate_fare(stopped_time, moving_time)
                    print_colored(f"🏁 Auto-completed trip. Final fare: €{total_fare:.2f}", "green")
                    logging.info(f"Viaje auto-completado al salir - Tarifa: €{total_fare:.2f}")
            
            logging.info("Usuario salió de la aplicación")
            print_colored("\n🌟 Thank you for using Digital Taximeter!", "cyan", "bright")
            print_colored("👋 Goodbye and safe travels!", "yellow")
            break
            
        else:
            logging.warning(f"Comando inválido recibido: '{command}'")
            print_colored(f"❓ Unknown command: '{command}'", "red")
            print_colored("💡 Type 'help' to see available commands.", "yellow")

if __name__ == "__main__":
    logging.info("Iniciando Digital Taximeter")
    taximeter()