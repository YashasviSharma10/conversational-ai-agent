import json

from config import client
from prompt import System_prompt
from schema import MyOutput
from tools import available_tools


message_history = [
    {
        "role": "system",
        "content": System_prompt,
    }
]


def run_agent(user_query: str):

    # Add user message to conversation history
    message_history.append(
        {
            "role": "user",
            "content": user_query,
        }
    )

    while True:

        response = client.chat.completions.parse(
            model="gemini-2.5-flash",
            response_format=MyOutput,
            messages=message_history,
        )

        raw_result = response.choices[0].message.content

        parsed_result = response.choices[0].message.parsed

        # Store assistant response
        message_history.append(
            {
                "role": "assistant",
                "content": raw_result,
            }
        )

        # START STEP
        if parsed_result.step == "start":

            print("🔥", parsed_result.content)
            continue

        # TOOL STEP
        if parsed_result.step == "Tool":

            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input

            print(f"🔨 {tool_to_call}({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)

            print(
                f"🔨 {tool_to_call}({tool_input}) = {tool_response}"
            )

            message_history.append(
                {
                    "role": "developer",
                    "content": json.dumps(
                        {
                            "step": "observe",
                            "tool": tool_to_call,
                            "input": tool_input,
                            "output": tool_response,
                        }
                    ),
                }
            )

            continue

        # PLAN STEP
        if parsed_result.step == "plan":

            print("🧠", parsed_result.content)
            continue

        # OUTPUT STEP
        if parsed_result.step == "output":

            print("🤖", parsed_result.content)

            return parsed_result.content