"""
Synchronous runner for executing Ansible playbooks.
This script runs 'ansible-playbook' synchronously, captures its output,
and logs the result using a utility function.
"""

import subprocess
import argparse
import os
from utils.logger import save_log
from utils.timestamp import generate_log_filename

def run_playbook(playbook, target):
    # Copy environment variables and set output format to JSON.
    env = os.environ.copy()
    env["ANSIBLE_STDOUT_CALLBACK"] = "json"

    # Build the ansible-playbook command.
    cmd = ["ansible-playbook", f"playbooks/{playbook}", "-l", target, "-i", "inventory/hosts.ini"]
    
    # Execute the playbook synchronously.
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)

    # Generate a log filename and save the playbook output.
    log_file = generate_log_filename(playbook)
    save_log(result.stdout, log_file)

    return result.returncode

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("playbook", help="Playbook file")
    parser.add_argument("target", help="Target host/group")
    args = parser.parse_args()
    exit(run_playbook(args.playbook, args.target))
