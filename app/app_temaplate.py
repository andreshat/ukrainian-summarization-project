import gradio as gr
from transformers import pipeline

# Load the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large")


# Function to generate the summary
def generate_summary(input_text, model_name, max_words):
    # Set the model for summarization
    # summarizer.model = model_name

    # Generate the summary
    summary = summarizer(input_text, max_length=max_words, min_length=10, do_sample=False)

    return summary[0]['summary_text']


with gr.Blocks() as demo:
    header = gr.Markdown(
        """
        # 🇺🇦Ukrainian Text Summarization!   
        Start typing below to see the output.
        """
    )
    with gr.Row():
        with gr.Column():
            with gr.Row():
                input_text = gr.Textbox(label="Input Text", lines=4)
            with gr.Row():
                # TODO: Replace gr.inputs.Dropdown with gr.Dropdown
                #  after default fixup in gradio
                model = gr.inputs.Dropdown(
                    choices=["t5-base", "t5-large", "facebook/bart-large", "google/pegasus-xsum"],
                    label="Model",
                    default="facebook/bart-large"
                )
                # TODO: Replace gr.inputs.Slider with gr.Slider
                #  after default fixup in gradio
                max_words = gr.inputs.Slider(
                    minimum=10,
                    maximum=500,
                    default=50,
                    step=10,
                    label="Max Words"
                )
            text_button = gr.Button("Summarize")
        with gr.Column():
            output_text = gr.Textbox(label="Output Summary", lines=4)

    text_button.click(generate_summary, inputs=[input_text, model, max_words], outputs=[output_text])


if __name__ == '__main__':
    demo.launch(debug=True)
