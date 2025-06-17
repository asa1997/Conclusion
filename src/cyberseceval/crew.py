from crewai import Crew, Process
# from cyberseceval.crew import crew
from cyberseceval.config.agents import agents
from cyberseceval.config.tasks import tasks

crew = Crew(
  agents=list(agents.values()),
  tasks=list(tasks.values()),
  process=Process.sequential
)
