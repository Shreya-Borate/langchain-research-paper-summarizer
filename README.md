# LangChain Research Paper Summarizer

A simple research paper summarization tool built with **LangChain**,
**Groq**, and **Streamlit**.

The project demonstrates how to create a reusable LangChain
`PromptTemplate`, save it as a JSON file, load it into a Streamlit
application, and connect it to an LLM using LCEL.

## Features

-   Select a research paper from a predefined list
-   Choose the explanation style:
    -   Beginner-Friendly
    -   Technical
    -   Code-Oriented
    -   Mathematical
-   Choose the explanation length:
    -   Short
    -   Medium
    -   Long
-   Uses a reusable prompt template
-   Uses Groq's `ChatGroq` model
-   Simple Streamlit user interface

## Technologies Used

-   Python
-   LangChain
-   LangChain Core
-   LangChain Groq
-   Groq API
-   Streamlit
-   python-dotenv

## Project Structure

``` text
langchain-research-paper-summarizer/
│
├── prompt_generator.py   # Creates and saves the prompt template
├── prompt_ui.py          # Streamlit application
├── template.json         # Saved LangChain prompt template
├── .env                  # API key (do not commit)
├── .gitignore
└── README.md
```

## How It Works

The application follows this flow:

``` text
User Input
    ↓
PromptTemplate
    ↓
Formatted Prompt
    ↓
ChatGroq
    ↓
Generated Summary
```

The prompt template contains three variables:

``` text
{paper_input}
{style_input}
{length_input}
```

These values are supplied by the Streamlit interface.

The chain is created using LangChain Expression Language (LCEL):

``` python
chain = template | model
```

The chain is then invoked with:

``` python
result = chain.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})
```

## Installation

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd langchain-research-paper-summarizer
```

### 2. Create a virtual environment

``` bash
python -m venv venv
```

Activate it on Windows:

``` powershell
venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install langchain langchain-core langchain-groq streamlit python-dotenv
```

### 4. Add your Groq API key

Create a `.env` file in the project directory:

``` env
GROQ_API_KEY=your_groq_api_key
```

Do not upload the `.env` file to GitHub.

Make sure `.env` is included in `.gitignore`.

## Running the Application

First, generate the prompt template:

``` bash
python prompt_generator.py
```

This creates:

``` text
template.json
```

Then start the Streamlit application:

``` bash
streamlit run prompt_ui.py
```

The application will open in your browser.

## Important Note

This version does **not** read the actual research paper PDFs. It sends
the selected paper title and the requested explanation preferences to
the language model.

The project can be extended in the future to support:

-   PDF uploads
-   Reading actual research papers
-   Document loaders
-   Text splitting
-   Embeddings
-   Vector databases
-   RAG (Retrieval-Augmented Generation)
-   Question answering over research papers

## Learning Goals

This project was created to practice:

-   LangChain `PromptTemplate`
-   Prompt variables
-   Saving and loading prompts
-   LangChain Expression Language (LCEL)
-   `ChatGroq`
-   `chain.invoke()`
-   Streamlit UI
-   Environment variables with `.env`

