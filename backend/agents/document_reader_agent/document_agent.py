from .pdf_reader import extract_text_from_pdf
from .text_summarizer import summarize_text
from .quiz_from_document import create_quiz

def handle_document_task(text: str):
    summary = summarize_text(text)
    quiz = create_quiz(text)

    return f"""
### 📘 Summary
{summary}

### 📝 Key Notes
- Bullet points created from text
(LLM auto-generates them)

### ❓ Quiz
{quiz}
"""
