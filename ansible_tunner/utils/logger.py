"""
Utility module for saving log content to a file.
It automatically creates a "logs" directory if it does not already exist.
"""

import os

def save_log(content, filename):
    # Ensure the logs directory exists.
    os.makedirs("logs", exist_ok=True)
    filepath = os.path.join("logs", filename)
    # Write the provided log content to the file.
    with open(filepath, "w") as f:
        f.write(content)
