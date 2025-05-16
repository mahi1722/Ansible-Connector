# minimal_agent.py

from crewai import Agent, Task, Crew, Tool
from remediation_agent import run_playbook


# Define the Ansible remediation tool
def remediation_tool(playbook_path: str, target_server_id: str):
    return run_playbook(playbook_path, target_server_id)


# Wrap it in a CrewAI Tool
ansible_tool = Tool(
    name="AnsibleConnector",
    description="Runs an Ansible playbook on a target server",
    func=lambda input: remediation_tool("example.yml", "server01")
)

# Create a simple agent
remediation_agent = Agent(
    role="Remediation Engineer",
    goal="Fix infrastructure issues using Ansible",
    backstory="An expert in automated recovery and orchestration.",
    tools=[ansible_tool],
    verbose=True
)

# Define a task (placeholder)
task = Task(
    description="Execute the remediation playbook using the connector",
    agent=remediation_agent
)

# Create the crew and run it
crew = Crew(
    agents=[remediation_agent],
    tasks=[task]
)

if __name__ == "__main__":
    result = crew.run()
    print("Result:", result)
