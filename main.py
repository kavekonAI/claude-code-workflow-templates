import os

class ClaudeCodeTemplate:
    def __init__(self, name, hooks, memory_patterns, instructions):
        self.name = name
        self.hooks = hooks
        self.memory_patterns = memory_patterns
        self.instructions = instructions

    def print_template(self):
        print(f"# {self.name} Template\n")
        print("## Hooks\n")
        for hook in self.hooks:
            print(f"- {hook}\n")
        print("## Memory Patterns\n")
        for pattern in self.memory_patterns:
            print(f"- {pattern}\n")
        print("## Project Instructions\n")
        for i, instruction in enumerate(self.instructions):
            print(f"{i+1}. {instruction}\n")

# Example usage
python_backend_template = ClaudeCodeTemplate(
    "Python Backend Template",
    ["python -m pip install flask", "python app.py"],
    ["{{project_name}}", "{{database_url}}"],
    ["Create a new Python project", "Install required dependencies", "Configure the database"]
)
python_backend_template.print_template()