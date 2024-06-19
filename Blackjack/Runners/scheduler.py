import time
import threading
import logging
from queue import PriorityQueue

class PrioritizedItem:
    def __init__(self, priority, command):
        self.priority = priority
        self.command = command

    def __lt__(self, other):
        return self.priority < other.priority

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\rNext command in {timer}", end="")
        time.sleep(1)
    print("\rExecuting command now!                ")

def log_command(command_name):
    logging.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {command_name}")

def execute_command(command):
    log_command(command.__name__)
    print(f"Executing {command.__name__}...")
    success = command()
    if success:
        print(f"{command.__name__} executed successfully.")
    else:
        print(f"{command.__name__} failed.")
    return success

def adder(queue, interval, command, priority, pause_event, stop_event):
    while not stop_event.is_set():
        pause_event.wait()
        time.sleep(interval)
        queue.put(PrioritizedItem(priority, command))
        print(f"Added {command.__name__} to the queue with priority {priority}")
        print_queue(queue)

def execute_queue(queue, pause_event, stop_event):
    while not stop_event.is_set():
        pause_event.wait()
        if not queue.empty():
            item = queue.get()
            execute_command(item.command)
            queue.task_done()
            countdown_timer(1)
            print_queue(queue)
        else:
            time.sleep(1)

def user_control(pause_event, stop_event, queue):
    while True:
        user_input = input("Enter 'pause' to pause, 'resume' to resume, 'stop' to stop, 'status' for status: ").strip().lower()
        if user_input == 'pause':
            pause_event.clear()
            print("Execution paused.")
        elif user_input == 'resume':
            pause_event.set()
            print("Execution resumed.")
        elif user_input == 'stop':
            stop_event.set()
            print("Execution stopped.")
            break
        elif user_input == 'status':
            print(f"Queue size: {queue.qsize()}")
            if not queue.empty():
                next_item = queue.queue[0]
                print(f"Next command: {next_item.command.__name__} with priority {next_item.priority}")
            else:
                print("Queue is empty.")
        else:
            print("Invalid command.")

def print_queue(queue):
    print("Current Queue:")
    for item in list(queue.queue):
        print(f"{item.command.__name__} (Priority: {item.priority})")
