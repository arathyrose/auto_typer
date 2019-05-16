
import pyautogui
import time
if __name__ == "__main__":
    n = 10  # The number of times you want the message to be spammed
    message = "Hello\n"  # The message to spam or autotype
    duration = 0.1  # the time alloted to type each letter (in seconds)
    wait_time = 2
    print('Autotyping starts in '+str(wait_time)+' seconds')
    # in this time interval, move the mouse to the text-box and click on it (in seconds)
    time.sleep(wait_time)
    for i in range(0, n):
        pyautogui.typewrite(message, duration)
