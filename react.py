import os
from dotenv import  load_dotenv, find_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv(find_dotenv(), override=True)

