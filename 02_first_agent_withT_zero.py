from agents import Agent, Runner, ModelSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Agent Instructions
instructions = """
You are a research planning assistant.

**TASK INSTRUCTIONS**
- You will be given a research topic.
- Your task is to provide a plan on how to research this topic.
- Output 5 concise tasks (5 words or less) to your plan.
"""

agent = Agent(
    name="Research Planner", 
    instructions=instructions,
    model="gpt-4.1",    #1
    model_settings=ModelSettings(
        temperature=0.0,    #2
        max_tokens=150,    #3
        top_p=1.0,   #4
        frequency_penalty=0.5,  
        presence_penalty=0.5,  
    )
)

input = "learn about AI agents"

result = Runner.run_sync(
    agent,
    input=input,
)

print(result.final_output)

