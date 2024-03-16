from crewai import Task
from textwrap import dedent
# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def problem_dfine(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Research the problem of {var1} in thailand and summarize them
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
    
            Use this variable: {var1}
        """
            ),
            agent=agent,
            expected_output="Summary of the problem in bullet points. and provide solution based on research papers and reference link of the research papers or news",
        )

    def solution_dfine(self, agent):
        return Task(
            description=dedent(
                f"""
            Provide a solution to the problem that recive from Plant Scientist and provide solution based on research papers and reference link of the research papers or news.
                                  
            {self.__tip_section()}

            Make sure to do something else.
        """
            ),
            agent=agent,
            expected_output="A solution to the problem that recive from Plant Scientist and provide solution based on research papers and reference link of the research papers or news. in bullet points",
        )
    def summary(self, agent):
        return Task(
            description=dedent(
                f"""
            summary the problem and solution in a simple language and communicate to the farmer
        """
            ),
            agent=agent,
            expected_output="summary the problem and solution in a simple language and communicate to the farmer",
        )