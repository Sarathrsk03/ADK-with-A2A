from google.adk.agents.llm_agent import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

from dotenv import load_dotenv
load_dotenv()




root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A summarizer assitant.',
    instruction='Summarize the given text in a concise manner.',
)


a2a_app = to_a2a(root_agent, port=8001)