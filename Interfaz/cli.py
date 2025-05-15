from Encuesta.gestor_encuestas import GestorEncuestas

gestor = GestorEncuestas()

def menu():
    while True:
        print("\n--- Administrador de Encuestas ---")
        print("1. Crear nueva encuesta")
        print("2. Listar encuestas activas")
        print("3. Ver resultados de encuesta")
        print("4. Cerrar encuesta manualmente")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            pregunta = input("Pregunta de la encuesta: ")
            opciones = input("Opciones (separadas por coma): ").split(",")
            duracion = int(input("Duración en minutos: "))
            gestor.crear_encuesta(pregunta, opciones, duracion)
            print("Encuesta creada exitosamente.")
        
        elif opcion == "2":
            encuestas = gestor.listar_encuestas_activas()
            print("Encuestas activas:", encuestas)

        elif opcion == "3":
            encuesta_id = input("ID de la encuesta: ")
            resultados = gestor.ver_resultados(encuesta_id)
            print("Resultados:", resultados)

        elif opcion == "4":
            encuesta_id = input("ID de la encuesta: ")
            gestor.cerrar_encuesta(encuesta_id)
            print("Encuesta cerrada.")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

def iniciar_cli():
    """Función que inicia el menú CLI cuando se llama desde main.py"""
    menu()

if __name__ == "__main__":
    iniciar_cli()
