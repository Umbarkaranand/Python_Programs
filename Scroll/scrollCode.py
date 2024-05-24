import pyautogui
import time

# Wait for the user to focus on the chat window
while(1):
    time.sleep(0.01)  # Adjust as needed

    # Simulate pressing the Page Up key (to scroll up)
    pyautogui.press('pageup')



# Alternatively, you can use the scroll wheel to scroll up
# pyautogui.scroll(10)  # Adjust the amount of scrolling as needed
