from crewai import Agent
from textwrap import dedent
from langchain.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py


class CustomAgents:
    def __init__(self):
        self.Ollama = Ollama(model="mistral", temperature=0)
        self.search_tool = DuckDuckGoSearchRun()
    def PlantScientist(self):
        return Agent(
            role="Plant Scientist",
            backstory=dedent(f"""You are expert in plant science, including plant growth, development, and breeding.
                             You have a deep understanding of plant biology, genetics, and breeding.
                             You are familiar with the latest research and technologies in plant science).
                             You are able to analyze problems in bullet points
                             You are femiliar with Thailand environment"""),
            goal=dedent(f"""Analyze problems and provide solution in bullet points based on research papers and reference link of the research papers or news"""),
            tools=[self.search_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def Secretary(self):
        return Agent(
            role="Secretary",
            backstory=dedent(f"""You are best in managing the communication between Plant Scientist and Farmer Solution Specialist to Farmer who has less knowledge of technology and science"""),
            goal=dedent(f"""summary the problem and solution in a simple language and communicate to the farmer"""),
            allow_delegation=True,
            verbose=True,
            llm=self.Ollama,
        )