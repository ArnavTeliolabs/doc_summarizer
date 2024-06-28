from transformers import pipeline
import tensorflow.keras as keras
from typing import Optional

# Initialize the summarizer pipeline outside the function to avoid re-initialization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def abstractive_summary(text: str, min_length: Optional[int] = 50, max_length: Optional[int] = None) -> str:
    if not text:
        return "Text is empty or None"
    
    try:
        # Calculate input length
        input_length = len(text.split())

        # Determine max_length based on input length, with a minimum of 50 and a maximum of 512 if not provided
        if max_length is None:
            max_length = max(min(2 * input_length, 512), 50)

        # Generate the summary
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

        if summary:
            return summary[0]['summary_text']
        else:
            return "Summary could not be generated."
    except Exception as e:
        return f"An error occurred: {str(e)}"
