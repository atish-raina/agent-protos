import os

from anthropic import Anthropic 

client = Anthropic(api_key=os.getenv("Anthropic_API_Key"))

def call_llm(prompt: str) :

	response = client.messages.create(

			model = "claude-sonnet-4-6",
			max_tokens = 20,
			messages = [
				{
					"role" : "user",
					"content" : prompt,
		
				}
			] ,
		)

	return response.content[0].text


prompt = input("Please state your query! \n")
print(call_llm(prompt))

