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

def parse_tasks(text):
    lines = text.split('\n') # split the input file into lines
    root = {}
    parents = {}

    for line in lines:
        if not line.strip():  # skip empty lines
            continue
        indent = len(line) - len(line.lstrip())
        level = indent // 4  # assuming each level is indented by 4 spaces
        task = line.strip()
        
        if level > 0: # if this is a subtask
            # If this is a subtask, add it to its parent task.
            parents[level - 1][task] = {}
            parents[level] = parents[level - 1][task]
        else: # if this is a top-level task
            # If this is a top-level task, add it to the root.
            root[task] = {}
            parents[level] = root[task]

    return root

# open the input file
with open('input.txt', 'r') as file:
    data = file.read()

# parse the input file
tasks = parse_tasks(data)

# write the output file
with open('output.txt', 'w') as file:
    for task, subtasks in tasks.items():
        if subtasks:
            subtask_str = format_tasks(subtasks)
            file.write(f'{task}: {subtask_str}\n')
        else:
            file.write(f'{task}\n')