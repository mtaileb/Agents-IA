from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict
from typing_extensions import TypedDict

# Load environment variables from .env file
load_dotenv()

# Agent Instructions
instructions = """  #1
You are a research planning assistant.

**TASK INSTRUCTIONS**
- You will be given a research topic.
- Begin by using the tool get_research_sources() 
to get a list of available research sources. 
- Constrain your research plan 
only to use the available research sources.
- Your task is to provide a plan for researching this topic.
- Output 5 concise tasks and specify which of the 
available research sources will be used for each task.
"""

class Task(TypedDict):
    step: int
    """Task Step."""
    research_source: str    #2
    """The source to search."""
    description: str
    """Task description."""

class ResearchPlanModel(BaseModel):
    tasks: list[Task]
    """Numbered tasks for research."""
    model_config = ConfigDict(extra='forbid')
    

@function_tool  #3
def get_research_sources() -> list[str]:
    """Provides a list of research sources."""
    search_sources = [  #4
        "Wikipedia",
        "Google",
        "YouTube",
    ]
    return search_sources    
    
agent = Agent(
    name="Research Planner", 
    instructions=instructions,
    output_type=ResearchPlanModel,
    tools=[get_research_sources],  #5
    )

input = "learn about AI agents"

result = Runner.run_sync(
    agent, 
    input=input,
    )

print(result.final_output)


#1 Updated prompt instructions that include mention of using the tool
#2 Adds the research source to the task step object
#3 Wraps the function we want to expose as a tool with decorator
#4 For this example, just returns a static list of research sources
#5 Registers the tool with the agent
