# NotesBot- Gemini-Powered Multi-File Processor

This project is a Python-based Streamlit application that processes and analyzes unstructured data from PDFs and images using Google Gemini’s Large Language Model (LLM) API. It extracts text from PDFs and images and answers user queries based on the extracted data.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [How It Works](#how-it-works)


## Features

- **Multiple File Uploads**: Users can upload multiple PDFs and images.
- **Text Extraction**: Extract text from PDFs and images using PyMuPDF (fitz) and Tesseract.
- **Query Processing**: Use Google Gemini’s generative AI to answer user queries based on the extracted text.
- **User-Friendly Interface**: Streamlit-powered UI for easy file upload and query submission.

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [Google Gemini API Access](https://ai.google/tools/gemini/)

### Clone the Repository

```bash
git clone https://github.com/your-username/gemini-multi-file-processor.git
cd gemini-multi-file-processor
Here's the given content rewritten in Markdown (`.md`) format:

```markdown
## Environment Variables

To use Google Gemini’s API, you'll need to set up environment variables. The project uses `dotenv` to manage these.

### Create a `.env` file in the project directory:

```bash
touch .env
```

### Add your Gemini API key:

```makefile
GEMINI_API_KEY=your-google-gemini-api-key
```

## Usage

### Start the Streamlit application:

```bash
streamlit run app.py
```

### Open your browser and go to:

```
http://localhost:8501
```

1. Upload your PDF and image files using the interface.
2. Input your query (e.g., "What is the main topic of the handwritten notes?").
3. The application will process the files, extract the text, and provide answers based on the extracted data.

## How It Works

1. **File Upload**: Users upload PDFs and images through the Streamlit interface.
2. **Text Extraction**:
    - **PDFs**: The application uses `PyMuPDF` (fitz) to extract images embedded in PDFs and `Tesseract` for Optical Character Recognition (OCR) to extract text from the images and PDFs.
3. **Knowledge Base Creation**: All extracted text is compiled into a centralized knowledge base.
4. **Gemini API Querying**: The knowledge base and user query are sent to Google Gemini’s LLM API, which generates answers based on the data.
5. **Response Display**: The generated response is shown in the Streamlit interface.
```

This `.md` content is properly formatted for inclusion in a `README.md` or documentation file.
