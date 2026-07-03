import os
import requests


def run_command(cmd: str):
    """
    Execute a system command.
    """

    result = os.system(cmd)
    return result


def get_weather(city: str):
    """
    Get weather information for a city.
    """

    url = f"https://wttr.in/{city.lower()}?format=%C+%t"

    response = requests.get(url)

    if response.status_code == 200:
        return f"the weather in {city} is {response.text}"

    return "something went wrong"


available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
}