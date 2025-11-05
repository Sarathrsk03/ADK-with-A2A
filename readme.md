# Multi-Agent Summarizer

This project demonstrates a multi-agent system built with the Google Agent Development Kit (ADK). It consists of two agents:

*   **Summarizer Agent**: A root agent that provides a text summarization service.
*   **Assistant Agent**: A root agent that can answer questions and delegate summarization tasks to the Summarizer Agent.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your API keys. You can use the `.env.example` as a template.

## Usage

To run the application, you need to start both the summarizer agent and the assistant's web interface.

1.  **Start the Summarizer Agent:**
    Open a terminal and run the following command from the project's root directory:
    ```bash
    uvicorn agent:a2a_app --host localhost --port 8001
    ```
    This will start the summarizer agent, which will be available for the assistant agent to communicate with.

2.  **Start the Assistant Web Interface:**
    Open a second terminal and run the following command:
    ```bash
    adk web -a assistant/agent.py
    ```
    This will launch the ADK web interface, where you can interact with the assistant agent.

Now, you can open your browser and navigate to the web interface to ask the assistant questions or give it text to summarize.
