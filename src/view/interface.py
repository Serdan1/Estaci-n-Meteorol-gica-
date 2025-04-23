import gradio as gr
from ..model.controller.controller import Controller

def create_interface():
    """Crea y devuelve la interfaz Gradio."""
    controller = Controller()

    with gr.Blocks() as interface:
        gr.Markdown("# Estación Meteorológica")
        gr.Markdown("Sistema para gestionar estaciones y registros climáticos con cifrado.")

        with gr.Row():
            with gr.Column():
                gr.Markdown("## Agregar Estación")
                id_estacion = gr.Textbox(label="ID de Estación")
                nombre = gr.Textbox(label="Nombre")
                ubicacion = gr.Textbox(label="Ubicación")
                agregar_btn = gr.Button("Agregar Estación")
                agregar_output = gr.Textbox(label="Resultado", interactive=False)
                agregar_btn.click(
                    fn=controller.agregar_estacion,
                    inputs=[id_estacion, nombre, ubicacion],
                    outputs=agregar_output
                )

        with gr.Row():
            with gr.Column():
                gr.Markdown("## Agregar Registro Climático")
                reg_id_estacion = gr.Textbox(label="ID de Estación")
                fecha = gr.Textbox(label="Fecha (ej. 2025-04-23 10:00)")
                temperatura = gr.Number(label="Temperatura (°C)")
                humedad = gr.Number(label="Humedad (%)")
                reg_btn = gr.Button("Agregar Registro")
                reg_output = gr.Textbox(label="Resultado", interactive=False)
                reg_btn.click(
                    fn=controller.agregar_registro,
                    inputs=[reg_id_estacion, fecha, temperatura, humedad],
                    outputs=reg_output
                )

        with gr.Row():
            with gr.Column():
                gr.Markdown("## Buscar Estación")
                buscar_id = gr.Textbox(label="ID de Estación")
                buscar_btn = gr.Button("Buscar")
                buscar_output = gr.Textbox(label="Resultado", interactive=False)
                buscar_btn.click(
                    fn=controller.buscar_estacion,
                    inputs=buscar_id,
                    outputs=buscar_output
                )

        with gr.Row():
            with gr.Column():
                gr.Markdown("## Mostrar Datos")
                mostrar_btn = gr.Button("Mostrar Todas las Estaciones")
                mostrar_output = gr.Textbox(label="Datos", interactive=False, lines=10)
                mostrar_btn.click(
                    fn=controller.mostrar_datos,
                    inputs=None,
                    outputs=mostrar_output
                )

        with gr.Row():
            with gr.Column():
                gr.Markdown("## Guardado Periódico")
                periodica_id = gr.Textbox(label="ID de Estación para Guardado Periódico")
                iniciar_btn = gr.Button("Iniciar Guardado Periódico")
                detener_btn = gr.Button("Detener Guardado Periódico")
                periodica_output = gr.Textbox(label="Resultado", interactive=False)
                
                iniciar_btn.click(
                    fn=controller.iniciar_guardado_periodico,
                    inputs=periodica_id,
                    outputs=periodica_output
                )
                detener_btn.click(
                    fn=controller.detener_guardado_periodico,
                    inputs=None,
                    outputs=periodica_output
                )

    return interface

def launch_interface():
    """Lanza la interfaz Gradio."""
    interface = create_interface()
    interface.launch()

# Propósito: Define una interfaz gráfica con Gradio que interactúa con el Controller para gestionar el sistema.

# Estructura:
# Usa gr.Blocks() para organizar la interfaz en secciones.

# Agregar Estación: Formulario con campos para id_estacion, nombre, y ubicacion, que llama a controller.agregar_estacion.

# Agregar Registro: Formulario con campos para id_estacion, fecha, temperatura, y humedad, que llama a controller.agregar_registro.

# Buscar Estación: Campo para id_estacion, que llama a controller.buscar_estacion.

# Mostrar Datos: Botón que llama a controller.mostrar_datos para mostrar todas las estaciones y registros descifrados.

# Sin diccionarios: La interfaz pasa datos directamente al controlador, que usa listas y arreglos.

# Uso: Proporciona una interfaz web interactiva para el usuario, conectando el modelo y el controlador en el patrón MVC.


# Tras añadir controles del temporizador:

# Nuevos Elementos:
# Añadimos una sección "Guardado Periódico" con un campo para el ID de Estación y dos botones: "Iniciar Guardado Periódico" y "Detener Guardado Periódico".

# El botón "Iniciar" llama a controller.iniciar_guardado_periodico, pasando el ID ingresado.

# El botón "Detener" llama a controller.detener_guardado_periodico.

# Sin diccionarios: La interfaz pasa datos primitivos al controlador.

# Uso: Permite al usuario iniciar y detener el guardado periódico desde la interfaz, cumpliendo el requisito de "cada N tiempo se guarde algo".

