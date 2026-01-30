"""Main entry point for the AI Math Tutor Gradio interface.

Run this file to start the Gradio web UI for the math tutor.
"""
from ui import create_interface


def main():
    """Launch the Gradio interface."""
    print("🚀 Starting AI Math Tutor Gradio UI...")
    interface = create_interface()
    
    print("🌐 Launching interface...")
    interface.launch(share=True)


if __name__ == "__main__":
    main()
