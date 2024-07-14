# Slack Bot

Slack Bot is an AI-powered chatbot application developed using FastAPI. It integrates OpenAI for natural language processing and Slack for communication. The bot is designed to answer questions and provide support via a Slack channel.

## Setup Instructions

### Prerequisites

- Python 3.10+
- FastAPI
- OpenAI API Key
- Slack Webhook URL

### Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Configure the environment variables:**

    Create a `.env` file in the root directory and add the following configurations:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    MODEL_NAME=your_model_name
    SLACK_WEBHOOK_URL=your_slack_webhook_url
    ```

    recommended openai models are gpt-4o, gpt-4-turbo (due to high context window size recommending gpt-4 models), gpt-3.5-turbo-0125.

### Running the Application

1. **Start the FastAPI server:**

    ```bash
    uvicorn main:app --reload
    ```

2. **Access the Swagger UI:**

    Open your browser and navigate to `http://localhost:8000/docs` to access the Swagger UI where you can interact with the API.

### Project Structure

- **main.py**: The entry point of the application.
- **requirements.txt**: Lists the dependencies required for the project.
- **routers/**: Contains the API routers.
  - **service.py**: API endpoints for answering questions.
- **utilities/**: Contains utility functions.
  - **ai_utils.py**: Utility functions for interacting with the AI model.
  - **generic.py**: Generic utility functions.

### Usage

1. **Trigger the Service API:**

    You can trigger the service API through the Swagger UI by sending a POST request to `/service/answer-questions/` with the required payload.
