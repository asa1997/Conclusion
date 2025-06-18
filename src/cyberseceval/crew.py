# from crewai import Crew, Process
# # from cyberseceval.crew import crew
# from cyberseceval.config.agents import agents
# from cyberseceval.config.tasks import tasks

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# crew = Crew(
#   agents=list(agents.values()),
#   tasks=list(tasks.values()),
#   process=Process.sequential
# )


@CrewBase
class ConclusionCrew():
	agents: List[BaseAgent]
	tasks: List[Task]
	
	# Paths to your YAML configuration files
	agents_config = "config/agents.yaml"
	tasks_config = "config/tasks.yaml"
	
	@agent
	def mitre_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['mitre_analyst'],  # type: ignore[index]
			verbose=True,
		)

	@agent
	def frr_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['frr_analyst'],  # type: ignore[index]
			verbose=True,
		)

	@agent
	def instruct_code_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['instruct_code_analyst'],  # type: ignore[index]
			verbose=True,
		)

	@agent
	def autocomplete_code_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['autocomplete_code_analyst'],  # type: ignore[index]
			verbose=True,
		)

	@agent
	def prompt_injection_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['prompt_injection_analyst'],  # type: ignore[index]
			verbose=True,
		)

	@agent
	def code_interp_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['code_interp_analyst'],  # type: ignore[index]
			verbose=True,
		)

	@agent
	def phishing_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['phishing_analyst'],  # type: ignore[index]
			verbose=True,
		)

	@agent
	def conclusion_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['conclusion_writer'],  # type: ignore[index]
			verbose=True,
		)

	@task

# @CrewBase
# class ConclusionCrew:
#     agents: List[Agent]
#     tasks: List[Task]

#     # YAML file paths
#     agents_config = "config/agents.yaml"
#     tasks_config = "config/tasks.yaml"

#     # Define agents using keys from the YAML
#     @agent
#     def mitre_analyst(self) -> Agent:
#         return "mitre_analyst"

#     @agent
#     def frr_analyst(self) -> Agent:
#         return "frr_analyst"

#     @agent
#     def instruct_code_analyst(self) -> Agent:
#         return "instruct_code_analyst"

#     @agent
#     def autocomplete_code_analyst(self) -> Agent:
#         return "autocomplete_code_analyst"

#     @agent
#     def prompt_injection_analyst(self) -> Agent:
#         return "prompt_injection_analyst"

#     @agent
#     def code_interp_analyst(self) -> Agent:
#         return "code_interp_analyst"

#     @agent
#     def phishing_analyst(self) -> Agent:
#         return "phishing_analyst"

#     @agent
#     def conclusion_writer(self) -> Agent:
#         return "conclusion_writer"