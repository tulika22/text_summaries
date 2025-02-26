# Text Summarizer

## Project Description
Text Summarizer is a web application that allows users to input text and get a summarized version of it. Users can specify a persona and a word limit for the summary.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/tulika22/text_summaries.git
    cd text-summarizer
    ```

2. Install the dependencies for the frontend:
    ```sh
    npm install
    ```

3. Install the dependencies for the backend:
    ```sh
    pip install <requirements>
    ```

4. Create a `.env` file in the server directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage
To start the application, follow these steps:

1. Run the backend server:
    ```sh
    python server.py
    ```

2. Run the frontend application:
    ```sh
    npm run dev
    ```

3. Open your browser and navigate to `http://localhost:5173`.


