# Multimodal-Tutor-Agent
Problem statement:
Application will accept images, handwritten notes, diagrams, charts, screenshots, PDF pages. and then based on the uploaded doc, it will understand the content, explain in simple language, generate summary, create assignment questions and generate voice naration

Project architecture:
User upload | PDF/image | Groq Vision LLM | Langsmith tracing | Generate: - Explaination - Summary - Assignment - Voice naration | streamlit app

Audio and text
For summary, reasoning- gpt 4o
for speech synthesis- gpt 4o-mini-TTS
