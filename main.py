from src.view.interface import create_interface

def main():
    """Lanza la interfaz Gradio del sistema."""
    interface = create_interface()
    try:
        interface.launch()
    finally:
        interface.close()

if __name__ == "__main__":
    main()

