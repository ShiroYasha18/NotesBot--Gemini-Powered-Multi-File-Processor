from dotenv import load_dotenv
import streamlit as st
import os
import pytesseract
import fitz  # PyMuPDF
from PIL import Image
import io
import google.generativeai as genai

# Load environment variables
load_dotenv()  # take environment variables from .env.

# Configure the Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(knowledge_base, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Pass the entire knowledge base as input along with the prompt
    response = model.generate_content([knowledge_base, prompt])
    return response.text


def input_image_setup(image):
    # Convert the image to a bytes format
    byte_io = io.BytesIO()
    image.save(byte_io, format=image.format)
    image_bytes = byte_io.getvalue()

    image_parts = [
        {
            "mime_type": "image/jpeg",  # Assume jpeg, adjust if necessary
            "data": image_bytes
        }
    ]
    return image_parts


def extract_images_from_pdf(pdf_file):
    pdf_images = []
    pdf_document = fitz.open(stream=pdf_file.getvalue(), filetype="pdf")
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            img_ext = base_image["ext"]
            img = Image.open(io.BytesIO(image_bytes))
            pdf_images.append(img)
    return pdf_images


def extract_text_from_image(image):
    # Extract text using pytesseract
    text = pytesseract.image_to_string(image)
    return text


## Initialize our Streamlit app
st.set_page_config(page_title="Gemini Multi-File Demo")

st.header("Gemini Application")

# Upload multiple files: images or PDFs
uploaded_files = st.file_uploader("Choose files (Images or PDFs)...", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

input_prompt = """
               You are an expert in understanding pdfs and handwritten notes.
               You will receive input images as pdfs & images of notes
               you will have to answer questions based on the input image
               """

# Set up the input prompt
input_text = st.text_input("Input Prompt: ", key="input")
submit = st.button("Process the files")

# Initialize a common knowledge base to store aggregated extracted text
knowledge_base = ""

if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file.type == "application/pdf":
            # Extract images from PDF
            extracted_images = extract_images_from_pdf(uploaded_file)
            if extracted_images:
                for img in extracted_images:
                    extracted_text = extract_text_from_image(img)
                    # Append extracted text to the common knowledge base
                    knowledge_base += f"\nExtracted from {uploaded_file.name}:\n{extracted_text}\n"
            else:
                st.warning(f"No images found in {uploaded_file.name}.")
        else:
            # Handle the case of uploading an image
            image = Image.open(uploaded_file)
            extracted_text = extract_text_from_image(image)
            # Append extracted text to the common knowledge base
            knowledge_base += f"\nExtracted from {uploaded_file.name}:\n{extracted_text}\n"

# Generate response if the user submits the input
if submit and knowledge_base:
    st.write("Generating response from the knowledge base...")
    response = get_gemini_response(knowledge_base, input_text)
    st.subheader("Gemini Response")
    st.write(response)
else:
    st.info("Please upload images or PDFs and press submit.")
