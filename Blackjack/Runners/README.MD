Automated Discord Bot Command Executor
Author: Ved Thakkar
Email: thakkarcved@gmail.com
Date: Version 3.8
Purpose
This program is designed to automate interactions with the Blackjack Discord bot. It runs specified commands at regular intervals to simulate continuous activity, allowing the user to remain AFK (Away From Keyboard) while maintaining engagement with the bot.

Overview
The program is structured into three main files:

commands.py: Contains the functions that simulate typing and sending commands to the Discord bot.
scheduler.py: Manages the scheduling and execution of commands using a priority queue.
main.py: Initializes the system, starts the adder threads, and manages user interactions.
File Descriptions
1. commands.py
This file contains the individual command functions. Each function simulates typing a command and sending it to the Discord bot.

type_spin_command(): Sends the /spin command.
type_claimall_command(): Sends the /claimall command.
type_slots_command(): Sends the /slots 10 command.
type_snakeeyes_command(): Sends the /snakeeyes 10 command.
type_dice_command(): Sends the /dice 10 command.
type_coinflip_command(): Sends the /coinflip command and performs the necessary follow-up actions.
2. scheduler.py
This file handles the scheduling and execution of commands using a priority queue.

countdown_timer(seconds): Displays a countdown timer before executing the next command.
adder(queue, interval, command, priority, pause_event, stop_event): Periodically adds commands to the queue.
execute_queue(queue, pause_event, stop_event): Continuously executes commands from the queue.
user_control(pause_event, stop_event, queue): Provides a command-line interface for the user to pause, resume, stop the execution, or check the queue status.
print_queue(queue): Prints the current state of the queue.
3. main.py
This file initializes the queue, starts the adder threads, and manages user interactions.

Initial Commands: Queues the initial commands (/spin, /claimall, etc.) with specified priorities.
Adder Threads: Starts threads that periodically add commands to the queue.
Executor Thread: Starts the thread that executes commands from the queue.
User Control Thread: Starts the thread that listens for user inputs to control the execution.
How the Queue System Works
Priority Queue
Initialization: A priority queue (PriorityQueue) is used to store commands. Each command is added to the queue with an associated priority.
Execution: Commands are executed in order of their priority. Higher-priority commands are executed before lower-priority ones.
Queue Printing: The current state of the queue is printed whenever a command is added or executed.
Adder System
Function: The adder function periodically adds commands to the queue based on specified intervals.
Threads: Multiple adder threads are created, each responsible for a different command. This ensures that commands are added to the queue at their respective intervals.
Command Intervals
/spin: Requeued every 306 seconds (5.1 minutes).
/claimall: Requeued immediately after execution (runs at startup and then as needed based on user logic).
/coinflip: Requeued every 1500 seconds (25 minutes).
/slots: Requeued every 900 seconds (15 minutes).
/snakeeyes: Requeued every 900 seconds (15 minutes).
/dice: Requeued every 900 seconds (15 minutes).
Detailed Workflow
Initialization (main.py)
Queue Initialization: The initial commands are queued with specified priorities.
Adder Threads: Threads are started for each command, periodically adding them to the queue.
Executor Thread: A thread is started to execute commands from the queue.
User Control Thread: A thread is started to handle user inputs for pausing, resuming, stopping, and checking the queue status.
Command Execution (scheduler.py)
Adder Function: Periodically adds commands to the queue based on their intervals.
Execute Queue Function: Retrieves and executes commands from the queue. After executing a command, it updates the queue and prints the current state.
User Control Function: Listens for user inputs to control the execution (pause, resume, stop, status).
Command Functions (commands.py)
Simulate Typing: Each function simulates typing a command and sending it to the Discord bot.
Execution: Commands are executed with specified delays to simulate real user interaction.
User Feedback and Control
Status Check: Users can check the status of the queue, including the number of commands and the next command to be executed.
Pause/Resume: Users can pause and resume the execution of commands.
Stop: Users can stop the execution of commands.
Queue Printing: The queue is printed every time it is updated, providing real-time feedback on the state of the system.