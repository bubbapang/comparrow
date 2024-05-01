# This script processes a task list, formatting and nesting tasks and subtasks.

folders_to_remove = ['INFLUENTIAL', 'GENERAL', 'FINANCE', 'CAREER']

# 1. Read a text file with a list of tasks.
def read_file():
    # Open and read the content of 'input.txt'.
    with open('input.txt', 'r', encoding='utf-8') as f:
        return f.read()

# 2. Format the file: remove empty lines and unwanted characters.
def format_file(file_content):
    # Split the content by lines and remove any that are empty.
    lines = [line for line in file_content.split('\n') if line]
    
    # Remove unwanted quirks and lines with unwanted folders.
    formatted_lines = []
    for line in lines:
        if any(folder in line for folder in folders_to_remove):
            continue  # Skip lines containing unwanted folders.
        # Remove unwanted quirks.
        quirks = ['~', '///', '1,1', ',', '-', '"']
        for quirk in quirks:
            line = line.replace(quirk, '')
        formatted_lines.append(line)
    return formatted_lines

# 3. Nest the tasks.
def nest_tasks(formatted_file):
    nested_tasks = {}
    current_task = None  # Keep track of the current task.
    for line in formatted_file:
        stripped_line = line.strip()
        # Identify main tasks and subtasks.
        if line == stripped_line:
            nested_tasks[stripped_line] = []
            current_task = stripped_line
        elif current_task:  
            nested_tasks[current_task].append(stripped_line)
    return nested_tasks

# 4. Output the nested tasks to a new file.
def write_file(nested_tasks):
    with open('output.txt', 'w', encoding='utf-8') as f:
        for main_task, subtasks in nested_tasks.items():
            # Encode main task to UTF-8 before writing.
            main_task_encoded = main_task.encode('utf-8')
            f.write(main_task_encoded.decode('utf-8'))  # Decode back to string before writing
            
            # Encode subtasks to UTF-8 before writing.
            subtasks_encoded = [subtask.encode('utf-8') for subtask in subtasks]
            if subtasks_encoded:
                # Decode each subtask back to string before joining.
                subtasks_str = [subtask.decode('utf-8') for subtask in subtasks_encoded]
                f.write(' $ ' + ' $ '.join(subtasks_str))
            f.write('\n')


# 5. Run the code.
file_content = read_file()
formatted_file = format_file(file_content)
nested_tasks = nest_tasks(formatted_file)
write_file(nested_tasks)
