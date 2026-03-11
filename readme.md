# Project Name

## Description
This project is a Python script that loads a PDF document, splits it into smaller chunks of text, creates embeddings for the chunks, and sets up a RetrievalQA chain using the GPT-2 model. The RetrievalQA chain allows for efficient retrieval of relevant documents based on the user's question.

## Installation
1. Clone the repository: `git clone https://github.com/Devprasanna1905/PDF_chatbot.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Run the script: `python app.py`
2. The script will load the PDF document specified by `<pdf_path>`, split it into smaller chunks, create embeddings for the chunks, and set up a RetrievalQA chain.
3. You can then ask questions about the content of the PDF document, and the script will generate answers based on the retrieved documents.

## Configuration
You can configure the following parameters in the `load_rag.py` file:
- `chunk_size`: The maximum length of each chunk of text.
- `chunk_overlap`: The number of characters that should overlap between adjacent chunks.
- `model_name`: The pre-trained model to use for creating embeddings.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please submit a pull request or open an issue on the GitHub repository.
