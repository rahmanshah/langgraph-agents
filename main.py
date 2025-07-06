import os

from dotenv import load_dotenv, find_dotenv

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState,StateGraph

from node import run_agent_reasoning,tool_node

load_dotenv(find_dotenv(), override=True)
def main():
    print("Hello from langgraph-agents!")


if __name__ == "__main__":
    main()
