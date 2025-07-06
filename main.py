import os

from dotenv import load_dotenv, find_dotenv
from typing import Literal

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState,StateGraph,END

from node import run_agent_reasoning,tool_node

load_dotenv(find_dotenv(), override=True)

def should_continue(state: MessagesState) -> str:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[LAST]
    # If the LLM makes a tool call, then perform an action
    if last_message.tool_calls:
        return ACT
    # Otherwise, we stop (reply to the user)
    return END

AGENT_REASON = 'agent_reason'
ACT = 'act'
LAST = -1

## Initialize the state graph
flow = StateGraph(MessagesState)

# Node
flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)

# Edges
flow.add_conditional_edges(AGENT_REASON,should_continue,
                           {END:END,
                            ACT:ACT})

flow.add_edge(ACT,AGENT_REASON)

app = flow.compile()


app.get_graph().draw_mermaid_png(output_file_path='graph.png')

def main():
    print("Hello from langgraph-agents!")


if __name__ == "__main__":
    main()
