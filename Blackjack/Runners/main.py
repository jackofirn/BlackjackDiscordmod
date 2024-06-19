import time
import threading
import keyboard
import logging
from queue import PriorityQueue
from commands import (
    type_spin_command,
    type_claimall_command,
    type_slots_command,
    type_snakeeyes_command,
    type_dice_command,
    type_coinflip_command
)
from scheduler import adder, execute_queue, user_control, print_queue, PrioritizedItem
from system_checks import system_check

try:
    from IPython.display import display, HTML
    ipython_available = True
except ImportError:
    print("IPython not available. Continuing without IPython features.")
    ipython_available = False

if __name__ == "__main__":
    if not system_check():
        print("System check failed. Exiting...")
        exit(1)

    # Set up logging
    logging.basicConfig(filename='command_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

    command_queue = PriorityQueue()
    pause_event = threading.Event()
    stop_event = threading.Event()
    pause_event.set()

    initial_commands = [
        (0, type_claimall_command),
        (1, type_spin_command),
        (2, type_coinflip_command),
        (3, type_slots_command),
        (3, type_snakeeyes_command),
        (3, type_dice_command)
    ]

    for priority, command in initial_commands:
        command_queue.put(PrioritizedItem(priority, command))

    print("Initial commands queued.")
    print_queue(command_queue)

    command_intervals = {
        type_claimall_command: 3605,
        type_spin_command: 309,
        type_coinflip_command: 1500,
        type_slots_command: 900,
        type_snakeeyes_command: 900,
        type_dice_command: 900
    }

    adder_threads = [
        threading.Thread(target=adder, args=(command_queue, command_intervals[type_claimall_command], type_claimall_command, 0, pause_event, stop_event), daemon=True),
        threading.Thread(target=adder, args=(command_queue, command_intervals[type_spin_command], type_spin_command, 1, pause_event, stop_event), daemon=True),
        threading.Thread(target=adder, args=(command_queue, command_intervals[type_coinflip_command], type_coinflip_command, 2, pause_event, stop_event), daemon=True),
        threading.Thread(target=adder, args=(command_queue, command_intervals[type_slots_command], type_slots_command, 3, pause_event, stop_event), daemon=True),
        threading.Thread(target=adder, args=(command_queue, command_intervals[type_snakeeyes_command], type_snakeeyes_command, 3, pause_event, stop_event), daemon=True),
        threading.Thread(target=adder, args=(command_queue, command_intervals[type_dice_command], type_dice_command, 3, pause_event, stop_event), daemon=True),
    ]

    for thread in adder_threads:
        thread.start()

    print("Press space to start...")
    keyboard.wait('space')
    print("Starting in 5 seconds...")
    time.sleep(5)

    executor_thread = threading.Thread(target=execute_queue, args=(command_queue, pause_event, stop_event), daemon=True)
    executor_thread.start()

    user_control_thread = threading.Thread(target=user_control, args=(pause_event, stop_event, command_queue), daemon=True)
    user_control_thread.start()

    executor_thread.join()
    user_control_thread.join()

    print("All initial commands executed.")

