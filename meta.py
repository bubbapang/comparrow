import subprocess
import time

time_to_wait = .3

# json
subprocess.run(['python', 'jsonify.py'])

print("JSON file created.")

time.sleep(time_to_wait)  

# archive
subprocess.run(['python', 'archive.py'])

print("Tasks archived.")

time.sleep(time_to_wait)  

# move
subprocess.run(['python', 'move.py'])

print("Data moved.")

time.sleep(time_to_wait)  

# summon
subprocess.run(['python', 'summon.py'])

print("App summoned.")
