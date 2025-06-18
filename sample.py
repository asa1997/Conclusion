# crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ResearchReportingCrew():
    """Research and Reporting crew for comprehensive topic analysis"""
    
    agents: List[BaseAgent]
    tasks: List[Task]
    
    # Paths to your YAML configuration files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    @before_kickoff
    def prepare_inputs(self, inputs):
        """Modify inputs before the crew starts"""
        print(f"Starting research and reporting on: {inputs.get('topic', 'Unknown topic')}")
        # You can modify inputs here if needed
        return inputs
    
    @after_kickoff
    def process_output(self, output):
        """Process output after the crew finishes"""
        print("Research and reporting completed successfully!")
        print(f"Report saved to: output/report.md")
        return output
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],  # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]  # Add web search capability
        )
    
    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],  # type: ignore[index]
            verbose=True
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']  # type: ignore[index]
        )
    
    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],  # type: ignore[index]
            output_file='output/report.md'  # Specify output file
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the research and reporting crew"""
        return Crew(
            agents=self.agents,  # Automatically collected by @agent decorator
            tasks=self.tasks,    # Automatically collected by @task decorator
            process=Process.sequential,
            verbose=True,
        )