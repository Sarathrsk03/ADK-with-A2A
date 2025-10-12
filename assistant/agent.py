from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

summarizer_agent = RemoteA2aAgent(
    name="summarizer_agent",
    description="Agent that handles text summarization.",
    agent_card=(
        f"http://localhost:8001/.well-known/agent-card.json"
    ),
)


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for answering questions',
    instruction='Answer user questions to the best of your ability. Delegate to summarizer_agent to summarize the content.',
    sub_agents=[summarizer_agent],
)


