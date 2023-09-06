import subprocess
import time

subprocess.run(['python', 'jsonify.py'])

print("JSON file created.")

time.sleep(.5)  # Sleeps for 2 seconds

subprocess.run(['python', 'move_data.py'])

print("Data moved.")

time.sleep(.5)  # Sleeps for 2 seconds

subprocess.run(['python', 'brain.py'])

print("Brain activated.")
