"""
Utility module for generating timestamped log filenames.
The generated filename is based on the provided playbook name and the current timestamp.
"""

from datetime import datetime

def generate_log_filename(playbook):
    # Generate a current timestamp in the format YYYYMMDD_HHMMSS.
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Replace the .yml extension (if present) and create a new filename.
    return f"{playbook.replace('.yml', '')}_{ts}.json"
