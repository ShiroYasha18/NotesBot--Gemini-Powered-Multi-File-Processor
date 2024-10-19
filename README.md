# Gemini-Powered Multi-File Processor

This project is a Python-based Streamlit application that processes and analyzes unstructured data from PDFs and images using Google Gemini’s Large Language Model (LLM) API. It extracts text from PDFs and images and answers user queries based on the extracted data.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

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
