from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
import os

api_key_gemini = os.getenv('GEMINI_API_KEY', '')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=api_key_gemini)
# Change this variable to test with different identities
person_name = "scarlett johansson"  
# Updated task prompt includes the person_name variable
task = f"Try filling this form with some genuine looking fake data for {person_name}. https://forms.gle/j6B8wxGFFezPeRpZ8"
async def main():
    agent = Agent(
        task=task,
        llm=llm,
    )
    result = await agent.run()
    print(result.final_result())
asyncio.run(main())
