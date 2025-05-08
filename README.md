# Gradio Chatbot with Ollama

A simple chatbot interface built with Gradio that uses Ollama for inference.

## Requirements

- Python 3.7+
- Ollama running locally
- Libraries listed in `requirements.txt`

## Setup Instructions

1. **Install Ollama:**
   
   Follow the instructions at [Ollama's official website](https://ollama.ai/) to install Ollama on your system.

2. **Pull a Model:**
   
   Run the following command to pull a model (e.g., llama3):
   ```
   ollama pull llama3
   ```

3. **Install Python Dependencies:**
   
   ```
   pip install -r requirements.txt
   ```

4. **Start Ollama Service:**
   
   Ensure Ollama is running in the background.

5. **Run the Application:**
   
   ```
   python app.py
   ```

6. **Access the Web UI:**
   
   Open your browser and navigate to the URL displayed in the terminal (typically http://127.0.0.1:7860).

## Customization

- To use a different model, change the `model` parameter in the `get_ollama_response` function in `app.py`.
- Adjust the Gradio UI components as needed to fit your requirements.

## Troubleshooting

- If you encounter connection errors, ensure Ollama is running and accessible at http://localhost:11434.
- If the model doesn't respond correctly, check that you've pulled the correct model in Ollama. 