import os

from anthropic import Anthropic 

client = Anthropic(api_key=os.getenv("Anthropic_API_Key"))

tools = [
    {
        "name": "get_ad_spend",
        "description": "Get the total amount spent so far from Google Ad Manager.",
        "input_schema": {
            "type": "object",
            "properties": {
                "date_range": {
                    "type": "string",
                    "description": "Date range to check, like 'today', 'this_month', or 'all_time'."
                }
            },
            "required": ["date_range"]
        }
    },
    {
        "name": "get_ad_count",
        "description": "Get the number of ads currently present in Google Ad Manager.",
        "input_schema": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "description": "Which ads to count, like 'active', 'paused', or 'all'."
                }
            },
            "required": ["status"]
        }
    }
]

system_prompt = """
You are an advertising analytics assistant.

Rules:
1. If the user asks for real metrics, live numbers, counts, spend, performance, or actual business data, you must use the available tool(s).
2. Never guess or invent metric values.
3. If the user asks for general explanations, definitions, help, or conceptual information, respond directly without using tools.
4. If the user asks for both explanation and live data, use the tool for the live data part and answer the explanation part normally.
5. Do not say you will fetch data unless you are actually making a tool call.
"""


def get_ad_spend(date_range: str) :
    return {
        date_range: date_range,
        amount: $150,

    }

def get_ad_count(status: str):
    return {
        status: status,
        count: 42,
    }

def run_tool(tool_name: str, tool_input: dict):
    if tool_name == "get_ad_spend":
        return get_ad_spend(tool_input["date_range"])
    elif tool_name == "get_ad_count":
        return get_ad_count(tool_input["status"])


def call_llm(prompt: str) :

	response = client.messages.create(

			model = "claude-sonnet-4-6",
			max_tokens = 2000,
			tools = tools,
			system=system_prompt,
			messages = [
				{
					"role" : "user",
					"content" : prompt,
		
				}
			] ,
		)

	print (response.content)
	print("stop_reason:", response.stop_reason)
	if(response and response.content and len(response.content) > 0):
		return response.content[0].text
	else:
		return "OOF"


prompt = input("Please state your query! \n")
print(call_llm(prompt))

