# src/utils.py

# TODO (Copilot): write a helper function `validate_task(task)` that:
# - accepts `task` (dict)
# - ensures 'title' exists and is non-empty
# - ensures 'priority' is one of ['low','medium','high']
# - returns True if valid, otherwise raises ValueError with message

def validate_task(task):
    if 'title' not in task or not task['title'].strip():
        raise ValueError("Task must have a non-empty 'title'.")
    
    valid_priorities = ['low', 'medium', 'high']
    if 'priority' not in task or task['priority'] not in valid_priorities:
        raise ValueError(f"Task 'priority' must be one of {valid_priorities}.")
    
    return True
# Example usage:
# task = {'title': 'Buy groceries', 'priority': 'medium'}
# validate_task(task)  # Should return True
# Example usage:
# task = {'title': '', 'priority': 'medium'}