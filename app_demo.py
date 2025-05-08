import gradio as gr
import subprocess

def reasoning_qwen3(prompt, mode):
    """
    Process a prompt with Qwen3 using specified reasoning mode.
    
    Args:
        prompt (str): The user's prompt
        mode (str): Either "think" or "no_think" to control reasoning depth
    
    Returns:
        str: Response from Qwen3 model
    """
    prompt_with_mode = f"{prompt} /{mode}"
    try:
        result = subprocess.run(
            ["ollama", "run", "qwen3:8b"],
            input=prompt_with_mode.encode(),
            stdout=subprocess.PIPE,
            check=True
        )
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f"Error running Ollama: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def multilingual_qwen3(prompt, lang):
    """
    Translate or process text in different languages using Qwen3.
    
    Args:
        prompt (str): The user's prompt
        lang (str): Target language for translation
    
    Returns:
        str: Translated or processed text from Qwen3 model
    """
    if lang != "English":
        prompt = f"Translate to {lang}: {prompt}"
    try:
        result = subprocess.run(
            ["ollama", "run", "qwen3:8b"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            check=True
        )
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f"Error running Ollama: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Create the reasoning interface
reasoning_ui = gr.Interface(
    fn=reasoning_qwen3,
    inputs=[
        gr.Textbox(label="Enter your prompt", lines=5),
        gr.Radio(["think", "no_think"], label="Reasoning Mode", value="think")
    ],
    outputs="text",
    title="Qwen3 Reasoning Mode Demo",
    description="Switch between /think and /no_think to control response depth.",
    examples=[
        ["Explain quantum computing", "think"],
        ["Explain quantum computing", "no_think"],
        ["What are the ethical implications of AI?", "think"]
    ]
)

# Create the multilingual interface
multilingual_ui = gr.Interface(
    fn=multilingual_qwen3,
    inputs=[
        gr.Textbox(label="Enter your prompt", lines=5),
        gr.Dropdown(["English", "French", "Hindi", "Chinese"], label="Target Language", value="English")
    ],
    outputs="text",
    title="Qwen3 Multilingual Translator",
    description="Use Qwen3 locally to translate prompts to different languages.",
    examples=[
        ["Hello, how are you today?", "French"],
        ["Artificial intelligence is transforming our world", "Hindi"],
        ["Tell me about the history of computers", "Chinese"]
    ]
)

# Create the tabbed interface
demo = gr.TabbedInterface(
    [reasoning_ui, multilingual_ui],
    tab_names=["Reasoning Mode", "Multilingual"]
)

if __name__ == "__main__":
    print("Starting Gradio app with Qwen3 via Ollama...")
    print("Make sure Ollama is installed and accessible in your PATH")
    
    # Launch the app
    demo.launch(
        server_name="0.0.0.0",  # Bind to all network interfaces
        server_port=7860,       # Use port 7860
        share=False,            # No public URL
        inbrowser=True,         # Open in browser automatically
        debug=True              # Enable debug mode
    ) 