import time
import logging

# Configuración simple de logging
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
    Funcion para calcular la tarifa total en euros
    stopped: 0.02€/s
    moving: 0.05€/s
    """
    logging.info(f"Calculando tarifa: parado={seconds_stopped:.1f}s, movimiento={seconds_moving:.1f}s")
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    # Redondear a 2 decimales para evitar problemas de precisión con dinero
    fare = round(fare, 2)
    print(f"Este es el total: {fare}€")
    return fare

def taximeter():
    """
    Funcion principal del taximetro: manejar y mostrar opciones.
    """
    print("Welcome to Digital Taxi")
    print("Available commands:'start', 'stop', 'move', 'finish', 'exit'\n")
    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        command = input("> ").strip().lower()

        if command == 'start':
            if trip_active:
                logging.warning("Intento de iniciar viaje con trip activo")
                print("Error: Trip already in progress.")
                continue
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'
            state_start_time = time.time()
            logging.info("Viaje iniciado")
            print("Trip started. Initial state: 'stopped'")

        elif command in ("stop", "move"):
            if not trip_active:
                logging.warning("Comando de estado sin viaje activo")
                print("Error: No active trip. Use 'start' to begin.")
                continue
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            state = "stopped" if command == "stop" else "moving"
            state_start_time = time.time()
            logging.info(f"Estado cambiado a: {state}")
            print(f"State changed to '{state}'.")

        elif command == 'finish':
            if not trip_active:
                logging.warning("Intento de finalizar viaje sin trip activo")
                print("Error: No active trip to finish.")
                continue
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            total_fare = calculate_fare(stopped_time, moving_time)
            logging.info(f"Viaje finalizado - Tiempo parado: {stopped_time:.1f}s, Tiempo movimiento: {moving_time:.1f}s")
            logging.info(f"Tarifa total calculada: €{total_fare:.2f}")
            print("\n--- Trip Summary ---")
            print(f"Stopped time: {stopped_time:.1f} seconds")
            print(f"Moving time: {moving_time:.1f} seconds")
            print(f"Total fare: €{total_fare:.2f}")
            print("---------------------\n")

            trip_active = False
            state = None

        elif command == 'exit':
            logging.info("Usuario salió de la aplicación")
            print("Exiting Digital Taxi. Goodbye!")
            break
        else:
            logging.warning(f"Comando inválido recibido: '{command}'")
            print("Invalid command. Please use 'start', 'stop', 'move', 'finish', or 'exit'.")

if __name__ == "__main__":
    logging.info("Iniciando Digital Taximeter")
    taximeter()