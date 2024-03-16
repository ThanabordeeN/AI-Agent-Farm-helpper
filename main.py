import os
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama
from textwrap import dedent
from agent import CustomAgents
from task import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1, ):
        self.var1 = var1
        #self.var2 = var2

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.PlantScientist()
        custom_agent_2 = agents.Solving_Method()
        custom_agent_3 = agents.Secretary()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.problem_dfine(
            custom_agent_1,
            self.var1,
            #self.var2,
        )

        custom_task_2 = tasks.solution_dfine(
            custom_agent_2,
        )
        custom_task_3 = tasks.summary(
            custom_agent_3,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2, custom_agent_3],
            tasks=[custom_task_1, custom_task_2,custom_task_3],
            verbose=1,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew Friendly Farmers AI")
    print("-------------------------------")
    var1 = input(dedent("""What is Your Problem : """))
    #var2 = input(dedent("""Enter variable 2: """))

    custom_crew = CustomCrew(var1)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you Friendly Farmers AI result:")
    print("########################\n")
    print(result)