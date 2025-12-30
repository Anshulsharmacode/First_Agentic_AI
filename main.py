import webbrowser
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent , AgentType
import os 


@tool
def open_webpage(url:str):
    """Open a webpage in the default web browser."""
    webbrowser.open(url)

    return "Webpage opened"

tools =[
    open_webpage
]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5
)

agent = initialize_agent(
    tools= tools,
    llm = llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

print("agent ", agent)

agent.run("Open the youtube 'https://www.wikipedia.org/'")