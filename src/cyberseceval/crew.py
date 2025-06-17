from crewai import Crew, Process
from src.cyberseceval.config.agents import agents
from src.cyberseceval.config.tasks import tasks

crew = Crew(
  agents=list(agents.values()),
  tasks=list(tasks.values()),
  process=Process.sequential
)
