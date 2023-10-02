def format_tasks(tasks):
    lines = []
    for task, subtasks in tasks.items():
        if subtasks:
            subtask_str = format_tasks(subtasks)
            line = f'{task}: {subtask_str}'
        else:
            line = task
        lines.append(line)
    return ', '.join(lines)

def parse_tasks(text, folders_to_remove=None, folders_to_indent=None):
    if folders_to_remove is None:
        folders_to_remove = []
    if folders_to_indent is None:
        folders_to_indent = []

    lines = text.split('\n')  # split the input file into lines
    root = {}
    parents = {}

    for line in lines:
        # Feature 2: Remove tildas
        line = line.replace("~", "")
        
        # Feature 3: Already handled by skipping empty lines
        
        # Feature 5: Remove ///
        line = line.replace("///", "")
        
        # Feature 6: Remove quotations
        line = line.replace("\"", "")
        
        # Feature 8: Remove 1,1 strings
        line = line.replace("1,1", "")
        
        # Skip empty lines and folders to remove
        if not line.strip() or any(folder in line for folder in folders_to_remove):
            continue
            
        # Feature 7: Ensure certain folders are indented
        for folder in folders_to_indent:
            if folder in line:
                line = "    " + line  # Indenting by 4 spaces

        indent = len(line) - len(line.lstrip())
        level = indent // 4  # assuming each level is indented by 4 spaces
        task = line.strip()

        if level > 0:  # if this is a subtask
            # If this is a subtask, add it to its parent task.
            parents[level - 1][task] = {}
            parents[level] = parents[level - 1][task]
        else:  # if this is a top-level task
            # If this is a top-level task, add it to the root.
            root[task] = {}
            parents[level] = root[task]

    return root

# open the input file
with open('input.txt', 'r') as file:
    data = file.read()

# parse the input file
folders_to_remove = ["INFLUENTIAL", "GENERAL", "FINANCE", "CAREER"]
folders_to_indent = ["REMINDERS", "ACTIONS", "QUESTIONS"]

tasks = parse_tasks(data, folders_to_remove, folders_to_indent)

# write the output file
with open('output.txt', 'w') as file:
    for task, subtasks in tasks.items():
        if subtasks:
            subtask_str = format_tasks(subtasks)
            file.write(f'{task}: {subtask_str}\n')
        else:
            file.write(f'{task}\n')