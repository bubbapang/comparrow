import csv

def archive_csv_tasks(filename):
    """Read tasks from a CSV file, return them as a list, and then clear the file."""
    tasks = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(row['idea'])

    # Identify the headers in the CSV file
    headers = reader.fieldnames

    # Clear the CSV file, leaving the headers
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    return tasks

def prepend_to_txt(filename, tasks):
    """Prepend tasks to the top of a text file."""
    with open(filename, 'r') as file:
        content = file.read()

    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
        file.write(content)

def main():
    # Archive tasks from CSV files
    csv1_tasks = archive_csv_tasks('data/list2.csv')
    csv2_tasks = archive_csv_tasks('data/list3.csv')
    
    # Combine tasks from both CSVs
    all_tasks = csv1_tasks + csv2_tasks
    
    # Prepend tasks to the top of archive.txt
    prepend_to_txt('private/lifo-archive.txt', all_tasks)

if __name__ == '__main__':
    main()
