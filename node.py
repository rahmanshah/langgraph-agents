from dotenv import load_dotenv, find_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv(find_dotenv(), override=True)

SYSTEM_MESSAGE = """You are a helpful assistant that can use tools to answer questions."""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Takes in a MessagesState and returns a new MessagesState with a single message from the LLM.

    The input MessagesState is passed to the LLM along with a system message.
    The system message is used to prime the LLM and keep it in context.
    The LLM's response is the single message in the returned MessagesState.
    """

    response = llm.invoke([{"role": "system","content": SYSTEM_MESSAGE}, *state.messages])
    return {'messages': [response]}


tool_node = ToolNode(tools)