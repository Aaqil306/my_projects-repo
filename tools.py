import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def get_weather(
    context: RunContext, #type: ignore
    city: str) -> str:
    """
    Get the current weather for a given location.
    """
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.split()
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: (e)")    
        return f"An error occurred while retrieving weather for {city}."
    
@function_tool()
async def search_web(
    context: RunContext,  # type: ignore
    query: str) -> str:
      """
      Search the web using DuckDuckGo.
      """
      try:
        search_tool =DuckDuckGoSearchRun()
        results = DuckDuckGoSearchRun().run(tool_input=query)
    # Log the search results
        logging.info(f"Search results for '{query}': {results}")
        return results
      except Exception as e:
        logging.error(f"Error searching for '{query}': {str(e)}")
        return f"An error occurred while searching for '{query}'."