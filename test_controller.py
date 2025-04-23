from src.model.controller.controller import Controller

if __name__ == "__main__":
    controller = Controller()
    
    # Agregar una estación
    print(controller.agregar_estacion("E001", "Buenos Aires", "34.6S, 58.4W"))
    
    # Iniciar guardado periódico
    print(controller.iniciar_guardado_periodico("E001"))
    
    # Esperar 30 segundos para ver algunos registros
    import time
    time.sleep(30)
    
    # Detener guardado
    print(controller.detener_guardado_periodico())
    
    # Mostrar datos
    print(controller.mostrar_datos())