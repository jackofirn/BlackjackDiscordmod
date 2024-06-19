import os
import pyautogui
import keyboard
import threading
import shutil
import psutil
import sys
from tqdm import tqdm
import subprocess

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}: {e}")
        sys.exit(1)

def check_packages():
    required_packages = ["pyautogui", "keyboard", "tqdm", "psutil", "IPython"]
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} not found. Installing...")
            install(package)

def check_python_version():
    if sys.version_info < (3, 6):
        print("Python version is too old. Please upgrade to Python 3.6 or higher.")
        return False
    print("Python version: OK")
    return True

def check_pyautogui():
    try:
        pyautogui.size()
        print("pyautogui: OK")
        return True
    except Exception as e:
        print(f"pyautogui check failed: {e}")
        return False

def check_keyboard():
    try:
        keyboard.is_pressed('a')
        print("keyboard: OK")
        return True
    except Exception as e:
        print(f"keyboard check failed: {e}")
        return False

def check_threads():
    try:
        thread = threading.Thread(target=lambda: None)
        thread.start()
        thread.join()
        print("threading: OK")
        return True
    except Exception as e:
        print(f"threading check failed: {e}")
        return False

def check_permissions():
    try:
        test_file = "test_permission.txt"
        with open(test_file, 'w') as f:
            f.write("Testing write permissions.")
        os.remove(test_file)
        print("Permissions: OK")
        return True
    except Exception as e:
        print(f"Permissions check failed: {e}")
        return False

def check_disk_space(min_required_space_gb=1):
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    if free_gb < min_required_space_gb:
        print(f"Not enough disk space. At least {min_required_space_gb} GB required.")
        return False
    print("Disk space: OK")
    return True

def check_cpu_memory():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    if cpu_usage > 90:
        print(f"High CPU usage: {cpu_usage}%.")
        return False
    if memory_info.percent > 90:
        print(f"High memory usage: {memory_info.percent}%.")
        return False
    print("CPU and Memory: OK")
    return True

def check_network_connectivity(host="8.8.8.8", port=53, timeout=3):
    import socket
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print("Network connectivity: OK")
        return True
    except Exception as e:
        print(f"Network connectivity check failed: {e}")
        return False

def system_check():
    check_packages()
    
    checks = {
        "Python version": check_python_version,
        "pyautogui": check_pyautogui,
        "keyboard": check_keyboard,
        "threading": check_threads,
        "Permissions": check_permissions,
        "Disk space": check_disk_space,
        "CPU and Memory": check_cpu_memory,
        "Network connectivity": check_network_connectivity,
    }

    all_ok = True
    for name, check in tqdm(checks.items(), desc="Running system checks"):
        if not check():
            print(f"{name} check failed.")
            all_ok = False

    if all_ok:
        print("System check passed.")
    else:
        print("System check failed. Please resolve the issues and try again.")
    
    return all_ok
