from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, llm
# from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from tools.json_chunk_reader import read_json_chunks
from typing import List

@CrewBase
class ConclusionCrew():
	agents: List[BaseAgent]
	tasks: List[Task]
	
	# Paths to your YAML configuration files
	agents_config = "config/agents.yaml"
	tasks_config = "config/tasks.yaml"

	@llm
	def llama3_llm(self) -> LLM:
		return LLM(
			model='ollama/llama3:8b',  # Specify the model you want to use
			base_url="http://localhost:11434",
			verbose=True  # Enable verbose mode for debugging
		)

	@llm
	def codellama_llm(self) -> LLM:
		return LLM(
			model='codellama:7b',  # Specify the model you want to use
			base_url="http://localhost:11434",
			# temperature=0.5,  # Adjust temperature for response variability
			# max_tokens=2048,  # Set maximum tokens for the response
			verbose=True  # Enable verbose mode for debugging
		)

	@agent
	def mitre_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['mitre_analyst'],  # type: ignore[index]
			verbose=True,
			tools=[read_json_chunks]  # Add JSON chunk reading capability
		)

	@agent
	def frr_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['frr_analyst'],  # type: ignore[index]
			verbose=True,
			tools=[read_json_chunks]  # Add JSON chunk reading capability
		)

	@agent
	def instruct_code_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['instruct_code_analyst'],  # type: ignore[index]
			verbose=True,
			tools=[read_json_chunks]  # Add JSON chunk reading capability
		)

	@agent
	def autocomplete_code_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['autocomplete_code_analyst'],  # type: ignore[index]
			verbose=True,
			tools=[read_json_chunks]  # Add JSON chunk reading capability
		)

	@agent
	def prompt_injection_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['prompt_injection_analyst'],  # type: ignore[index]
			verbose=True,
			tools=[read_json_chunks]  # Add JSON chunk reading capability
		)

	@agent
	def code_interp_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['code_interp_analyst'],  # type: ignore[index]
			verbose=True,
			tools=[read_json_chunks]  # Add JSON chunk reading capability
		)

	@agent
	def phishing_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['phishing_analyst'],  # type: ignore[index]
			verbose=True,
			tools=[read_json_chunks]  # Add JSON chunk reading capability
		)

	@agent
	def conclusion_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['conclusion_writer'],  # type: ignore[index]
			verbose=True,
		)
	
	@task
	def mitre_task(self) -> Task:
		return Task(
			config=self.tasks_config['mitre_eval'],  # type: ignore[index]
			output_file='output/mitre_report.md'  # Specify output file
		)

	@task
	def frr_task(self) -> Task:
		return Task(
			config=self.tasks_config['frr_eval'],  # type: ignore[index]
			output_file='output/frr_report.md'  # Specify output file
		)

	@task
	def instruct_task(self) -> Task:
		return Task(
			config=self.tasks_config['instruct_eval'],  # type: ignore[index]
			output_file='output/instruct_report.md'  # Specify output file
		)

	@task
	def autocomplete_task(self) -> Task:
		return Task(
			config=self.tasks_config['autocomplete_eval'],  # type: ignore[index]
			output_file='output/autocomplete_report.md'  # Specify output file
		)

	@task
	def prompt_injection_task(self) -> Task:
		return Task(
			config=self.tasks_config['prompt_injection_eval'],  # type: ignore[index]
			output_file='output/prompt_injection_report.md'  # Specify output file
		)

	@task
	def code_interp_task(self) -> Task:
		return Task(
			config=self.tasks_config['code_interp_eval'],  # type: ignore[index]
			output_file='output/code_interp_report.md'  # Specify output file
		)

	@task
	def phishing_task(self) -> Task:
		return Task(
			config=self.tasks_config['phishing_eval'],  # type: ignore[index]
			output_file='output/phishing_report.md'  # Specify output file
		)

	@task
	def conclusion_task(self) -> Task:
		return Task(
			config=self.tasks_config['conclusion_task'],  # type: ignore[index]
			output_file='output/conclusion_report.md'  # Specify output file
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=[
				self.mitre_analyst(),
				self.frr_analyst(),
				self.instruct_code_analyst(),
				self.autocomplete_code_analyst(),
				self.prompt_injection_analyst(),
				self.code_interp_analyst(),
				self.phishing_analyst(),
				self.conclusion_writer(),
			],
			tasks=[
				self.mitre_task(),
				self.frr_task(),
				self.instruct_task(),
				self.autocomplete_task(),
				self.prompt_injection_task(),
				self.code_interp_task(),
				self.phishing_task(),
				self.conclusion_task(),
			],
			process=Process.sequential
		)
	