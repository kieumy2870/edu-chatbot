# Math Solver Chatbot
## ✨ Features

*   **Multi-modal Input:** Accepts math problems via text description or image upload.
*   **AI Powered:** Utilizes Google's Gemini Generative AI model for accurate and detailed step-by-step solutions.
*   **Interactive UI:** Clean and responsive web interface built with Gradio.
*   **Contextual History:** Maintains a session state for continuous interaction.

## 🛠️ Tech Stack

*   [Python 3](https://www.python.org/)
*   [Google Generative AI SDK](https://ai.google.dev/) (Gemini)
*   [Gradio](https://www.gradio.app/) (Web UI)
*   [Pillow](https://python-pillow.org/) (Image Processing)

## 📂 Project Structure

```text
└── ai_service/
    ├── ai_service.py       
    ├── app.py              
    ├── config.py           
    ├── main.py             
    ├── prompt.py           
    ├── requirements.txt    
    ├── ui.py               
    └── .env.example       
```
## Installation
1. Clone the repository:
```
git clone https://github.com/kieumy2870/edu-chatbot.git
cd ai_service
```
2. Create and activate a virtual environment
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
## Configuration
1. Get a Gemini API Key
- Visit Google AI Studio to generate a free API key.
2. Set up Environment Variables
- Rename the .env.example file to .env.
- Open .env and paste your API key.
```
GEMINI_API_KEY=your_actual_api_key_here
```
## Usage
```
python main.py
```
```
Run application...
* Running on local URL:  http://127.0.0.1:7860
* Running on public URL: https://8430d6b43c4bbdd030.gradio.live
```