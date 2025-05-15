"""
Asynchronous runner for executing Ansible playbooks.
This script uses asyncio to run 'ansible-playbook' asynchronously,
captures its output in JSON format, and saves the output to a log file.
"""

import argparse
import asyncio
import os
from utils.logger import save_log
from utils.timestamp import generate_log_filename

async def run_playbook(playbook, target):
    # Copy the current environment and set Ansible output to JSON.
    env = os.environ.copy()
    env["ANSIBLE_STDOUT_CALLBACK"] = "json"

    # Build the command list for executing the playbook.
    cmd = ["ansible-playbook", f"playbooks/{playbook}", "-l", target, "-i", "inventory/hosts.ini"]
    
    # Create a subprocess to run the playbook asynchronously.
    process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT, env=env)
    
    # Capture and decode the process output.
    stdout, _ = await process.communicate()
    output = stdout.decode()
    
    # Generate a log filename based on the playbook name and current timestamp.
    log_file = generate_log_filename(playbook)
    # Save the output to the log file.
    save_log(output, log_file)

    # Return the subprocess exit code.
    return process.returncode

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("playbook", help="Playbook file")
    parser.add_argument("target", help="Target host/group")
    args = parser.parse_args()
    asyncio.run(run_playbook(args.playbook, args.target))
