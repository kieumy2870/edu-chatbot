from ui import create_interface

def main():
    print("Init Gradio interface...")
    app_interface = create_interface()
    
    print("Run application...")
    app_interface.launch(share=True)

if __name__ == "__main__":
    main()