
import pyautogui
import time
if __name__ == "__main__":
    n = int(input('Enter the number of times you want the message to be spammed'))
    duration = float(
        input('Enter the time allotted to type each letter (in seconds)'))
    wait_time = int(
        input('How much time would you require for the script to start?'))
    print('Autotyping starts in '+str(wait_time)+' seconds')
    print('Now move the mouse to the text-box and click on it')
    time.sleep(wait_time)
    for i in range(0, n):
        pyautogui.hotkey('ctrl','v') 
        pyautogui.typewrite('\n', duration)
