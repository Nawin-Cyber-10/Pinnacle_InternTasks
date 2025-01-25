import os

def ensure_output_dir():
    """Ensure the output directory exists."""
    if not os.path.exists("output"):
        os.makedirs("output")

ensure_output_dir()
