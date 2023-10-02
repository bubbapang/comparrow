import subprocess
import time

# json
subprocess.run(['python', 'jsonify.py'])

print("JSON file created.")

time.sleep(.5)  # Sleeps for 2 seconds

# archive
subprocess.run(['python', 'archive.py'])

print("Tasks archived.")

time.sleep(.5)  # Sleeps for 2 seconds

# move_data
subprocess.run(['python', 'move_data.py'])

print("Data moved.")

time.sleep(.5)  # Sleeps for 2 seconds

# brain
subprocess.run(['python', 'brain.py'])

print("Brain activated.")
