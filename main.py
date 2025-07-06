import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)
def main():
    print("Hello from langgraph-agents!")


if __name__ == "__main__":
    main()
