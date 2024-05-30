import psutil
import time
import datetime
from pushbullet import Pushbullet

def count_processes(process_name):
    processes = psutil.process_iter()
    return len([p for p in processes if p.name() == process_name])

process_name = "metin2client.exe"
previous_count = count_processes(process_name)
pb = Pushbullet("YOUR_ACCESS_TOKEN")  # Replace "YOUR_ACCESS_TOKEN" with your actual Pushbullet access token

while True:
    current_count = count_processes(process_name)
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")  # Updated format
    print(f"[{timestamp}] Current number of {process_name} processes: {current_count}")
    
    if current_count == 0:
        # Add timestamp when count is 0 and script stops
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")  # Updated format
        message = f"No {process_name} processes found. Stopping script... at {timestamp}"
        pb.push_note("Process Monitor", message)
        print(message)
        break
    
    if previous_count is not None and current_count < previous_count:
        # Add timestamp to the message
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")  # Updated format
        message = f"Number of {process_name} processes decreased: {previous_count} -> {current_count} at {timestamp}"
        pb.push_note("Process Monitor", message)
        print(message)
    
    previous_count = current_count
    time.sleep(60)  # Adjust the sleep interval as needed 60=1min
