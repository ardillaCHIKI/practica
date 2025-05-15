from Interfaz.cli import iniciar_cli
from Interfaz.gradio_ui import iniciar_gradio

def main():
    print("Bienvenido a la aplicación del streamer 🎥🎙️")
    print("1. Administrar desde CLI (Streamer)")
    print("2. Acceder como espectador (Gradio UI)")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        iniciar_cli()  # Activa el CLI para el streamer
    elif opcion == "2":
        iniciar_gradio()  # Activa la interfaz Gradio para espectadores
    else:
        print("Opción no válida. Saliendo...")

if __name__ == "__main__":
    main()

