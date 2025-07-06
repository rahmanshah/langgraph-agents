import os
from dotenv import  load_dotenv, find_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv(find_dotenv(), override=True)
@tool
def triple(num:float)->float:
    """
    Returns the input number multiplied by 3.

    Args:
        num (float): The number to triple.

    Returns:
        float: The tripled number.
    """
    return num * 3

tools = [TavilySearch(max_results=1), triple]

llm = ChatGroq(model='llama3-70b-8192',temperature=0.1).bind_tools(tools)