import time
import pyautogui

def type_spin_command():
    try:
        for char in '/spin':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('space')
        time.sleep(0.055)
        pyautogui.press('enter')
        time.sleep(0.055)
        pyautogui.press('enter')
        time.sleep(5)
        return True
    except Exception as e:
        print(f"Error executing /spin: {e}")
        return False

def type_claimall_command():
    try:
        for char in '/claimall':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('space')
        time.sleep(0.055)
        pyautogui.press('enter')
        time.sleep(0.055)
        pyautogui.press('enter')
        time.sleep(15)
        return True
    except Exception as e:
        print(f"Error executing /claimall: {e}")
        return False

def type_slots_command():
    try:
        for char in '/slots':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('space')
        time.sleep(0.055)
        for char in '100':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('enter')
        time.sleep(9)
        return True
    except Exception as e:
        print(f"Error executing /slots: {e}")
        return False

def type_snakeeyes_command():
    try:
        for char in '/snakeeyes':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('space')
        time.sleep(0.055)
        for char in '100':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('enter')
        time.sleep(9)
        return True
    except Exception as e:
        print(f"Error executing /snakeeyes: {e}")
        return False

def type_dice_command():
    try:
        for char in '/dice':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('space')
        time.sleep(0.055)
        for char in '100':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('enter')
        time.sleep(9)
        return True
    except Exception as e:
        print(f"Error executing /dice: {e}")
        return False

def type_coinflip_command():
    try:
        for char in '/coinflip':
            pyautogui.write(char)
            time.sleep(0.055)
        pyautogui.press('enter')
        time.sleep(0.055)
        pyautogui.write('h')
        time.sleep(0.055)
        pyautogui.press('tab')
        time.sleep(0.165)
        pyautogui.write('h')
        time.sleep(0.165)
        pyautogui.press('enter')
        time.sleep(2.37+3.64)
        return True
    except Exception as e:
        print(f"Error executing /coinflip: {e}")
        return False
