# Claude Configuration - Python Scripting

## Project Context
This is a Python scripting project for automation, data processing, or utilities.

## Memory Patterns
- Remember project-specific module imports
- Track data transformation pipelines
- Note file I/O patterns and paths
- Remember error handling strategies

## Workflow Instructions
1. **When starting a new script**:
   - Begin with shebang and encoding declaration
   - Import standard library modules first
   - Then import third-party packages
   - Finally import local modules

2. **When writing functions**:
   - Write docstrings for all public functions
   - Use type hints where applicable
   - Keep functions focused and small
   - Handle exceptions appropriately

3. **When processing data**:
   - Validate input data early
   - Use generators for large datasets
   - Implement progress indicators for long operations
   - Clean up temporary files

4. **When debugging**:
   - Use logging instead of print statements
   - Implement verbose/debug modes
   - Use pdb for complex debugging
   - Write unit tests for critical functions

## Code Style Guidelines
- Follow PEP 8 conventions
- Use Black formatting style
- Maximum line length: 88 characters
- Use f-strings for string formatting
- Use list/dict comprehensions where appropriate

## Dependencies Management
- Track requirements in requirements.txt
- Use virtual environments
- Pin major versions for stability
- Document optional dependencies

## Common Tasks
- Read/write CSV/JSON files
- Process command-line arguments
- Make HTTP requests
- Schedule tasks
- Send email notifications
- Work with dates and times